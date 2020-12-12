# ==============================================================
# Base de Dados - UCoimbra MiEEC 2020/2021
# Projeto: NETFLOX
# Gonçalo Cavaleiro - UC2018279569
# João Vasco        - UC2019236378
#
# Ficheiro: menus.py
#
# Descrição:
#
#
# Colors
# Main:        palegreen1
# Secondary:   lightcyan
# Error:       tomato
#
# print(term.home + term.on_blue + term.clear) Clear Screen
# ==============================================================
import datetime
import textwrap
import time

import psycopg2
from blessed import Terminal

# Create the terminal
term = Terminal()
# Create the text wrapper
wrapper = textwrap.TextWrapper(width=60)
# Border, keeps everything a bit more together
borderX = term.width // 5
borderY = term.height // 6


# ==== Get User Input ====
# This funtion get the user input, forces to be an integer
# Status: Done
def getUserInput_Integer(str, posY, maxOption=100, minOption=1):
    str = str + ": "
    errorStr = "Dê-me o número correspondente à opção!"
    invalidOption = "Opção inváilda!"

    print(term.move_xy(0, borderY + posY) + term.black + term.clear_eol)
    print(term.move_xy(0, borderY + posY + 1) + term.black + term.clear_eol)

    posX = ((term.width // 2) - (len(str) // 2))

    while True:
        try:
            userInput = int(input(term.move_xy(posX, borderY + posY + 1) + term.lightcyan + str))
        except ValueError:
            print(term.center(term.move_y(borderY + posY) + term.tomato + errorStr))
            print(term.center(term.move_y(borderY + posY + 1) + term.move_right + term.black + term.clear_eol))
            continue
        else:
            if minOption <= userInput <= maxOption:
                print(term.move_xy(0, borderY + posY) + term.black + term.clear_eol)
                return userInput
            else:
                print(term.move_xy(0, borderY + posY) + term.black + term.clear_eol)
                print(term.center(term.move_y(borderY + posY) + term.tomato + invalidOption))
                print(term.center(term.move_y(borderY + posY + 1) + term.move_right + term.black + term.clear_eol))


# ==== Get User Input ====
# This funtion get the user input, forces to be an email
# Just checks if there is a "@" present
# Removes all spaces at the start and the end
# Status: Done
def getUserInput_Email(str, posY):
    str = str + ": "
    errorStr = "Dê-me um email válido!"

    print(term.move_xy(0, borderY + posY) + term.black + term.clear_eol)
    print(term.move_xy(0, borderY + posY + 1) + term.black + term.clear_eol)

    posX = ((term.width // 2) - (len(str) // 2))

    while True:
        userInput = input(term.move_xy(posX, borderY + posY + 1) + term.lightcyan + str)
        userInput = userInput.strip()  # Remove all spaces at start and end
        userInput = userInput.lower()  # Change all chars to lowercase

        if userInput.find("@") == -1:
            print(term.center(term.move_y(borderY + posY) + term.tomato + errorStr))
            print(term.center(term.move_y(borderY + posY + 1) + term.move_right + term.black + term.clear_eol))
        else:
            break
    print(term.move_xy(0, borderY + posY) + term.black + term.clear_eol)
    return userInput


# ==== Get User Input ====
# This funtion get the user input, forces to be an string
# Just checks if there is any char after removing spaces
# Removes all spaces at the start and the end
# Status: Done
def getUserInput_String(str, posY):
    str = str + ": "
    errorStr = "Dê-me pelo menos um caracter!"

    print(term.move_xy(0, borderY + posY) + term.black + term.clear_eol)
    print(term.move_xy(0, borderY + posY + 1) + term.black + term.clear_eol)

    posX = ((term.width // 2) - (len(str) // 2))

    while True:
        print(len(str))
        userInput = input(term.move_xy(posX, borderY + posY + 1) + term.lightcyan + str)
        userInput = userInput.strip()  # Remove all spaces at start and end

        if userInput == "":
            print(term.center(term.move_y(borderY + posY) + term.tomato + errorStr))
            print(term.center(term.move_y(borderY + posY + 1) + term.move_right + term.black + term.clear_eol))
        else:
            break
    print(term.move_xy(0, borderY + posY) + term.black + term.clear_eol)
    return userInput


# ==== Clear the Screen ====
# This funtion clears the screen keeping only some info
# At the screen borders
# Recieves the menu name to print
# Status: Done
def clearScreen(menuName, username="None"):
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Footer text
    strToPrint = menuName
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)

    if username != "None":
        strToPrint = "Bem-vindo, " + username + "."
        print(term.move_xy(borderX, borderY + 2) + term.lightcyan + strToPrint)

# ==== Clear lines ====
# This funtion clears a range of lines
# Status: Done
def clearLines(start, end):
    for i in range(start, end):
        print(term.move_xy(0, borderY + i) + term.black + term.clear_eol)


# ==== Reset terminal ====
# This funtion resets the terminal
# Status: Done
def resetTerminal():
    print(term.home + term.on_black + term.clear + term.white)


# ======================================================================================================================
# ============= Main Functions =========================================================================================
# ======================================================================================================================
# ==== First Pages ====

# Status: Done
def firstPage(errorType="None"):
    clearScreen("Página Inicial V1")

    errorStrUserExist = "Já existe um utilizador com esse email, faça login"
    errorStrUserNotExist = "Não existe nenhum utilizador com esse email, crie uma conta"
    errorStrNotAdmin = "Não tem permissões, contate o administrador"
    errorStrWrongPassword = "Palavra passe errada, tente novamente"

    # Main Body
    strToPrint = "Bem-vindo ao NetFLOX"
    print(term.center(term.move_y(borderY + 5) + term.palegreen1 + strToPrint))

    if errorType != "None":
        if errorType == "userAlreadyExist":
            print(term.center(term.move_y(borderY + 6) + term.tomato + errorStrUserExist))
        elif errorType == "userNotExist":
            print(term.center(term.move_y(borderY + 6) + term.tomato + errorStrUserNotExist))
        elif errorType == "userNoPermission":
            print(term.center(term.move_y(borderY + 6) + term.tomato + errorStrNotAdmin))
        elif errorType == "wrongPassword":
            print(term.center(term.move_y(borderY + 6) + term.tomato + errorStrWrongPassword))

    strToPrint = "== Utilizadores =="
    print(term.center(term.move_y(borderY + 7) + term.palegreen1 + strToPrint))

    strToPrint = "[1] -> Fazer login"
    print(term.center(term.move_y(borderY + 8) + term.lightcyan + strToPrint))

    strToPrint = "[2] -> Criar Conta"
    print(term.center(term.move_y(borderY + 9) + term.lightcyan + strToPrint))

    strToPrint = "== Administradores =="
    print(term.center(term.move_y(borderY + 11) + term.palegreen1 + strToPrint))

    strToPrint = "[3] -> Fazer login"
    print(term.center(term.move_y(borderY + 12) + term.lightcyan + strToPrint))

    strToPrint = "== Sair =="
    print(term.center(term.move_y(borderY + 14) + term.palegreen1 + strToPrint))

    strToPrint = "[4] -> Sair do NetFLOX"
    print(term.center(term.move_y(borderY + 15) + term.lightcyan + strToPrint))

    strToPrint = "Escolha uma das opções a cima"
    option = getUserInput_Integer(strToPrint, 18, 4)

    return option


# Status: notDone
def newAccount():
    # Always clear the screen first
    clearScreen("Nova conta user V1")
    # Main Body
    strToPrint = "Criar conta no NetFLOX"
    print(term.center(term.move_y(borderY + 5) + term.palegreen1 + strToPrint))

    strToPrint = "Nome utilizador"
    username = getUserInput_String(strToPrint, 7)

    strToPrint = "Email"
    email = getUserInput_Email(strToPrint, 9)

    strToPrint = "Password"
    password = getUserInput_String(strToPrint, 11)

    print(term.home + term.on_black + term.white + term.clear)

    return username, email, password


def userLogin():
    clearScreen("User Login V1")
    # Main Body
    strToPrint = "Fazer login no NetFLOX"
    print(term.center(term.move_y(borderY + 5) + term.palegreen1 + strToPrint))

    strToPrint = "Email"
    email = getUserInput_Email(strToPrint, 7)

    strToPrint = "Password"
    password = getUserInput_String(strToPrint, 9)

    print(term.home + term.on_black + term.white + term.clear)

    return email, password


def adminLogin():
    clearScreen("Admin Login V1")
    # Main Body
    strToPrint = "Fazer login no NetFLOX como Administrador"
    print(term.center(term.move_y(borderY + 5) + term.palegreen1 + strToPrint))

    strToPrint = "Email"
    email = getUserInput_Email(strToPrint, 7)

    strToPrint = "Password"
    password = getUserInput_String(strToPrint, 9)

    print(term.home + term.on_black + term.white + term.clear)

    return email, password


# ==== User Menus ====

# ==== User Main Menu ====
# This funtion has the main options the user needs
# recieves the username, balance and unread messages
# Status: Done
def mainMenuUser(username, balance, unreadMessages):
    clearScreen("Menu Inicial User V1", username=username)

    # Main Body
    # User info
    strToPrint = "Saldo disponível: " + str(balance / 100) + "€"
    print(term.move_xy(borderX, borderY + 3) + term.lightcyan + strToPrint)

    # Menus
    strToPrint = "Escolha a opção pretendida"
    print(term.center(term.move_y(borderY + 6) + term.palegreen1 + strToPrint))

    strToPrint = "[1] -> Ver artigos"
    print(term.move_xy((term.width // 2) - 15, borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "[2] -> Artigos alugados"
    print(term.move_xy((term.width // 2) - 15, borderY + 10) + term.lightcyan + strToPrint)

    strToPrint = "[3] -> Histórico e Estatísticas"
    print(term.move_xy((term.width // 2) - 15, borderY + 11) + term.lightcyan + strToPrint)

    strToPrint = "[4] -> Caixa de Entrada (" + str(unreadMessages) + ")"
    print(term.move_xy((term.width // 2) - 15, borderY + 12) + term.lightcyan + strToPrint)

    strToPrint = "[5] -> Logout"
    print(term.move_xy((term.width // 2) - 15, borderY + 14) + term.lightcyan + strToPrint)

    strToPrint = "Escolha uma das opções a cima"
    option = getUserInput_Integer(strToPrint, 17, 5)

    return option


# ==== Ver artigos ====
# This funtion shows the movies to the user
# Status: Done
def verArtigosUser(username):
    # Always clear the screen first
    clearScreen("Artigos User V3", username=username)
    # Main Body

    strToPrint = "Escolha a opção pretendida"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

    strToPrint = "[1] -> Ver artigos disponíveis"
    print(term.move_xy((term.width // 2) - 15, borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "[2] -> Pesquisar Artigo"
    print(term.move_xy((term.width // 2) - 15, borderY + 10) + term.lightcyan + strToPrint)

    strToPrint = "[3] -> Menu Principal"
    print(term.move_xy((term.width // 2) - 15, borderY + 12) + term.lightcyan + strToPrint)

    strToPrint = "Escolha uma das opções a cima"

    option = getUserInput_Integer(strToPrint, 17, 3)

    return option


# ==== Listar artigos ====
# This funtion lists all the items available
# Recieves a database cursor a database conection and the user id idUser
# Status: Done
def listarArtigosUser(cursor, dbCon, idUser):
    # Always clear the screen first
    command = "SELECT pessoa_nome FROM cliente WHERE pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser,))
    username, = cursor.fetchone()
    clearScreen("Listar Artigos User V1", username=username)
    # Main Body

    command = "SELECT titulo, tipo, preco, id_art FROM artigos"
    cursor.execute(command)
    data = cursor.fetchall()  # [0]>titulo, [1]>tipo, [2]>preco, [3]>id_art
    resultAmount = cursor.rowcount

    strToPrint = "Temos " + str(resultAmount) + " artigos disponíveis para alugar"
    print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

    limit = 5
    linha = 0
    show = True

    if (resultAmount > 0):
        for i in range(resultAmount):
            if show:
                strToPrint = "[" + str(i + 1) + "] -> " + str(data[i][1]) + ": " + str(data[i][0])
                print(term.move_xy((term.width // 2) - 30, borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                strToPrint = "Preço: {:.2f}€".format(int(data[i][2]) / 100)
                print(term.move_xy(term.width - (borderX + 24), borderY + 8 + linha) + term.lightcyan + strToPrint)
                linha += 1

                if (linha >= limit) and (i != (resultAmount - 1)):
                    strToPrint = "Quer mais? (Sim/Não)"
                    out = getUserInput_String(strToPrint, 16)
                    out = out.lower()
                    if out == "sim" or out == "s":
                        clearLines(8, 8 + linha)
                        linha = 0
                    else:
                        show = False
        strToPrint = "Escolha o artigo (Sair -> 0)"
        artigo = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

        if artigo != 0:
            idArtigo = data[artigo - 1][3]

            mostrarArtigo(cursor, dbCon, idArtigo, idUser)

    else:  # Nothing to show just get out
        strToPrint = "Não há artigos disponíveis."
        print(term.center(term.move_y(borderY + 6) + term.tomato + strToPrint))
        strToPrint = "Escreva algo para sair"
        getUserInput_String(strToPrint, 16)

    return


# ==== Pesquisa de artigos ====
# This funtion allows the user to make a custom search
# Recieves a database cursor a database conection and the user id idUser
# Status: Done
def pesquisarArtigosUser(cursor, dbCon, idUser):
    # Always clear the screen first
    command = "SELECT pessoa_nome FROM cliente WHERE pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser,))
    username, = cursor.fetchone()
    clearScreen("Pesquisa de Artigos User V1", username=username)
    # Main Body

    strToPrint = "Escolha a forma de pesquisa pretendida"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

    strToPrint = "[1] -> Título"
    print(term.move_xy((term.width // 2) - 15, borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "[2] -> Ator"
    print(term.move_xy((term.width // 2) - 15, borderY + 10) + term.lightcyan + strToPrint)

    strToPrint = "[3] -> Realizador"
    print(term.move_xy((term.width // 2) - 15, borderY + 11) + term.lightcyan + strToPrint)

    strToPrint = "[4] -> Produtor"
    print(term.move_xy((term.width // 2) - 15, borderY + 12) + term.lightcyan + strToPrint)

    strToPrint = "[5] -> Menu Anterior"
    print(term.move_xy((term.width // 2) - 15, borderY + 14) + term.lightcyan + strToPrint)

    strToPrint = "Escolha uma das opções a cima"
    option = getUserInput_Integer(strToPrint, 17, 5)

    if option == 1:
        searchType = "Título"
        clearScreen("Pesquisa de Artigos User V1")

        strToPrint = "Pesquisa por " + searchType
        print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

        strToPrint = "Termo de Pesquisa"
        searchTerm = getUserInput_String(strToPrint, 8)

        strToPrint = "Quer ordenar? (Sim/Não)"
        out = getUserInput_String(strToPrint, 16)
        out = out.lower()

        if out == "sim" or out == "s":
            strToPrint = "Dê-me a ordem desejada (ASC/DESC)"
            out = getUserInput_String(strToPrint, 16)
            out = out.lower()
            if out == "desc" or out == "d":
                ordem = "ASC"
            else:
                ordem = "DESC"
        else:  # order anyway but don't tell the user
            ordem = "ASC"

        clearScreen("Pesquisa de Artigos User Titulo V1")

        # ILIKE online works in Postgres but is case insensitive
        command = "SELECT titulo, tipo, preco, id_art FROM artigos WHERE titulo ILIKE %s " \
                  "ORDER BY titulo {order}".format(order=ordem)  # Order is code defined, no way to alter it so

        searchTermAll = "%" + searchTerm + "%"  # Find all with search term

        cursor.execute(command, (searchTermAll,))
        data = cursor.fetchall()  # [0]>titulo, [1]>tipo, [2]>preco, [3]>id_art
        resultAmount = cursor.rowcount

        strToPrint = "Pesquisa por [ " + searchTerm + " ] deu " + str(resultAmount) + " resultados"
        print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

        limit = 5
        linha = 0
        show = True

        if (resultAmount > 0):
            for i in range(resultAmount):
                if show:
                    strToPrint = "[" + str(i + 1) + "] -> " + str(data[i][1]) + ": " + str(data[i][0])
                    print(term.move_xy((term.width // 2) - 30, borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                    strToPrint = "Preço: {:.2f}€".format(int(data[i][2]) / 100)
                    print(term.move_xy(term.width - (borderX + 24), borderY + 8 + linha) + term.lightcyan + strToPrint)
                    linha += 1

                    if (linha >= limit) and (i != (resultAmount - 1)):
                        strToPrint = "Quer mais? (Sim/Não)"
                        out = getUserInput_String(strToPrint, 16)
                        out = out.lower()
                        if out == "sim" or out == "s":
                            clearLines(8, 8 + linha)
                            linha = 0
                        else:
                            show = False
            strToPrint = "Escolha o artigo (Sair -> 0)"
            artigo = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

            if artigo != 0:
                idArtigo = data[artigo - 1][3]

                mostrarArtigo(cursor, dbCon, idArtigo, idUser)

        else:  # Nothing to show just get out
            strToPrint = "Pesquisa por [ " + searchTerm + " ] não teve resultados."
            print(term.center(term.move_y(borderY + 6) + term.tomato + strToPrint))
            strToPrint = "Escreva algo para sair"
            getUserInput_String(strToPrint, 16)

    elif option == 2:
        searchType = "Atores"
        clearScreen("Pesquisa de Artigos User V1")

        strToPrint = "Pesquisa por " + searchType
        print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

        strToPrint = "Termo de Pesquisa"
        searchTerm = getUserInput_String(strToPrint, 8)

        clearScreen("Pesquisa de Artigos User Atores V1")

        strToPrint = "Quer ordenar? (Sim/Não)"
        out = getUserInput_String(strToPrint, 16)
        out = out.lower()

        if out == "sim" or out == "s":
            strToPrint = "Dê-me a ordem desejada (ASC/DESC)"
            out = getUserInput_String(strToPrint, 16)
            out = out.lower()
            if out == "desc" or out == "d":
                ordem = "ASC"
            else:
                ordem = "DESC"
        else:  # order anyway but don't tell the user
            ordem = "ASC"

        # ILIKE online works in Postgres but is case insensitive
        command = "SELECT id_ator, primeiro_nome, segundo_nome FROM atores WHERE primeiro_nome ILIKE %s" \
                  "OR segundo_nome ILIKE %s" \
                  "ORDER BY primeiro_nome {order}".format(order=ordem)

        searchTermAll = "%" + searchTerm + "%"  # Find all with search term

        cursor.execute(command, (searchTermAll, searchTermAll))
        data = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome
        resultAmount = cursor.rowcount

        strToPrint = "Pesquisa por [ " + searchTerm + " ] deu " + str(resultAmount) + " resultados"
        print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

        limit = 5
        linha = 0
        show = True

        if (resultAmount > 0):
            for i in range(resultAmount):
                if show:
                    strToPrint = "[" + str(i + 1) + "] -> " + str(data[i][1]) + " " + str(data[i][2])
                    print(term.move_xy((term.width // 2) - 25, borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                    linha += 1

                    if (linha >= limit) and (i != (resultAmount - 1)):
                        strToPrint = "Quer mais? (Sim/Não)"
                        out = getUserInput_String(strToPrint, 16)
                        out = out.lower()
                        if out == "sim" or out == "s":
                            clearLines(8, 8 + linha)
                            linha = 0
                        else:
                            show = False
            strToPrint = "Escolha o ator (Sair -> 0)"
            ator = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

            clearLines(8, 13)

            if ator != 0:
                idAtor = data[ator - 1][0]

                print(idAtor)

                # Retirar artigos onde o ator participa
                command = "SELECT DISTINCT id_art, tipo, titulo, preco FROM artigos art, artigos_atores aa, atores act " \
                          "WHERE art.id_art = aa.artigos_id_art AND aa.atores_id_ator = act.id_ator " \
                          "AND act.id_ator = %s"

                cursor.execute(command, (idAtor,))
                atorFilmes = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome, [3]>preco

                resultAmount = cursor.rowcount

                linha = 0
                show = True

                if (resultAmount > 0):
                    for i in range(resultAmount):
                        if show:
                            strToPrint = "[" + str(i + 1) + "] -> " + str(atorFilmes[i][1]) + " " + str(
                                atorFilmes[i][2])
                            print(term.move_xy((term.width // 2) - 25,
                                               borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                            strToPrint = "Preço: {:.2f}€".format(int(atorFilmes[i][3]) / 100)
                            print(term.move_xy(term.width - (borderX + 24),
                                               borderY + 8 + linha) + term.lightcyan + strToPrint)
                            linha += 1

                            if (linha >= limit) and (i != (resultAmount - 1)):
                                strToPrint = "Quer mais? (Sim/Não)"
                                out = getUserInput_String(strToPrint, 16)
                                out = out.lower()
                                if out == "sim" or out == "s":
                                    clearLines(8, 8 + linha)
                                    linha = 0
                                else:
                                    show = False
                    strToPrint = "Escolha o filme (Sair -> 0)"
                    artigo = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

                idArtigo = atorFilmes[artigo - 1][0]

                mostrarArtigo(cursor, dbCon, idArtigo, idUser)

        else:  # Nothing to show just get out
            strToPrint = "Pesquisa por [ " + searchTerm + " ] não teve resultados."
            print(term.center(term.move_y(borderY + 6) + term.tomato + strToPrint))
            strToPrint = "Escreva algo para sair"
            getUserInput_String(strToPrint, 16)

    elif option == 3:
        searchType = "Realizador"
        clearScreen("Pesquisa de Artigos User V1")

        strToPrint = "Pesquisa por " + searchType
        print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

        strToPrint = "Termo de Pesquisa"
        searchTerm = getUserInput_String(strToPrint, 8)

        clearScreen("Pesquisa de Artigos User Realizador V1")

        strToPrint = "Quer ordenar? (Sim/Não)"
        out = getUserInput_String(strToPrint, 16)
        out = out.lower()

        if out == "sim" or out == "s":
            strToPrint = "Dê-me a ordem desejada (ASC/DESC)"
            out = getUserInput_String(strToPrint, 16)
            out = out.lower()
            if out == "desc" or out == "d":
                ordem = "ASC"
            else:
                ordem = "DESC"
        else:  # order anyway but don't tell the user
            ordem = "ASC"

        # ILIKE online works in Postgres but is case insensitive
        command = "SELECT id_produtor, primeiro_nome, segundo_nome FROM produtor WHERE primeiro_nome ILIKE %s" \
                  "OR segundo_nome ILIKE %s" \
                  "ORDER BY primeiro_nome {order}".format(order=ordem)  # Order is code defined, no way to alter it so

        searchTermAll = "%" + searchTerm + "%"  # Find all with search term

        cursor.execute(command, (searchTermAll, searchTermAll))
        data = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome
        resultAmount = cursor.rowcount

        strToPrint = "Pesquisa por [ " + searchTerm + " ] deu " + str(resultAmount) + " resultados"
        print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

        limit = 5
        linha = 0
        show = True

        if (resultAmount > 0):
            for i in range(resultAmount):
                if show:
                    strToPrint = "[" + str(i + 1) + "] -> " + str(data[i][1]) + " " + str(data[i][2])
                    print(term.move_xy((term.width // 2) - 25, borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                    linha += 1

                    if (linha >= limit) and (i != (resultAmount - 1)):
                        strToPrint = "Quer mais? (Sim/Não)"
                        out = getUserInput_String(strToPrint, 16)
                        out = out.lower()
                        if out == "sim" or out == "s":
                            clearLines(8, 8 + linha)
                            linha = 0
                        else:
                            show = False
            strToPrint = "Escolha o realizador (Sair -> 0)"
            Realizador = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

            clearLines(8, 13)

            if Realizador != 0:
                idRealizador = data[Realizador - 1][0]

                # Retirar artigos onde o ator participa
                command = "SELECT DISTINCT id_art, tipo, titulo, preco FROM artigos a, artigos_realizador ar, realizador r " \
                          "WHERE a.id_art = ar.artigos_id_art AND ar.realizador_id_realizador = r.id_realizador " \
                          "AND r.id_realizador = '%s'"

                cursor.execute(command, (idRealizador,))
                atorRealizador = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome, [3]>preco

                resultAmount = cursor.rowcount

                linha = 0
                show = True

                if (resultAmount > 0):
                    for i in range(resultAmount):
                        if show:
                            strToPrint = "[" + str(i + 1) + "] -> " + str(atorRealizador[i][1]) + ": " + str(
                                atorRealizador[i][2])
                            print(term.move_xy((term.width // 2) - 25,
                                               borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                            strToPrint = "Preço: {:.2f}€".format(int(atorRealizador[i][3]) / 100)
                            print(term.move_xy(term.width - (borderX + 24),
                                               borderY + 8 + linha) + term.lightcyan + strToPrint)
                            linha += 1

                            if (linha >= limit) and (i != (resultAmount - 1)):
                                strToPrint = "Quer mais? (Sim/Não)"
                                out = getUserInput_String(strToPrint, 16)
                                out = out.lower()
                                if out == "sim" or out == "s":
                                    clearLines(8, 8 + linha)
                                    linha = 0
                                else:
                                    show = False
                    strToPrint = "Escolha o filme (Sair -> 0)"
                    artigo = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

                idArtigo = atorRealizador[artigo - 1][0]

                mostrarArtigo(cursor, dbCon, idArtigo, idUser)

        else:  # Nothing to show just get out
            strToPrint = "Pesquisa por [ " + searchTerm + " ] não teve resultados."
            print(term.center(term.move_y(borderY + 6) + term.tomato + strToPrint))
            strToPrint = "Escreva algo para sair"
            getUserInput_String(strToPrint, 16)

    elif option == 4:
        searchType = "Produtor"
        clearScreen("Pesquisa de Artigos User V1")

        strToPrint = "Pesquisa por " + searchType
        print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

        strToPrint = "Termo de Pesquisa"
        searchTerm = getUserInput_String(strToPrint, 8)

        clearScreen("Pesquisa de Artigos User Produtor V1")

        strToPrint = "Quer ordenar? (Sim/Não)"
        out = getUserInput_String(strToPrint, 16)
        out = out.lower()

        if out == "sim" or out == "s":
            strToPrint = "Dê-me a ordem desejada (ASC/DESC)"
            out = getUserInput_String(strToPrint, 16)
            out = out.lower()
            if out == "desc" or out == "d":
                ordem = "ASC"
            else:
                ordem = "DESC"
        else:  # order anyway but don't tell the user
            ordem = "ASC"

        # ILIKE online works in Postgres but is case insensitive
        command = "SELECT id_produtor, primeiro_nome, segundo_nome FROM produtor WHERE primeiro_nome ILIKE %s" \
                  "OR segundo_nome ILIKE %s" \
                  "ORDER BY primeiro_nome {order}".format(order=ordem)  # Order is code defined, no way to alter it so

        searchTermAll = "%" + searchTerm + "%"  # Find all with search term

        cursor.execute(command, (searchTermAll, searchTermAll))
        data = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome
        resultAmount = cursor.rowcount

        strToPrint = "Pesquisa por [ " + searchTerm + " ] deu " + str(resultAmount) + " resultados"
        print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

        limit = 5
        linha = 0
        show = True

        if (resultAmount > 0):
            for i in range(resultAmount):
                if show:
                    strToPrint = "[" + str(i + 1) + "] -> " + str(data[i][1]) + " " + str(data[i][2])
                    print(term.move_xy((term.width // 2) - 25, borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                    linha += 1

                    if (linha >= limit) and (i != (resultAmount - 1)):
                        strToPrint = "Quer mais? (Sim/Não)"
                        out = getUserInput_String(strToPrint, 16)
                        out = out.lower()
                        if out == "sim" or out == "s":
                            clearLines(8, 8 + linha)
                            linha = 0
                        else:
                            show = False
            strToPrint = "Escolha o produtor (Sair -> 0)"
            produtor = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

            clearLines(8, 13)

            if produtor != 0:
                idProdutor = data[produtor - 1][0]

                # Retirar artigos onde o ator participa
                command = "SELECT DISTINCT id_art, tipo, titulo, preco FROM artigos a, artigos_produtor ap, produtor p " \
                          "WHERE a.id_art = ap.artigos_id_art AND ap.produtor_id_produtor = p.id_produtor " \
                          "AND p.id_produtor = '%s'"

                cursor.execute(command, (idProdutor,))
                atorProdutor = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome, [3]>preco

                resultAmount = cursor.rowcount

                linha = 0
                show = True

                if (resultAmount > 0):
                    for i in range(resultAmount):
                        if show:
                            strToPrint = "[" + str(i + 1) + "] -> " + str(atorProdutor[i][1]) + " " + str(
                                atorProdutor[i][2])
                            print(term.move_xy((term.width // 2) - 25,
                                               borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                            strToPrint = "Preço: {:.2f}€".format(int(atorProdutor[i][3]) / 100)
                            print(term.move_xy(term.width - (borderX + 24),
                                               borderY + 8 + linha) + term.lightcyan + strToPrint)
                            linha += 1

                            if (linha >= limit) and (i != (resultAmount - 1)):
                                strToPrint = "Quer mais? (Sim/Não)"
                                out = getUserInput_String(strToPrint, 16)
                                out = out.lower()
                                if out == "sim" or out == "s":
                                    clearLines(8, 8 + linha)
                                    linha = 0
                                else:
                                    show = False
                    strToPrint = "Escolha o filme (Sair -> 0)"
                    artigo = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

                idArtigo = atorProdutor[artigo - 1][0]

                mostrarArtigo(cursor, dbCon, idArtigo, idUser)

        else:  # Nothing to show just get out
            strToPrint = "Pesquisa por [ " + searchTerm + " ] não teve resultados."
            print(term.center(term.move_y(borderY + 6) + term.tomato + strToPrint))
            strToPrint = "Escreva algo para sair"
            getUserInput_String(strToPrint, 16)

    elif option == 5:
        return 5


# ==== Listar artigos alugados ====
# This funtion lists all the rented items available
# Recieves a database cursor a database conection and the user id idUser
# Status: Done
def listarArtigosAlugadosUser(cursor, dbCon, idUser):
    # Always clear the screen first
    command = "SELECT pessoa_nome FROM cliente WHERE pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser,))
    username, = cursor.fetchone()
    clearScreen("Listar Artigos Alugados User V1", username=username)
    # Main Body

    nowTime = datetime.datetime.now()
    nowTimestamp = int(nowTime.timestamp())

    # Check if user already own's it
    command = "SELECT artigos_id_art FROM aluguer WHERE cliente_pessoa_id_pessoa = %s " \
              "AND data_validade > %s " \
              "AND cliente_pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser, nowTimestamp, idUser))
    IDartigos = cursor.fetchall()  # [0]>artigos_id_art
    resultAmount = cursor.rowcount

    strToPrint = "Tem " + str(resultAmount) + " artigos disponíveis para visualização"
    print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

    limit = 5
    linha = 0
    show = True

    if (resultAmount > 0):
        for i in range(resultAmount):
            if show:
                command = "SELECT titulo, tipo, id_art FROM artigos WHERE id_art = %s"
                cursor.execute(command, (IDartigos[i],))
                data = cursor.fetchone()

                strToPrint = "[" + str(i + 1) + "] -> " + str(data[1]) + ": " + str(data[0])
                print(term.move_xy((term.width // 2) - 30, borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                linha += 1

                if (linha >= limit) and (i != (resultAmount - 1)):
                    strToPrint = "Quer mais? (Sim/Não)"
                    out = getUserInput_String(strToPrint, 16)
                    out = out.lower()
                    if out == "sim" or out == "s":
                        clearLines(8, 8 + linha)
                        linha = 0
                    else:
                        show = False

        strToPrint = "Escolha o artigo (Sair -> 0)"
        artigo = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

        if artigo != 0:
            idArtigo = IDartigos[artigo - 1][0]

            mostrarArtigo(cursor, dbCon, idArtigo, idUser)

    else:  # Nothing to show just get out
        strToPrint = "Não há artigos disponíveis, alugue um na nossa loja!"
        print(term.center(term.move_y(borderY + 6) + term.tomato + strToPrint))
        strToPrint = "Escreva algo para sair"
        getUserInput_String(strToPrint, 16)

    return


# ==== Pesquisa de artigos alugados ====
# This funtion allows the user to make a custom search
# Recieves a database cursor a database conection and the user id idUser
# Status: Not Done
def pesquisarArtigosAlugadosUser(cursor, dbCon, idUser):
    # Always clear the screen first
    command = "SELECT pessoa_nome FROM cliente WHERE pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser,))
    username, = cursor.fetchone()
    clearScreen("Pesquisa de Artigos User V1", username=username)
    # Main Body

    strToPrint = "Escolha a forma de pesquisa pretendida"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

    strToPrint = "[1] -> Título"
    print(term.move_xy((term.width // 2) - 15, borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "[2] -> Ator"
    print(term.move_xy((term.width // 2) - 15, borderY + 10) + term.lightcyan + strToPrint)

    strToPrint = "[3] -> Realizador"
    print(term.move_xy((term.width // 2) - 15, borderY + 11) + term.lightcyan + strToPrint)

    strToPrint = "[4] -> Produtor"
    print(term.move_xy((term.width // 2) - 15, borderY + 12) + term.lightcyan + strToPrint)

    strToPrint = "[5] -> Menu Anterior"
    print(term.move_xy((term.width // 2) - 15, borderY + 14) + term.lightcyan + strToPrint)

    strToPrint = "Escolha uma das opções a cima"
    option = getUserInput_Integer(strToPrint, 17, 5)

    if option == 1:
        searchType = "Título"
        clearScreen("Pesquisa de Artigos User V1")

        strToPrint = "Pesquisa por " + searchType
        print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

        strToPrint = "Termo de Pesquisa"
        searchTerm = getUserInput_String(strToPrint, 8)

        strToPrint = "Quer ordenar? (Sim/Não)"
        out = getUserInput_String(strToPrint, 16)
        out = out.lower()

        if out == "sim" or out == "s":
            strToPrint = "Dê-me a ordem desejada (ASC/DESC)"
            out = getUserInput_String(strToPrint, 16)
            out = out.lower()
            if out == "desc" or out == "d":
                ordem = "ASC"
            else:
                ordem = "DESC"
        else:  # order anyway but don't tell the user
            ordem = "ASC"

        clearScreen("Pesquisa de Artigos User Titulo V1")

        # ILIKE online works in Postgres but is case insensitive
        command = "SELECT titulo, tipo, preco, id_art FROM artigos WHERE titulo ILIKE %s " \
                  "ORDER BY titulo {order}".format(order=ordem)  # Order is code defined, no way to alter it so

        searchTermAll = "%" + searchTerm + "%"  # Find all with search term

        cursor.execute(command, (searchTermAll,))
        data = cursor.fetchall()  # [0]>titulo, [1]>tipo, [2]>preco, [3]>id_art
        resultAmount = cursor.rowcount

        strToPrint = "Pesquisa por [ " + searchTerm + " ] deu " + str(resultAmount) + " resultados"
        print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

        limit = 5
        linha = 0
        show = True

        if(resultAmount > 0):
            for i in range(resultAmount):
                if show:
                    strToPrint = "[" + str(i + 1) + "] -> " + str(data[i][1]) + ": " + str(data[i][0])
                    print(term.move_xy((term.width // 2) - 30, borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                    strToPrint = "Preço: {:.2f}€".format(int(data[i][2]) / 100)
                    print(term.move_xy(term.width - (borderX + 24), borderY + 8 + linha) + term.lightcyan + strToPrint)
                    linha += 1

                    if (linha >= limit) and (i != (resultAmount - 1)):
                        strToPrint = "Quer mais? (Sim/Não)"
                        out = getUserInput_String(strToPrint, 16)
                        out = out.lower()
                        if out == "sim" or out == "s":
                            clearLines(8, 8 + linha)
                            linha = 0
                        else:
                            show = False
            strToPrint = "Escolha o artigo (Sair -> 0)"
            artigo = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

            if artigo != 0:
                idArtigo = data[artigo - 1][3]

                mostrarArtigo(cursor, dbCon, idArtigo, idUser)

        else:  # Nothing to show just get out
            strToPrint = "Pesquisa por [ " + searchTerm + " ] não teve resultados."
            print(term.center(term.move_y(borderY + 6) + term.tomato + strToPrint))
            strToPrint = "Escreva algo para sair"
            getUserInput_String(strToPrint, 16)

    elif option == 2:
        searchType = "Atores"
        clearScreen("Pesquisa de Artigos User V1")

        strToPrint = "Pesquisa por " + searchType
        print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

        strToPrint = "Termo de Pesquisa"
        searchTerm = getUserInput_String(strToPrint, 8)

        clearScreen("Pesquisa de Artigos User Atores V1")

        strToPrint = "Quer ordenar? (Sim/Não)"
        out = getUserInput_String(strToPrint, 16)
        out = out.lower()

        if out == "sim" or out == "s":
            strToPrint = "Dê-me a ordem desejada (ASC/DESC)"
            out = getUserInput_String(strToPrint, 16)
            out = out.lower()
            if out == "desc" or out == "d":
                ordem = "ASC"
            else:
                ordem = "DESC"
        else:  # order anyway but don't tell the user
            ordem = "ASC"

        # ILIKE online works in Postgres but is case insensitive
        command = "SELECT id_ator, primeiro_nome, segundo_nome FROM atores WHERE primeiro_nome ILIKE %s" \
                  "OR segundo_nome ILIKE %s" \
                  "ORDER BY primeiro_nome {order}".format(order=ordem)

        searchTermAll = "%" + searchTerm + "%"  # Find all with search term

        cursor.execute(command, (searchTermAll, searchTermAll))
        data = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome
        resultAmount = cursor.rowcount

        strToPrint = "Pesquisa por [ " + searchTerm + " ] deu " + str(resultAmount) + " resultados"
        print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

        limit = 5
        linha = 0
        show = True

        if (resultAmount > 0):
            for i in range(resultAmount):
                if show:
                    strToPrint = "[" + str(i + 1) + "] -> " + str(data[i][1]) + " " + str(data[i][2])
                    print(term.move_xy((term.width // 2) - 25, borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                    linha += 1

                    if (linha >= limit) and (i != (resultAmount - 1)):
                        strToPrint = "Quer mais? (Sim/Não)"
                        out = getUserInput_String(strToPrint, 16)
                        out = out.lower()
                        if out == "sim" or out == "s":
                            clearLines(8, 8 + linha)
                            linha = 0
                        else:
                            show = False
            strToPrint = "Escolha o ator (Sair -> 0)"
            ator = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

            clearLines(8, 13)

            if ator != 0:
                idAtor = data[ator - 1][0]

                print(idAtor)

                # Retirar artigos onde o ator participa
                command = "SELECT DISTINCT id_art, tipo, titulo, preco FROM artigos art, artigos_atores aa, atores act " \
                          "WHERE art.id_art = aa.artigos_id_art AND aa.atores_id_ator = act.id_ator " \
                          "AND act.id_ator = %s"

                cursor.execute(command, (idAtor,))
                atorFilmes = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome, [3]>preco

                resultAmount = cursor.rowcount

                linha = 0
                show = True

                if (resultAmount > 0):
                    for i in range(resultAmount):
                        if show:
                            strToPrint = "[" + str(i + 1) + "] -> " + str(atorFilmes[i][1]) + " " + str(
                                atorFilmes[i][2])
                            print(term.move_xy((term.width // 2) - 25,
                                               borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                            strToPrint = "Preço: {:.2f}€".format(int(atorFilmes[i][3]) / 100)
                            print(term.move_xy(term.width - (borderX + 24),
                                               borderY + 8 + linha) + term.lightcyan + strToPrint)
                            linha += 1

                            if (linha >= limit) and (i != (resultAmount - 1)):
                                strToPrint = "Quer mais? (Sim/Não)"
                                out = getUserInput_String(strToPrint, 16)
                                out = out.lower()
                                if out == "sim" or out == "s":
                                    clearLines(8, 8 + linha)
                                    linha = 0
                                else:
                                    show = False
                    strToPrint = "Escolha o filme (Sair -> 0)"
                    artigo = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

                idArtigo = atorFilmes[artigo - 1][0]

                mostrarArtigo(cursor, dbCon, idArtigo, idUser)

        else:  # Nothing to show just get out
            strToPrint = "Pesquisa por [ " + searchTerm + " ] não teve resultados."
            print(term.center(term.move_y(borderY + 6) + term.tomato + strToPrint))
            strToPrint = "Escreva algo para sair"
            getUserInput_String(strToPrint, 16)

    elif option == 3:
        searchType = "Realizador"
        clearScreen("Pesquisa de Artigos User V1")

        strToPrint = "Pesquisa por " + searchType
        print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

        strToPrint = "Termo de Pesquisa"
        searchTerm = getUserInput_String(strToPrint, 8)

        clearScreen("Pesquisa de Artigos User Realizador V1")

        strToPrint = "Quer ordenar? (Sim/Não)"
        out = getUserInput_String(strToPrint, 16)
        out = out.lower()

        if out == "sim" or out == "s":
            strToPrint = "Dê-me a ordem desejada (ASC/DESC)"
            out = getUserInput_String(strToPrint, 16)
            out = out.lower()
            if out == "desc" or out == "d":
                ordem = "ASC"
            else:
                ordem = "DESC"
        else:  # order anyway but don't tell the user
            ordem = "ASC"

        # ILIKE online works in Postgres but is case insensitive
        command = "SELECT id_produtor, primeiro_nome, segundo_nome FROM produtor WHERE primeiro_nome ILIKE %s" \
                  "OR segundo_nome ILIKE %s" \
                  "ORDER BY primeiro_nome {order}".format(order=ordem)  # Order is code defined, no way to alter it so

        searchTermAll = "%" + searchTerm + "%"  # Find all with search term

        cursor.execute(command, (searchTermAll, searchTermAll))
        data = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome
        resultAmount = cursor.rowcount

        strToPrint = "Pesquisa por [ " + searchTerm + " ] deu " + str(resultAmount) + " resultados"
        print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

        limit = 5
        linha = 0
        show = True

        if (resultAmount > 0):
            for i in range(resultAmount):
                if show:
                    strToPrint = "[" + str(i + 1) + "] -> " + str(data[i][1]) + " " + str(data[i][2])
                    print(term.move_xy((term.width // 2) - 25, borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                    linha += 1

                    if (linha >= limit) and (i != (resultAmount - 1)):
                        strToPrint = "Quer mais? (Sim/Não)"
                        out = getUserInput_String(strToPrint, 16)
                        out = out.lower()
                        if out == "sim" or out == "s":
                            clearLines(8, 8 + linha)
                            linha = 0
                        else:
                            show = False
            strToPrint = "Escolha o realizador (Sair -> 0)"
            Realizador = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

            clearLines(8, 13)

            if Realizador != 0:
                idRealizador = data[Realizador - 1][0]

                # Retirar artigos onde o ator participa
                command = "SELECT DISTINCT id_art, tipo, titulo, preco FROM artigos a, artigos_realizador ar, realizador r " \
                          "WHERE a.id_art = ar.artigos_id_art AND ar.realizador_id_realizador = r.id_realizador " \
                          "AND r.id_realizador = '%s'"

                cursor.execute(command, (idRealizador,))
                atorRealizador = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome, [3]>preco

                resultAmount = cursor.rowcount

                linha = 0
                show = True

                if (resultAmount > 0):
                    for i in range(resultAmount):
                        if show:
                            strToPrint = "[" + str(i + 1) + "] -> " + str(atorRealizador[i][1]) + ": " + str(
                                atorRealizador[i][2])
                            print(term.move_xy((term.width // 2) - 25,
                                               borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                            strToPrint = "Preço: {:.2f}€".format(int(atorRealizador[i][3]) / 100)
                            print(term.move_xy(term.width - (borderX + 24),
                                               borderY + 8 + linha) + term.lightcyan + strToPrint)
                            linha += 1

                            if (linha >= limit) and (i != (resultAmount - 1)):
                                strToPrint = "Quer mais? (Sim/Não)"
                                out = getUserInput_String(strToPrint, 16)
                                out = out.lower()
                                if out == "sim" or out == "s":
                                    clearLines(8, 8 + linha)
                                    linha = 0
                                else:
                                    show = False
                    strToPrint = "Escolha o filme (Sair -> 0)"
                    artigo = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

                idArtigo = atorRealizador[artigo - 1][0]

                mostrarArtigo(cursor, dbCon, idArtigo, idUser)

        else:  # Nothing to show just get out
            strToPrint = "Pesquisa por [ " + searchTerm + " ] não teve resultados."
            print(term.center(term.move_y(borderY + 6) + term.tomato + strToPrint))
            strToPrint = "Escreva algo para sair"
            getUserInput_String(strToPrint, 16)

    elif option == 4:
        searchType = "Produtor"
        clearScreen("Pesquisa de Artigos User V1")

        strToPrint = "Pesquisa por " + searchType
        print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

        strToPrint = "Termo de Pesquisa"
        searchTerm = getUserInput_String(strToPrint, 8)

        clearScreen("Pesquisa de Artigos User Produtor V1")

        strToPrint = "Quer ordenar? (Sim/Não)"
        out = getUserInput_String(strToPrint, 16)
        out = out.lower()

        if out == "sim" or out == "s":
            strToPrint = "Dê-me a ordem desejada (ASC/DESC)"
            out = getUserInput_String(strToPrint, 16)
            out = out.lower()
            if out == "desc" or out == "d":
                ordem = "ASC"
            else:
                ordem = "DESC"
        else:  # order anyway but don't tell the user
            ordem = "ASC"

        # ILIKE online works in Postgres but is case insensitive
        command = "SELECT id_produtor, primeiro_nome, segundo_nome FROM produtor WHERE primeiro_nome ILIKE %s" \
                  "OR segundo_nome ILIKE %s" \
                  "ORDER BY primeiro_nome {order}".format(order=ordem)  # Order is code defined, no way to alter it so

        searchTermAll = "%" + searchTerm + "%"  # Find all with search term

        cursor.execute(command, (searchTermAll, searchTermAll))
        data = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome
        resultAmount = cursor.rowcount

        strToPrint = "Pesquisa por [ " + searchTerm + " ] deu " + str(resultAmount) + " resultados"
        print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

        limit = 5
        linha = 0
        show = True

        if (resultAmount > 0):
            for i in range(resultAmount):
                if show:
                    strToPrint = "[" + str(i + 1) + "] -> " + str(data[i][1]) + " " + str(data[i][2])
                    print(term.move_xy((term.width // 2) - 25, borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                    linha += 1

                    if (linha >= limit) and (i != (resultAmount - 1)):
                        strToPrint = "Quer mais? (Sim/Não)"
                        out = getUserInput_String(strToPrint, 16)
                        out = out.lower()
                        if out == "sim" or out == "s":
                            clearLines(8, 8 + linha)
                            linha = 0
                        else:
                            show = False
            strToPrint = "Escolha o produtor (Sair -> 0)"
            produtor = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

            clearLines(8, 13)

            if produtor != 0:
                idProdutor = data[produtor - 1][0]

                # Retirar artigos onde o ator participa
                command = "SELECT DISTINCT id_art, tipo, titulo, preco FROM artigos a, artigos_produtor ap, produtor p " \
                          "WHERE a.id_art = ap.artigos_id_art AND ap.produtor_id_produtor = p.id_produtor " \
                          "AND p.id_produtor = '%s'"

                cursor.execute(command, (idProdutor,))
                atorProdutor = cursor.fetchall()  # [0]>id_ator, [1]>primeiro_nome, [2]>segundo_nome, [3]>preco

                resultAmount = cursor.rowcount

                linha = 0
                show = True

                if (resultAmount > 0):
                    for i in range(resultAmount):
                        if show:
                            strToPrint = "[" + str(i + 1) + "] -> " + str(atorProdutor[i][1]) + " " + str(
                                atorProdutor[i][2])
                            print(term.move_xy((term.width // 2) - 25,
                                               borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                            strToPrint = "Preço: {:.2f}€".format(int(atorProdutor[i][3]) / 100)
                            print(term.move_xy(term.width - (borderX + 24),
                                               borderY + 8 + linha) + term.lightcyan + strToPrint)
                            linha += 1

                            if (linha >= limit) and (i != (resultAmount - 1)):
                                strToPrint = "Quer mais? (Sim/Não)"
                                out = getUserInput_String(strToPrint, 16)
                                out = out.lower()
                                if out == "sim" or out == "s":
                                    clearLines(8, 8 + linha)
                                    linha = 0
                                else:
                                    show = False
                    strToPrint = "Escolha o filme (Sair -> 0)"
                    artigo = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

                idArtigo = atorProdutor[artigo - 1][0]

                mostrarArtigo(cursor, dbCon, idArtigo, idUser)

        else:  # Nothing to show just get out
            strToPrint = "Pesquisa por [ " + searchTerm + " ] não teve resultados."
            print(term.center(term.move_y(borderY + 6) + term.tomato + strToPrint))
            strToPrint = "Escreva algo para sair"
            getUserInput_String(strToPrint, 16)

    elif option == 5:
        return 5


def verArtigosAlugadosUser(username):
    # Always clear the screen first
    clearScreen("Artigos alugados User V3", username=username)
    # Main Body

    strToPrint = "Escolha a opção pretendida"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

    strToPrint = "[1] -> Ver artigos alugados"
    print(term.move_xy((term.width // 2) - 15, borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "[2] -> Pesquisar Artigo Alugado"
    print(term.move_xy((term.width // 2) - 15, borderY + 10) + term.lightcyan + strToPrint)

    strToPrint = "[3] -> Menu Principal"
    print(term.move_xy((term.width // 2) - 15, borderY + 12) + term.lightcyan + strToPrint)

    strToPrint = "Escolha uma das opções a cima"

    option = getUserInput_Integer(strToPrint, 17, 3)

    return option


# ==== Estatisticas ====
# This funtion shows one movie to the user
# Status: Done
def verHistoricoEstatisticas(username):
    # Always clear the screen first
    clearScreen("Histórico e Estatísticas User V2", username=username)
    # Main Body

    strToPrint = "Escolha a opção pretendida"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

    strToPrint = "[1] -> Ver históricos artigos alugados"
    print(term.move_xy((term.width // 2) - 15, borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "[2] -> Ver estatísticas"
    print(term.move_xy((term.width // 2) - 15, borderY + 10) + term.lightcyan + strToPrint)

    strToPrint = "[3] -> Menu Principal"
    print(term.move_xy((term.width // 2) - 15, borderY + 12) + term.lightcyan + strToPrint)

    strToPrint = "Escolha uma das opções a cima"

    option = getUserInput_Integer(strToPrint, 17, 3)

    return option


# ==== Alugar Artigo ====
# This funtion rents a certain item to the user
# Recieves a database cursor a database conection and the user id and a item id
# Status: Done
def estatisticasUser(cursor, dbCon, idUser):
    command = "SELECT pessoa_nome FROM cliente WHERE pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser,))
    username, = cursor.fetchone()
    clearScreen("Estastísticas User V4", username=username)

    # Total gasto
    command = "SELECT CAST(SUM(preco) AS BIGINT) FROM aluguer WHERE cliente_pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser,))
    stats = cursor.fetchall()  # [0]>SUM(preco)

    if (cursor.rowcount > 0):

        price = "{:.2f}€".format(int(stats[0][0]) / 100)

        strToPrint = "No total já gastou " + str(price)
        print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))
        strToPrint = "Dos quais:"
        print(term.center(term.move_y(borderY + 8) + term.palegreen1 + strToPrint))

    else:  # Nothing to show just get out
        strToPrint = "No total já gastou muito! Muito obrigado! "
        print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

    # Filmes
    command = "SELECT CAST(SUM(aluguer.preco) AS BIGINT) FROM aluguer " \
              "JOIN artigos a on a.id_art = aluguer.artigos_id_art " \
              "WHERE a.tipo = 'Filme'"

    cursor.execute(command)
    stats = cursor.fetchall()  # [0]>SUM(preco), [1]>Tipo

    if (cursor.rowcount > 0):
        price = "{:.2f}€".format(int(stats[0][0]) / 100)
        strToPrint = price + " em filmes"
        print(term.center(term.move_y(borderY + 10) + term.lightcyan + strToPrint))

    # Séries
    command = "SELECT CAST(SUM(aluguer.preco) AS BIGINT) FROM aluguer " \
              "JOIN artigos a on a.id_art = aluguer.artigos_id_art " \
              "WHERE a.tipo = 'Série'"

    cursor.execute(command)
    stats = cursor.fetchall()  # [0]>SUM(preco) , [1]>Tipo

    if (cursor.rowcount > 0):
        price = "{:.2f}€".format(int(stats[0][0]) / 100)
        strToPrint = price + " em séries"
        print(term.center(term.move_y(borderY + 11) + term.lightcyan + strToPrint))

    # Documentários
    command = "SELECT CAST(SUM(aluguer.preco) AS BIGINT) FROM aluguer " \
              "JOIN artigos a on a.id_art = aluguer.artigos_id_art " \
              "WHERE a.tipo = 'Documentário'"

    cursor.execute(command)
    stats = cursor.fetchall()  # [0]>SUM(preco), [1]>Tipo

    if (cursor.rowcount > 0):
        price = "{:.2f}€".format(int(stats[0][0]) / 100)
        strToPrint = price + " em documentários"
        print(term.center(term.move_y(borderY + 12) + term.lightcyan + strToPrint))

    strToPrint = "Escreva algo para sair"
    getUserInput_String(strToPrint, 16)

    return


# ==== Historico ====
# This funtion shows all the items the user rented
# Status: Done
def listarArtigosHistoricoUser(cursor, dbCon, idUser):
    # Always clear the screen first
    command = "SELECT pessoa_nome FROM cliente WHERE pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser,))
    username, = cursor.fetchone()
    clearScreen("Listar Historico Alugados User V1", username=username)
    # Main Body

    nowTime = datetime.datetime.now()
    nowTimestamp = int(nowTime.timestamp())

    # Check if user already own's it
    command = "SELECT artigos_id_art FROM aluguer WHERE cliente_pessoa_id_pessoa = %s " \
              "AND data_validade <= %s " \
              "AND cliente_pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser, nowTimestamp, idUser))
    IDartigos = cursor.fetchall()  # [0]>artigos_id_art
    resultAmount = cursor.rowcount

    strToPrint = "Já alugou " + str(resultAmount) + " artigos"
    print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))

    limit = 5
    linha = 0
    show = True

    if (resultAmount > 0):
        for i in range(resultAmount):
            if show:
                command = "SELECT titulo, tipo, id_art FROM artigos WHERE id_art = %s"
                cursor.execute(command, (IDartigos[i],))
                data = cursor.fetchone()

                strToPrint = "[" + str(i + 1) + "] -> " + str(data[1]) + ": " + str(data[0])
                print(term.move_xy((term.width // 2) - 30, borderY + 8 + (linha)) + term.lightcyan + strToPrint)

                linha += 1

                if (linha >= limit) and (i != (resultAmount - 1)):
                    strToPrint = "Quer mais? (Sim/Não)"
                    out = getUserInput_String(strToPrint, 16)
                    out = out.lower()
                    if out == "sim" or out == "s":
                        clearLines(8, 8 + linha)
                        linha = 0
                    else:
                        show = False

        strToPrint = "Escolha o artigo (Sair -> 0)"
        artigo = getUserInput_Integer(strToPrint, 16, resultAmount, 0)

        if artigo != 0:
            idArtigo = IDartigos[artigo - 1][0]

            mostrarArtigo(cursor, dbCon, idArtigo, idUser)

    else:  # Nothing to show just get out
        strToPrint = "Nunca alugou nada na NetFLOX, visite a nossa loja!"
        print(term.center(term.move_y(borderY + 6) + term.tomato + strToPrint))
        strToPrint = "Escreva algo para sair"
        getUserInput_String(strToPrint, 16)

    return

# ==== Mostrar artigo ====
# This funtion shows one movie to the user
# Along with all the movie details
# Also checks if the user already has the item
# Recieves a database cursor a database conection and the user id and a item id
# Status: Done
def mostrarArtigo(cursor, dbCon, id, idUser):
    command = "SELECT pessoa_nome FROM cliente WHERE pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser,))
    username, = cursor.fetchone()
    clearScreen("Mostrar Artigo User V4", username=username)

    command = "SELECT tipo, titulo, preco, tempo_para_ver, detalhes FROM artigos WHERE id_art = %s"
    cursor.execute(command, (id,))
    data = cursor.fetchone()  # [0]>tipo, [1]>titulo, [2]>preco, [3]>tempo_para_ver, [4]>detalhes

    price = "{:.2f}€".format(int(data[2]) / 100)

    # ==== Nome ====
    strToPrint = str(data[0]) + ": "
    offX = len(strToPrint)
    print(term.move_xy((term.width // 2) - 10 - offX, borderY + 5) + term.palegreen1 + strToPrint)
    strToPrint = str(data[1])
    print(term.move_xy((term.width // 2) - 10, borderY + 5) + term.lightcyan + strToPrint)

    # ==== Realizador/Produtor ====

    command = "SELECT primeiro_nome, segundo_nome FROM realizador " \
              "JOIN artigos_realizador ar on realizador.id_realizador = ar.realizador_id_realizador " \
              "JOIN artigos a on a.id_art = ar.artigos_id_art WHERE id_art = %s"
    cursor.execute(command, (id,))
    realizador = cursor.fetchall()

    if (cursor.rowcount > 0):
        strToPrint = "Realizado por: "
        varLen = len(strToPrint)
        print(term.move_xy((term.width // 2) - 30, borderY + 8) + term.palegreen1 + strToPrint)
        strToPrint = str(realizador[0][0] + " " + realizador[0][1])
        print(term.move_xy((term.width // 2) - 30 + varLen, borderY + 8) + term.lightcyan + strToPrint)

    command = "SELECT primeiro_nome, segundo_nome FROM produtor " \
              "JOIN artigos_produtor ap on produtor.id_produtor = ap.produtor_id_produtor " \
              "JOIN artigos a on a.id_art = ap.artigos_id_art WHERE id_art = %s"
    cursor.execute(command, (id,))
    produtor = cursor.fetchall()

    if (cursor.rowcount > 0):
        strToPrint = "Produzido por: "
        varLen = len(strToPrint)
        print(term.move_xy((term.width // 2) - 30, borderY + 10) + term.palegreen1 + strToPrint)
        strToPrint = str(produtor[0][0] + " " + produtor[0][1])
        print(term.move_xy((term.width // 2) - 30 + varLen, borderY + 10) + term.lightcyan + strToPrint)

    # ==== Actores ====

    # Example
    # SELECT * FROM tracks JOIN albums ON tracks.album_id = albums.id
    # JOIN artists ON albums.artist_id = artists.id;

    command = "SELECT primeiro_nome, segundo_nome FROM atores " \
              "JOIN artigos_atores aa on atores.id_ator = aa.atores_id_ator " \
              "JOIN artigos a on a.id_art = aa.artigos_id_art WHERE id_art = %s"

    cursor.execute(command, (id,))
    actores = cursor.fetchall()

    strToPrint = "Atores:"
    print(term.move_xy((term.width // 2) + 5, borderY + 8) + term.palegreen1 + strToPrint)

    for i in range(len(actores)):
        strToPrint = actores[i][0] + " " + actores[i][1]
        print(term.move_xy((term.width // 2) + 13, borderY + 8 + i) + term.lightcyan + strToPrint)

    # ==== Detalhes ====
    strToPrint = "== Detalhes =="
    print(term.center(term.move_y(borderY + 13) + term.palegreen1 + strToPrint))

    textToWrap = data[4]

    txt = wrapper.wrap(text=textToWrap)

    for i in range(len(txt)):
        print(term.center(term.move_y(borderY + 14 + i) + term.lightcyan + str(txt[i])))

    nowTime = datetime.datetime.now()
    nowTimestamp = int(nowTime.timestamp())

    # Check if user already own's it
    command = "SELECT data_validade FROM aluguer WHERE cliente_pessoa_id_pessoa = %s " \
              "AND data_validade > %s " \
              "AND artigos_id_art = %s"
    cursor.execute(command, (idUser, nowTimestamp, id))
    data = cursor.fetchone()  # [0]>id_aluguer, data_validade

    # Get the user input

    if (cursor.rowcount == 0):
        strToPrint = "[1] -> Alugar (" + price + ")"
        print(term.center(term.move_y(borderY + 20) + term.palegreen1 + strToPrint))

        strToPrint = "[2] -> Sair"
        print(term.center(term.move_y(borderY + 22) + term.palegreen1 + strToPrint))

        strToPrint = "Escolha uma das opções a cima"
        option = getUserInput_Integer(strToPrint, 23, 2)

    else:
        endDate = int(data[0])
        endDate = datetime.datetime.fromtimestamp(endDate)

        strToPrint = "Já possui esse artigo até " + str(endDate.strftime("%d %b de %Y"))
        print(term.center(term.move_y(borderY + 20) + term.palegreen1 + strToPrint))

        strToPrint = "[1] -> Sair"
        print(term.center(term.move_y(borderY + 22) + term.palegreen1 + strToPrint))

        strToPrint = "Escolha uma das opções a cima"
        option = getUserInput_Integer(strToPrint, 23, 1) + 1  # Lazy way to reduce line of codes

    if option == 1:
        alugarArtigo(cursor, dbCon, id, idUser)
    elif option == 2:
        return


# ==== Alugar Artigo ====
# This funtion rents a certain item to the user
# Recieves a database cursor a database conection and the user id and a item id
# Status: Done
def alugarArtigo(cursor, dbCon, idArtigo, idUser):
    command = "SELECT pessoa_nome FROM cliente WHERE pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser,))
    username, = cursor.fetchone()
    clearScreen("Alugar Artigo User V4", username=username)

    command = "SELECT tipo, titulo, preco, tempo_para_ver FROM artigos WHERE id_art =%s"
    cursor.execute(command, (idArtigo,))
    data = cursor.fetchone()  # [0]>tipo, [1]>titulo, [2]>preco, [3]>tempo_para_ver, [4]>detalhes

    priceCents = int(data[2])

    price = "{:.2f}€".format(int(data[2]) / 100)

    strToPrint = str(data[0]) + ": " + str(data[1])
    print(term.center(term.move_y(borderY + 5) + term.lightcyan + strToPrint))

    nowTime = datetime.datetime.now()
    interval = datetime.timedelta(weeks=int(data[3]), hours=1)  # Just add an hour to prevent any time mistakes

    finalTime = nowTime + interval

    strToPrint = "Fica disponível até: " + str(finalTime.strftime("%d %b %Y às %H")) + ", total de " + \
                 str(data[3]) + " semana" + str(("s", "")[int(data[3]) == 1])  # Make plural if if bigger than one
    print(term.center(term.move_y(borderY + 7) + term.lightcyan + strToPrint))

    strToPrint = "Preço total pelo aluguer: " + price
    print(term.center(term.move_y(borderY + 9) + term.lightcyan + strToPrint))

    nowTimestamp = int(nowTime.timestamp())
    endTimestamp = int(finalTime.timestamp())

    strToPrint = "Quer alugar o artigo? (Sim/Não)"
    out = getUserInput_String(strToPrint, 16)
    out = out.lower()
    if out == "sim" or out == "s":
        try:
            command = "CALL aluguer(%s,%s,%s,%s,%s);"
            cursor.execute(command, (nowTimestamp, endTimestamp, priceCents, idArtigo, idUser))
        except psycopg2.errors.RaiseException as err:
            clearScreen("Alugar Artigo User V4")

            dbCon.rollback()  # Rollback and revert the last command

            error = str(err).split("\n")  # get the real error

            strToPrint = "Erro: " + str(error[0])
            print(term.center(term.move_y(borderY + 9) + term.tomato + strToPrint))
            strToPrint = "Voltando atrás"
            print(term.center(term.move_y(borderY + 12) + term.tomato + strToPrint))

            time.sleep(5)  # Let the user read the error
        else:
            dbCon.commit()  # It worked? Commit the data
    else:
        return
    return


# ==== Caixa de Entrada ====
# This funtion shows the user all the messages he recieved
# Recieves a database cursor a database conection and the user id and a item id
# Status: Badly Done, tables are messed up, if the message is for all creates lots of copys
# If one reads a for all messages every other user see it as read
def caixaEntradaUser(cursor, dbConn, idUser):
    command = "SELECT pessoa_nome FROM cliente WHERE pessoa_id_pessoa = %s"
    cursor.execute(command, (idUser,))
    username, = cursor.fetchone()
    clearScreen("Caixa de entrada V2", username=username)

    strToPrint = "Caixa de Entrada"
    print(term.center(term.move_y(borderY + 6) + term.palegreen1 + strToPrint))

    command = "SELECT assunto, corpo, mensagens_lida, id_msg FROM mensagem"
    cursor.execute(command)
    data = cursor.fetchall()  # [0]>assunto, [1]>corpo, [2]>mensagens_n_lidas, [3]>id_msg

    resultAmount = cursor.rowcount

    limit = 5
    linha = 0
    show = True

    print(term.move_xy((term.width // 2) - 8,
                       borderY + 20) + term.dodgerblue + "Por ler" + term.move_right(10) + term.lightcyan + "Lida")

    if (resultAmount > 0):
        for i in range(resultAmount):
            if show:
                if data[i][2] == False:
                    strToPrint = "[" + str(i + 1) + "] -> " + str(data[i][0])
                    print(term.move_xy((term.width // 2) - 10,
                                       borderY + 8 + linha) + term.dodgerblue + strToPrint + term.normal)
                else:
                    strToPrint = "[" + str(i + 1) + "] -> " + str(data[i][0])
                    print(
                        term.move_xy((term.width // 2) - 10, borderY + 8 + linha) + term.lightcyan + strToPrint)

                linha += 1

                if (linha >= limit) and (i != (resultAmount - 1)):
                    strToPrint = "Quer mais? (Sim/Não)"
                    out = getUserInput_String(strToPrint, 16)
                    out = out.lower()
                    if out == "sim" or out == "s":
                        clearLines(8, 8 + linha)
                        linha = 0
                    else:
                        show = False

        strToPrint = "Escolha a mensagem (Sair -> 0)"
        mensagem = getUserInput_Integer(strToPrint, 16, resultAmount, 0) - 1  # Arrays start at 0

        if mensagem != 0:
            clearScreen("Caixa de entrada V2", username=username)

            strToPrint = str(data[mensagem][0])
            print(term.center(term.move_y(borderY + 6) + term.palegreen1 + strToPrint))

            textToWrap = data[mensagem][1]

            txt = wrapper.wrap(text=textToWrap)

            for i in range(len(txt)):
                print(term.center(term.move_y(borderY + 9 + i) + term.lightcyan + str(txt[i])))

            strToPrint = "Escreva algo para sair"
            getUserInput_String(strToPrint, 16)

            msdId = data[mensagem][3]

            command = "UPDATE mensagem SET mensagens_lida = True WHERE id_msg = %s"
            cursor.execute(command, (msdId,))
            dbConn.commit()

    else:  # Nothing to show just get out
        strToPrint = "Não tem mensagens"
        print(term.center(term.move_y(borderY + 6) + term.lightcyan + strToPrint))
        strToPrint = "Escreva algo para sair"
        getUserInput_String(strToPrint, 16)
    return


# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# Main for test
if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    clearScreen("Teste")
    getUserInput_Email("Teste Email", 2)
    getUserInput_Integer("Teste Int", 2)
    getUserInput_String("Teste String", 2)
    firstPage()
    time.sleep(20)
    # Reset when leaving
    print(term.home + term.on_black + term.white + term.clear)
