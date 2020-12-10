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

    global userID
    loginData = []

    while True:
        loginData = login(cur, dbConn)  # Login first

        if(loginData[0] != "Exit"): # Contains the user type and the Id
            loginStatus = loginData[0]
            userID = loginData[1]

            loggedIn = True

            while loggedIn:
                # =========== ADMIN ===========
                if loginStatus == "Admin":
                    print("Login como admin")
                # =========== USER ===========
                elif loginStatus == "User":

                    command = "SELECT count(id_msg) FROM mensagem WHERE mensagens_n_lidas = false"
                    cursor.execute(command)
                    unreadMsgs = cursor.fetchone()

                    if (cursor.rowcount == 0):
                        unreadMsgs = 0
                    else:
                        unreadMsgs, = unreadMsgs

                    command = "SELECT pessoa_nome, saldo FROM cliente WHERE pessoa_email = '{userEmail}'".format(
                        userEmail=userID)
                    cursor.execute(command)
                    userData = cursor.fetchone()  # Using , should be ok since the user exists (i.e made the login)

                    userOption = menu.mainMenuUser(userData[0], userData[1], unreadMsgs)

                    if userOption == 1: # Ver artigos
                        while True:
                            userOptionVerArtigos = menu.verArtigosUser()

                            if userOptionVerArtigos == 1: # Ver disponiveis
                                break
                            elif userOptionVerArtigos == 2: # Pesquisa
                                while True:
                                    userOptionVerArtigos = menu.pesquisarArtigosUser(cur, dbConn)
                                    if userOptionVerArtigos == 5:
                                        break
                                    else:
                                        print(userOptionVerArtigos)
                            elif userOptionVerArtigos == 3: # Alugar
                                break
                            elif userOptionVerArtigos == 4:
                                break
                            elif userOptionVerArtigos == 5:
                                break

                    elif userOption == 2: # Artigos Atuais
                        loggedIn = False

                    elif userOption == 3: # Historico e estatisticas
                        loggedIn = False

                    elif userOption == 4: # Caixa de entrada
                        loggedIn = False

                    elif userOption == 5: #Logout
                        loggedIn = False

                else:
                    print("ERROOOOOOUUUUUUUUUU")
        else:
            print("Saindo!")
            return


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
                elif loginAccepted:
                    return "User", userInfo[0]


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
                elif loginAccepted:
                    return "Admin", adminInfo[0]

        elif userOption == 4:
            return "Exit",


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

    menu.resetTerminal()

    print("==== FIM ====")
    time.sleep(10)
    print("\033c")
