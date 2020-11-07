import configparser
import psycopg2

def connectToDB():
    config = configparser.ConfigParser()
    config.read('config.ini')

    configParams = config.items("PostgresDB_Credentials")

    dbParams = {}

    for i in configParams:
        dbParams[i[0]] = i[1]

    db = psycopg2.connect(**dbParams)

    cursor = db.cursor()
    # Print PostgreSQL Connection properties
    print(db.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    return cursor



