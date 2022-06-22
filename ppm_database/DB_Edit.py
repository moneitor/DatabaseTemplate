import sqlite3 as sq
from pprint import pprint as pp

import os

db = "./sequences.db"

conn = sq.connect(db)
cursor = conn.cursor()

cursor.execute('SELECT * FROM sequences;')
#cursor.execute('DELETE FROM sequences WHERE name = ?;',  ("circular_corridor",))
#cursor.execute('SELECT * FROM sequences WHERE rowid = (?);', "circular_corridor")

projects = cursor.fetchall()
pp(projects)

conn.commit()
conn.close()

#print("###################################")

