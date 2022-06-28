import sqlite3

con = sqlite3.connect('Movies.db')
cur = con.cursor()

#run query to show all
cursor = cur.execute("SELECT * FROM Movies")
print(cur.fetchall())


# Query to fetch only movie name and lead actor
cur.execute("SELECT Actor From Movies")
print(cur.fetchall())

con.commit()
con.close()
