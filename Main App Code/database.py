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

    return cursor, db


if __name__ == '__main__':
    print("Database")
