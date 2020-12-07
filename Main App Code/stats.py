import configparser
import time
import psycopg2

def main(cur, dbConn):
    print("Faz as coisas aqui, cur  é o cursor, dbConn é a conexão à base de dados")


# ======================================================================================================================
def connectToDB():
    config = configparser.ConfigParser()
    config.read('config.ini')

    configParams = config.items("PostgresDB_Credentials")

    dbParams = {}

    for i in configParams:
        dbParams[i[0]] = i[1]

    db = psycopg2.connect(**dbParams)

    dbCursor = db.cursor()

    return dbCursor, db


# ======================================================================================================================


if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    cursor, conn = connectToDB()

    dbStatus = conn.get_dsn_parameters()
    print(dbStatus['dbname'], "@", dbStatus['host'], sep="")

    time.sleep(1)

    main(cursor, conn)

    cursor.close()
    conn.close()

    print("==== FIM ====")
    time.sleep(2)
    print("\033c")
