import psycopg2 # pip install psycopg2
import pandas as pd

def connect_db(host, port, user, password, database):
    connection = psycopg2.connect(
            user     = user,
            password = password,
            host     = host, 
            port     = port,
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
         VALUES (""'"  + values[0] + "',"  + str(values[1])+ ",'"  + values[2] + "');"
    cursor.execute(query) # comment

    connection.commit()
    close_connection(connection,cursor)

def delete_from_table(key, value, table_name, db_name):
    connection = connect_db("localhost","5432","postgres","postgres",db_name)
    cursor = connection.cursor()

    query = "DELETE FROM " + table_name + " WHERE " + key + "='" + str(value) + "';"
    cursor.execute(query)
    connection.commit()

    close_connection(connection,cursor)

def update_table(set_key, set_value, cond_key, cond_value, table_name, db_name):
    connection = connect_db("localhost","5432","postgres","postgres",db_name)
    cursor = connection.cursor()

    query = "UPDATE " + table_name + " SET " + set_key + "=" + str(set_value) + " WHERE " + cond_key + "='" + str(cond_value) + "';"
    cursor.execute(query)
    connection.commit()

    close_connection(connection,cursor)

def read_table(cond_key, cond_value, table_name, db_name):
    connection = connect_db("localhost","5432","postgres","postgres",db_name)
    cursor = connection.cursor()

    query = "SELECT * FROM " + table_name + " WHERE " + cond_key + "= '" + str(cond_value) + "';"
    cursor.execute(query)
    record = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(record)
    df.columns = colnames

    close_connection(connection,cursor)

    return df
