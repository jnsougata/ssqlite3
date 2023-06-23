import io
import deta
import sqlite3
import hashlib


class Block:
    def __init__(self, **kwargs):
        self.chunk = kwargs["chunk"]
        self.hash = kwargs.get("hash", "")
        self.index = int(kwargs["key"])


class SQLBase(deta._Base):

    def __init__(self,  db_name: str, project_key: str):
        super().__init__(
            name=db_name,
            project_key=project_key,
            project_id=project_key.split("_")[0],
        )
        self.conn = None
        self.block_hahses = {}
    
    def connect(self,):
        self.conn = sqlite3.connect(":memory:")
        resp = self.fetch()
        items = resp.items
        while resp.last:
            resp = self.fetch(last=resp.last)
            items += resp.items
        if not items:
            return
        items = [Block(**item) for item in items]
        items = sorted(items, key=lambda x: x.index)
        self.script = "".join([item.chunk for item in items])
        for item in items:
            self.block_hahses[item.index] = item.hash
        self.conn.cursor().executescript(self.script)
    
    def commit(self):
        self.conn.commit()
        tempfile = io.StringIO()
        for line in self.conn.iterdump():
            tempfile.write("%s\n" % line)
        tempfile.seek(0)
        data = tempfile.read()
        chunk_size = 300 * 1024
        chunks = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]
        updates = []
        for i, chunk in enumerate(chunks):
            previous_hash = self.block_hahses.get(i, "")
            current_hash = hashlib.sha256(chunk.encode()).hexdigest()
            if previous_hash and previous_hash == current_hash:
                continue
            updates.append({"chunk": chunk, "hash": current_hash, "key": str(i)})
        if updates:
            batches = [updates[i : i + 25] for i in range(0, len(updates), 25)]
            for batch in batches:
                self.put_many(batch)
    
    def close(self):
        self.conn.close()
        