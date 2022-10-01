import psycopg2 # pip install psycopg2


def connect_db(host, port, user, password, database):
    connection = psycopg2.connect(
            user = user,
            password = password,
            host = host, 
            port = port,
            database = database
        )

    return connection


def close_connection(connection, cursor):
    connection.close()
    cursor.close()


def create_table(query, db_name):
    connection = connect_db("localhost","5432","postgres","postgres",db_name)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    close_connection(connection,cursor)


def insert_into_table(values, table_name, db_name):
    connection = connect_db("localhost","5432","postgres","postgres",db_name)
    cursor = connection.cursor()

    query = "INSERT INTO " + table_name + "(firstname, age, politicalView) \
                VALUES (""'"  + values[1] + "',"  + str(values[2])+ ",'"  + values[3] + "');"
    cursor.execute(query)
    connection.commit()

    close_connection(connection,cursor)

def delete_from_table(key, value, table_name, db_name):
    connection = connect_db("localhost","5432","postgres","postgres",db_name)
    cursor = connection.cursor()

    query = "DELETE FROM " + table_name + " WHERE " + key + "=" + str(value) + ";"
    cursor.execute(query)
    connection.commit()

    close_connection(connection,cursor)
