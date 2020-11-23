#==============================================================
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
#==============================================================
import time

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
def getUserInput_Integer(str, posY):
    errorStr = "Dê-me o número correspondente à opção!"

    posX = ((term.width // 2) - (len(str) // 2))

    while True:
        try:
            userInput = int(input(term.move_xy(posX, borderY + posY + 1) + term.lightcyan + str))
        except ValueError:
            print(term.move_xy((term.width // 2) - (len(errorStr) // 2), borderY + posY) + term.tomato + errorStr)
            print(term.move_xy(posX + 1, borderY + posY + 1) + term.black + blankLine)
            continue
        else:
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
            print(term.move_xy((term.width // 2) - (len(errorStr) // 2), borderY + posY) + term.tomato + errorStr)
            print(term.move_xy(posX + 1, borderY + posY + 1) + term.black + blankLine)
        else:
            break
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
            print(term.move_xy((term.width // 2) - (len(errorStr) // 2), borderY + posY) + term.tomato + errorStr)
            print(term.move_xy(posX + 1, borderY + posY + 1) + term.black + blankLine)
        else:
            break

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

    strToPrint = "Escolha uma das opções a cima: "
    option = getUserInput_Integer(strToPrint, 15)

    return option


# Status: notDone
def newAccount():
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

    strToPrint = "Nome utilizador: "
    username = getUserInput_String(strToPrint, 7)

    strToPrint = "Email: "
    email = getUserInput_Email(strToPrint, 9)

    strToPrint = "Password: "
    password = getUserInput_String(strToPrint, 11)

    print(term.home + term.on_black + term.clear)

    return username, email, password


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
    strToPrint = "Criar conta no NetFLOX"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 5) + term.palegreen1 + strToPrint)

    strToPrint = "Nome utilizador: "
    username = input(term.move_xy((term.width // 2) - 11, borderY + 7) + term.lightcyan + strToPrint)

    strToPrint = "Email: "
    email = input(term.move_xy((term.width // 2) - 11, borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "Password: "
    password = input(term.move_xy((term.width // 2) - 11, borderY + 11) + term.lightcyan + strToPrint)

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
    firstPage()
    time.sleep(5)
    output = newAccount()
    # Reset when leaving
    print(term.home + term.on_black + term.white + term.clear)
    print(output)
