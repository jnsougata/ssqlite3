# ssqlite3

## Installation

```bash
pip install git+https://github.com/jnsougata/ssqlite3.git
```

# Usage

```python
from ssqlite3 import SQLBase

# Create a database
db = SQLBase(
    db_name="sqldb", 
    project_key="collection_key"
)
db.connect()
```
```python
# Create a table and insert some data
db.conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
db.conn.execute("INSERT INTO users (id, name, age) VALUES (1, 'John', 25)")
db.conn.execute("INSERT INTO users (id, name, age) VALUES (2, 'Jane', 22)")
db.conn.execute("INSERT INTO users (id, name, age) VALUES (3, 'Bob', 30)")
db.conn.execute("INSERT INTO users (id, name, age) VALUES (4, 'Alice', 27)")
db.commit()
```

```python
# Add new attr to the table
db.conn.execute("ALTER TABLE users ADD city TEXT")
db.commit()
```

```python
# Update data
db.conn.execute("UPDATE users SET city='New York' WHERE id=1")
db.commit()
```

```python
# print all the users with name starting with J
users = db.conn.execute("SELECT * FROM users WHERE name LIKE 'J%'").fetchall()
print(users)
```
- don't forget to commit the changes after doing a bunch of oprations.

