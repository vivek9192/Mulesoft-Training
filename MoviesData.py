import sqlite3
con= sqlite3.connect('Movies.db')
print(con) 

con.cursor()


con.execute("INSERT INTO Movies VALUES('KGF','Yash','Srinidhi','Prashanth Neel','2018-12-31')")
con.execute("INSERT INTO Movies VALUES('KGF2','Yash','Srinidhi','Prashanth Neel','2022-04-14')")
con.execute("INSERT INTO Movies VALUES('Vikram','Kamal Hassan','Shivani','Lokesh','2022-06-03')")
con.execute("INSERT INTO Movies VALUES('RRR','NTR','Olivia','Rajamouli','2022-03-24')")


con.commit()
con.close()
