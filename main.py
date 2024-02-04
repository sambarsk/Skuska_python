import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    port = '3306',
    database = 'auta'
)

cursor = connection.cursor()
sql_query = "SELECT * FROM slovenske_mesta"
cursor.execute(sql_query)
results = cursor.fetchall()

def sucet(a, b):

    c = a + b
    return c

print(sucet(91, 1))

for row in results:
    print(row)

# Zatvorenie kurzora a pripojenia
cursor.close()
connection.close()