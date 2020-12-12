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
                    command = "SELECT count(id_msg) FROM mensagem WHERE mensagens_lida = false"
                    cursor.execute(command)
                    unreadMsgs = cursor.fetchone()

                    if (cursor.rowcount == 0):
                        unreadMsgs = 0
                    else:
                        unreadMsgs, = unreadMsgs

                    command = "SELECT pessoa_nome, saldo FROM cliente WHERE pessoa_id_pessoa = %s"
                    cursor.execute(command, (userID,))
                    userData = cursor.fetchone()  # Using , should be ok since the user exists (i.e made the login)

                    userOption = menu.mainMenuUser(userData[0], userData[1], unreadMsgs)

                    username = userData[0]

                    if userOption == 1: # Ver artigos
                        while True:
                            userOptionVerArtigos = menu.verArtigosUser(username)

                            if userOptionVerArtigos == 1: # Ver todos disponiveis
                                    userOptionListarArtigos = menu.listarArtigosUser(cur, dbConn, userID)

                            elif userOptionVerArtigos == 2: # Pesquisa
                                while True:
                                    userOptionPesquisaArtigos = menu.pesquisarArtigosUser(cur, dbConn, userID)
                                    if userOptionPesquisaArtigos == 5:
                                        break

                            elif userOptionVerArtigos == 3: # Sair
                                break

                    elif userOption == 2: # Artigos alugados
                        while True:
                            userOptionArtigosAlugados = menu.verArtigosAlugadosUser(username)

                            if userOptionArtigosAlugados == 1: # Ver todos disponiveis
                                    userOptionListarArtigos = menu.listarArtigosAlugadosUser(cur, dbConn, userID)
                            elif userOptionArtigosAlugados == 2: # Pesquisa
                                while True:
                                        break

                            elif userOptionArtigosAlugados == 3: # Sair
                                break

                    elif userOption == 3: # Historico e estatisticas
                        while True:
                            userOptionHistorico = menu.verHistoricoEstatisticas(username)

                            if userOptionHistorico == 1:  # Historico
                                menu.listarArtigosHistoricoUser(cur, dbConn, userID)

                            elif userOptionHistorico == 2:  # Estatisticas
                                menu.estatisticasUser(cur, dbConn, userID)

                            elif userOptionVerArtigos == 3:  # Sair
                                break
                    elif userOption == 4: # Caixa de entrada
                        menu.caixaEntradaUser(cur, dbConn, userID)

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

            command = "SELECT pessoa_id_pessoa, pessoa_password FROM cliente WHERE pessoa_email = %s"
            cursor.execute(command, (userInfo[0],))
            data = cursor.fetchone()

            if (cursor.rowcount == 0):
                error = "userNotExist"
            else:
                truePwd = data[1]
                loginAccepted = crypt.verify(userInfo[1], truePwd)
                if not loginAccepted:
                    error = "wrongPassword"
                elif loginAccepted:
                    return "User", data[0]


        elif userOption == 2:
            createdUser = False
            error = False

            try:
                userInfo = menu.newAccount()

                encPassword = crypt.hash(userInfo[2])

                command = "INSERT INTO cliente (pessoa_email, pessoa_nome, pessoa_password) VALUES (%s,%s,%s)"
                cur.execute(command,(userInfo[1], userInfo[0], encPassword))
            except psycopg2.errors.UniqueViolation:
                dbConn.rollback()
                error = "userAlreadyExist"
            else:
                dbConn.commit()

        elif userOption == 3:
            adminInfo = menu.adminLogin()

            command = "SELECT pessoa_id_pessoa, pessoa_password FROM admin WHERE pessoa_email = %s"
            cursor.execute(command, (adminInfo[0]))
            data = cursor.fetchone()

            if (cursor.rowcount == 0):
                error = "userNoPermission"
            else:
                truePwd = data[1]
                loginAccepted = crypt.verify(adminInfo[1], truePwd)
                if not loginAccepted:
                    error = "wrongPassword"
                elif loginAccepted:
                    return "Admin", data[0]

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
