import configparser
import psycopg2

def startUp():
    db = connect()

    cursor = db.cursor()
    # Print PostgreSQL Connection properties
    print(db.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    return cursor


def connect():
    dbParams = getConfig()
    database = psycopg2.connect(**dbParams)

    return database


def getConfig():
    config = configparser.ConfigParser()
    config.read('config.ini')

    configParams = config.items("PostgresDB_Credentials")

    outParams = {}

    for i in configParams:
        outParams[i[0]] = i[1]

    return outParams



