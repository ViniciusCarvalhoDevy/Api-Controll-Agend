import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Vini5119#",
    database="controllagend"
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
        print("Conectado ao banco:", result)
finally:
    connection.close()