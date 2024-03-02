import psycopg2 # pip install psycopg2
import pandas as pd
import names
import random
import os

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

    print("Deleted row with value {value1} in {key1} from table {table_name1}.".format(value1=value, key1=key, table_name1=table_name))

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

def gen_data(length = 25):
    """
    Install first the package "names": pip install names
        https://en.moonbooks.org/Articles/How-to-generate-random-names-first-and-last-names-with-python-/
        https://pynative.com/python-random-sample/
    """

    list_fn  = [names.get_first_name() for _ in range(length)]
    list_age = [random.randint(18, 50) for _ in range(length)]
    list_pv  = random.choices(["left","right"], k=length)

    data = {'firstName': list_fn, 'age': list_age, 'politicalView': list_pv}
    df = pd.DataFrame(data)

    return df

def gen_table():
    ### Create table
    qr = "CREATE TABLE IF NOT EXISTS employee (id serial PRIMARY KEY, \
            firstname text NOT NULL, \
            age INT, \
            politicalView text);"
    db = "week8"

    create_table(qr, db)
    print("Created employee table.")


def prepate_data(ready_data=True):
    print("Data preparation starting ...") 

    if ready_data == True:
        main_dir = r"D:\Documents\python\repo\Introduction_Python"
        # sys.path.append(r"D:\Documents\python\repo\week8_repo") # add folder to path

        ### IMPORT
        df = pd.read_excel(main_dir + os.sep + "3_Dataframe\data\data.xlsx") 

        print("Imported excel data.")
    else: 
        df = gen_data()

        print("Created a random data.")



    return df