import mysql.connector

__connect = None


def get_sql_connection():
    global __connect
    if __connect is None:
        __connect = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='pharmacy_schema')
    return __connect
