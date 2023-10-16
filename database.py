import sqlite3

base = sqlite3.connect('database.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS data(login PRIMARY KEY, password)'.format('data'))
base.commit()

# cur.execute('INSERT INTO data VALUES (?, ?)', ('jonny123', '12345678'))
# base.commit()