import sqlite3

conn = sqlite3.connect('DataLab2')
cur = conn.cursor()
cur.execute("select sklady.kod, sklady.vmest from sklady inner join yasshiki on sklady.kod = yasshiki.sklad group by "
            "sklady.kod having count(yasshiki.kod) > sklady.vmest;")

a = cur.fetchone()

print("Первое задание: " + "kod:", a[0], ", sklad:", a[1], sep="")

# второе задание
conn = sqlite3.connect('DataLab3')
cur = conn.cursor()
cur.execute("")
