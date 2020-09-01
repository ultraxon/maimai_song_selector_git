import sqlite3

conn = sqlite3.connect('maimai_info.db')
print("Opened database successfully")

c = conn.cursor()
c.execute('CREATE INDEX QUERY_INDEX ON MAIMAI_MUSIC_INFO (STARS, DIFFICULTY, CATEGORY);')

conn.commit()
conn.close()
