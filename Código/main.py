# ==============================================================
# Base de Dados - UCoimbra MiEEC 2020/2021
# Projeto: NETFLOX
# Gonçalo Cavaleiro - UC2018279569
# João Vasco        - UC2019236378
#
# Ficheiro: main.py
#
# Descrição:
# Este ficheiro contém a estrutura básica da aplicação
# Realiza a conexão à base de dados, importando a configuração do
# Ficheiro config.ini e chama os restantes menus.
#
# Tipo Erro:
# "userAlreadyExist"
# "userNotExist"
# "userNoPermission"
#
# Depêndencias              Versão
# Blessed                   1.17.11     https://pypi.org/project/blessed/
# passlib                   1.7.4       https://pypi.org/project/passlib/
# psycopg2                  2.8.6       https://pypi.org/project/psycopg2/
# configparser              Python built-in
# datetime                  Python built-in
# ==============================================================
# ==== Import files ====

import userMenus as user
import adminMenus as admin
import commonMenus as menus

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

        if (loginData[0] != "Exit"):  # Contains the user type and the Id
            loginStatus = loginData[0]
            userID = loginData[1]

            loggedIn = True

            while loggedIn:
                # =========== ADMIN ===========
                if loginStatus == "Admin":
                    command = "SELECT pessoa_nome FROM admin WHERE pessoa_id_pessoa = %s"
                    cursor.execute(command, (userID,))
                    adminData, = cursor.fetchone()  # Using , should be ok since the user exists (i.e made the login)

                    optionAdminMainMenu = admin.mainMenu(adminData)

                    if optionAdminMainMenu == 2:  # Aumentar Saldo
                        admin.aumentarSaldo(cur, dbConn, userID)

                    elif optionAdminMainMenu == 5:  # Logout
                        loggedIn = False

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

                    userOption = user.mainMenu(userData[0], userData[1], unreadMsgs)

                    username = userData[0]

                    if userOption == 1:  # Ver artigos
                        while True:
                            userOptionVerArtigos = user.verArtigos(username)

                            if userOptionVerArtigos == 1:  # Ver todos disponiveis
                                userOptionListarArtigos = user.listarArtigos(cur, dbConn, userID)

                            elif userOptionVerArtigos == 2:  # Pesquisa
                                while True:
                                    userOptionPesquisaArtigos = user.pesquisarArtigos(cur, dbConn, userID)
                                    if userOptionPesquisaArtigos == 5:
                                        break

                            elif userOptionVerArtigos == 3:  # Sair
                                break

                    elif userOption == 2:  # Artigos alugados
                        while True:
                            userOptionArtigosAlugados = user.verArtigosAlugados(username)

                            if userOptionArtigosAlugados == 1:  # Ver todos disponiveis
                                userOptionListarArtigos = user.listarArtigosAlugados(cur, dbConn, userID)
                            elif userOptionArtigosAlugados == 2:  # Pesquisa
                                user.pesquisarArtigosAlugados(cur, dbConn, userID)
                            elif userOptionArtigosAlugados == 3:  # Sair
                                break

                    elif userOption == 3:  # Historico e estatisticas
                        while True:
                            userOptionHistorico = user.verHistoricoEstatisticas(username)

                            if userOptionHistorico == 1:  # Historico
                                user.listarArtigosHistorico(cur, dbConn, userID)

                            elif userOptionHistorico == 2:  # Estatisticas
                                user.estatisticas(cur, dbConn, userID)

                            elif userOptionHistorico == 3:  # Sair
                                break
                    elif userOption == 4:  # Caixa de entrada
                        user.caixaEntrada(cur, dbConn, userID)

                    elif userOption == 5:  # Logout
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
        userOption = menus.firstPage(error)
        error = "None"  # Reset the error code

        if userOption == 1:
            userInfo = menus.userLogin()

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
                userInfo = menus.newAccount()

                encPassword = crypt.hash(userInfo[2])

                command = "INSERT INTO cliente (pessoa_email, pessoa_nome, pessoa_password) VALUES (%s,%s,%s)"
                cur.execute(command, (userInfo[1], userInfo[0], encPassword))
            except psycopg2.errors.UniqueViolation:
                dbConn.rollback()
                error = "userAlreadyExist"
            else:
                dbConn.commit()

        elif userOption == 3:
            adminInfo = menus.adminLogin()

            command = "SELECT pessoa_id_pessoa, pessoa_password FROM admin WHERE pessoa_email = %s"
            cursor.execute(command, (adminInfo[0],))
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

    user.resetTerminal()

    print("==== Obrigado por usar o netFLOX ====")
    time.sleep(5)
    print("\033c")
