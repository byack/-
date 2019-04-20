import sqlite3

conn = sqlite3.connect('travel_date.db')
curs = conn.cursor()

curs.execute("""
CREATE TABLE travel_date(
    username TEXT,
    region1 TEXT,
    region2 TEXT,
    region3 TEXT,
    region4 TEXT,
    region5 TEXT
)
""")

conn.commit()
curs.close()
conn.close()