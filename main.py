import mysql.connector

connection = mysql.connector.connect(
    host = "jdbc:mysql://localhost:3306",
    user = "root",
    password = "root",
    database = "auta"
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