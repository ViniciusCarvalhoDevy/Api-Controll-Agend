import pymysql


def testConnection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="asdasdas#",
        database="controllagend"
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            result = cursor.fetchone()
            print("Conectado ao banco:", result)
    finally:
        connection.close()