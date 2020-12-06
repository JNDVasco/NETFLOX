# ==============================================================
# Base de Dados - UCoimbra MiEEC 2020/2021
# Projeto: NETFLOX
# Gonçalo Cavaleiro - UC2018279569
# João Vasco        - UC2019236378
#
# Ficheiro: Main
#
# Descrição:
#
# Tipo Erro:
# "userAlreadyExist"
# "userNotExist"
# "userNoPermission"
# Depêndencias              Versão
# ==============================================================
# ==== Import files ====

# import database as db
import menus as menu

import time
from passlib.hash import sha256_crypt as crypt
import psycopg2
import configparser


# ==== startUp funtion ====
# ==== End startUp funtion ====

def main(cur, dbConn):

    #Start by login

# ======================================================================================================================
def login(cur, dbConn):
    error = "None"
    while True:
        userOption = menu.firstPage(error)
        error = "None"  # Reset the error code

        if userOption == 1:
            userInfo = menu.userLogin()

            command = "SELECT pessoa_password FROM cliente WHERE pessoa_email = '{userEmail}'".format(
                userEmail=userInfo[0])
            cursor.execute(command)
            data = cursor.fetchone()

            if (cursor.rowcount == 0):
                error = "userNotExist"
            else:
                truePwd, = data
                loginAccepted = crypt.verify(userInfo[1], truePwd)
                if not loginAccepted:
                    error = "wrongPassword"


        elif userOption == 2:
            createdUser = False
            error = False

            try:
                userInfo = menu.newAccount()

                encPassword = crypt.hash(userInfo[2])

                command = "INSERT INTO cliente (pessoa_email, pessoa_nome, pessoa_password) VALUES ('{email}','{nome}','{password}')".format(
                    email=userInfo[1], nome=userInfo[0], password=encPassword)

                cur.execute(command)
            except psycopg2.errors.UniqueViolation:
                dbConn.rollback()
                error = "userAlreadyExist"
            else:
                dbConn.commit()

        elif userOption == 3:
            adminInfo = menu.adminLogin()

            command = "SELECT pessoa_password FROM admin WHERE pessoa_email = '{adminEmail}'".format(
                adminEmail=adminInfo[0])
            cursor.execute(command)
            data = cursor.fetchone()

            if (cursor.rowcount == 0):
                error = "userNoPermission"
            else:
                truePwd, = data
                loginAccepted = crypt.verify(adminInfo[1], truePwd)
                if not loginAccepted:
                    error = "wrongPassword"


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
