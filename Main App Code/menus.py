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
import time

from passlib.hash import sha256_crypt as pwd

from blessed import Terminal

# Create the terminal
term = Terminal()

# Border, keeps everything a bit more together
borderX = term.width // 5
borderY = term.height // 6

# just a line to clear a specific part
blankLine = "thisStringJustGetsPrintedInBlackToClearTheLine"


# ==== Get User Input ====
# This funtion get the user input, forces to be an integer
# Status: Done
def getUserInput_Integer(str, posY, maxOption):
    errorStr = "Dê-me o número correspondente à opção!"
    errorStrMaxNumber = "           Opção não disponível           "

    posX = ((term.width // 2) - (len(str) // 2))

    while True:
        try:
            userInput = int(input(term.move_xy(posX, borderY + posY + 1) + term.lightcyan + str))
        except ValueError:
            print(term.move_xy((term.width // 2) - (len(errorStr) // 2), borderY + posY) + term.tomato + errorStr)
            print(term.move_xy(posX + 1, borderY + posY + 1) + term.clear_eol)
            continue
        else:
            if userInput > maxOption:
                print(term.move_xy(0, borderY + posY) + term.clear_eol)
                print(term.move_xy((term.width // 2) - (len(errorStrMaxNumber) // 2),
                                   borderY + posY) + term.tomato + errorStrMaxNumber)
                print(term.move_xy(posX + 1, borderY + posY + 1) + term.clear_eol)
                continue
            print(term.move_xy(0, borderY + posY) + term.clear_eol)
            return userInput


# ==== Get User Input ====
# This funtion get the user input, forces to be an email
# Just checks if there is a "@" present
# Removes all spaces at the start and the end
# Status: Done
def getUserInput_Email(str, posY):
    errorStr = "Dê-me um email válido!"

    posX = ((term.width // 2) - (len(str) // 2))

    while True:
        userInput = input(term.move_xy(posX, borderY + posY + 1) + term.lightcyan + str)
        userInput = userInput.strip()  # Remove all spaces at start and end

        if userInput.find("@") == -1:
            print(term.move_xy(0, borderY + posY) + term.clear_eol)
            print(term.move_xy((term.width // 2) - (len(errorStr) // 2), borderY + posY) + term.tomato + errorStr)
        else:
            break
    print(term.move_xy(0, borderY + posY) + term.clear_eol)
    return userInput


# ==== Get User Input ====
# This funtion get the user input, forces to be an string
# Just checks if there is any char after removing spaces
# Removes all spaces at the start and the end
# Status: Done
def getUserInput_String(str, posY):
    errorStr = "Dê-me pelo menos um caracter!"

    posX = ((term.width // 2) - (len(str) // 2))

    while True:
        userInput = input(term.move_xy(posX, borderY + posY + 1) + term.lightcyan + str)
        userInput = userInput.strip()  # Remove all spaces at start and end

        if userInput == "":
            print(term.move_xy(0, borderY + posY) + term.clear_eol)
            print(term.move_xy((term.width // 2) - (len(errorStr) // 2), borderY + posY) + term.tomato + errorStr)
            print(term.move_xy(posX + 1, borderY + posY + 1) + term.clear_eol)
        else:
            break
    print(term.move_xy(0, borderY + posY) + term.clear_eol)
    return userInput


# ======================================================

# ==== First Pages ====

# Status: SemiDone
def firstPage():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Footer text
    strToPrint = "Página Inicial V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)

    # Main Body
    strToPrint = "Bem-vindo ao NetFLOX"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 5) + term.palegreen1 + strToPrint)

    strToPrint = "== Utilizadores =="
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 7) + term.lightcyan + strToPrint)

    strToPrint = "[1] -> Fazer login"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 8) + term.lightcyan + strToPrint)

    strToPrint = "[2] -> Criar Conta"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "== Administradores =="
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 12) + term.lightcyan + strToPrint)

    strToPrint = "[3] -> Fazer login"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 13) + term.lightcyan + strToPrint)

    strToPrint = "[4] -> Sair do NetFLOX"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 16) + term.lightcyan + strToPrint)

    strToPrint = "Escolha uma das opções a cima: "
    option = getUserInput_Integer(strToPrint, 19, 4)

    return option


# Status: notDone
def newAccount(cursor, dbConn):
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Footer text
    strToPrint = "Nova conta user V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)

    # Main Body
    strToPrint = "Criar conta no NetFLOX"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 5) + term.palegreen1 + strToPrint)

    while True:

        errorStr = "Já existe um utilizador com esse email"

        # Get the data of the user
        strToPrint = "Nome utilizador: "
        username = getUserInput_String(strToPrint, 7)
        strToPrint = "Email: "
        email = getUserInput_Email(strToPrint, 9)
        strToPrint = "Password: "
        password = getUserInput_String(strToPrint, 11)

        print(term.home + term.on_black + term.clear)


        # ==== Create the account in the database

        password = pwd.hash(password)

        try:
            query = "INSERT INTO clientes(nome, email, password, is_admin) VALUES ('%s','%s','%s','%s')" % (
                username, email, password, False)
            cursor.execute(query)
            # Importante! Torna as alterações à base de dados persistentes
            dbConn.commit()
        except Exception:
            print(term.move_xy((term.width // 2) - (len(errorStr) // 2), borderY) + term.tomato + errorStr)
            continue
        else:
            query = "INSERT INTO clientes(nome, email, password, is_admin) VALUES ('%s','%s','%s','%s')" % (
                userInfo[0], userInfo[1], userInfo[2], False)
            cursor.execute(query)
            # Importante! Torna as alterações à base de dados persistentes
            dbConn.commit()


def login():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Footer text
    strToPrint = "Login V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)

    # Main Body
    strToPrint = "Login no NetFLOX"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 5) + term.palegreen1 + strToPrint)

    strToPrint = "Email: "
    email = getUserInput_Email(strToPrint, 9)

    strToPrint = "Password: "
    password = getUserInput_String(strToPrint, 11)

    print(term.home + term.on_black + term.clear)


# ==== User Menus ====

# Status: SemiDone
def mainMenuUser(username, balance, unreadMessages):
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body
    # User info
    strToPrint = "Bem-vindo, " + username + "."
    print(term.move_xy(borderX, borderY + 2) + term.lightcyan + strToPrint)

    strToPrint = "Saldo disponível: " + str(balance / 100) + "€"
    print(term.move_xy(borderX, borderY + 3) + term.lightcyan + strToPrint)

    # Menus
    strToPrint = "Escolha a opção pretendida"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 5) + term.palegreen1 + strToPrint)

    strToPrint = "[1] -> Artigos "
    print(term.move_xy((term.width // 2) - 10, borderY + 7) + term.lightcyan + strToPrint)

    strToPrint = "[2] -> Ver artigos"
    print(term.move_xy((term.width // 2) - 10, borderY + 8) + term.lightcyan + strToPrint)

    strToPrint = "[3] -> Artigos atuais"
    print(term.move_xy((term.width // 2) - 10, borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "[4] -> Histórico e Estatísticas"
    print(term.move_xy((term.width // 2) - 10, borderY + 12) + term.lightcyan + strToPrint)

    strToPrint = "[5] -> Caixa de Entrada (" + str(unreadMessages) + ")"
    print(term.move_xy((term.width // 2) - 10, borderY + 15) + term.lightcyan + strToPrint)

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoDisponiveisUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoDisponiveisSearchUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoAlugarUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoDetalhesUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoAtuaisUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoAtuaisSearchUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoHistoryUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def inboxUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def readMessageUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# ==== Admin Menus ====
# Status: notDone
def mainMenuAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoGestaoAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoCorrigirPrecoAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoAddRemoveAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def artigoVerAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def aumentarSaldoAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def estatisticasAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def inboxAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Status: notDone
def sendMessageAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.palegreen1 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.palegreen1 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.palegreen1 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.palegreen1 + strToPrint)


# Main for test
if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    login()
    time.sleep(5)
    print(term.home + term.on_black + term.white + term.clear)
