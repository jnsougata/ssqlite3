from setuptools import setup



setup(
    name='ssqlite3',
    version='0.0.1',
    description='A simple wrapper around Deta Base to use SQLite3 in Python',
    url='https://github.com/jnsougata/space-sqlite3',
    author='jnsougata',
    author_email='jnsougata@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    packages=['ssqlite3'],
    keywords='sqlite3 deta base',
    python_requires='>=3.8.0',
    install_requires=['deta']
)