import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = 'root',
    database = 'auta'
)

cursor = connection.cursor()
sql_query = "SELECT * FROM slovenske_mesta ORDER BY mesto"
cursor.execute(sql_query)
results = cursor.fetchall()

def sucet(a, b):

    c = a + b
    return c

print(sucet(91, 1))

mesta = []
id_cisla = []

for row in results:
    print(row)
    mesta.append(row[1])
    id_cisla.append(row[0])

print(mesta)
print(id_cisla)

def sucetIDCisiel(zoznam):
    sucet = 0
    for i in zoznam:
        sucet += i

    return sucet

print(sucetIDCisiel(id_cisla))

# Zatvorenie kurzora a pripojenia
cursor.close()
connection.close()