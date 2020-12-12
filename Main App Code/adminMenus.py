# ==============================================================
# Base de Dados - UCoimbra MiEEC 2020/2021
# Projeto: NETFLOX
# Gonçalo Cavaleiro - UC2018279569
# João Vasco        - UC2019236378
#
# Ficheiro: adminMenus.py
#
# Descrição:
# Este ficheiro contém os menus relacionados com o admin
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
# ==== Admin Main Menu ====
# This funtion has the main options the user needs
# recieves the username, balance and unread messages
# Status: Done
def mainMenu(username):
    clearScreen("Menu Inicial Admin V1", username=username)

    # Main Body
    # User info
    # Menus
    strToPrint = "Escolha a opção pretendida"
    print(term.center(term.move_y(borderY + 6) + term.palegreen1 + strToPrint))

    strToPrint = "[1] -> Gestão de Artigos"
    print(term.move_xy((term.width // 2) - 15, borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "[2] -> Aumentar Saldo"
    print(term.move_xy((term.width // 2) - 15, borderY + 10) + term.lightcyan + strToPrint)

    strToPrint = "[3] -> Estatísticas"
    print(term.move_xy((term.width // 2) - 15, borderY + 11) + term.lightcyan + strToPrint)

    strToPrint = "[4] -> Mensagens"
    print(term.move_xy((term.width // 2) - 15, borderY + 12) + term.lightcyan + strToPrint)

    strToPrint = "[5] -> Logout"
    print(term.move_xy((term.width // 2) - 15, borderY + 14) + term.lightcyan + strToPrint)

    strToPrint = "Escolha uma das opções a cima"
    option = getUserInput_Integer(strToPrint, 17, 5)

    return option

def aumentarSaldo(cursor, dbConn, idUser):
    # Always clear the screen first
    clearScreen("Aumentar Saldo Admin V1")
    # Main Body


    strToPrint = "Aumentar saldo"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

    strToPrint = "Introduza o mail do utilizador a receber o dinheiro"
    emailUser = getUserInput_Email(strToPrint, 6)

    strToPrint = "Introduza a quantia em Euro (Max: 150€)"
    quantia = getUserInput_Integer(strToPrint, 8, 150, 0) * 100 # Database stores money in cents

    price = "{:.2f}€".format(quantia / 100)

    clearScreen("Aumentar Saldo Admin V1")

    strToPrint = "Quer mesmo adiconar " + price + " a " + emailUser + " (Sim/Não)"
    out = getUserInput_String(strToPrint, 8)
    out = out.lower()

    if out == "sim" or out == "s":
        command = "UPDATE cliente SET saldo = saldo + %s WHERE pessoa_email = %s"
        cursor.execute(command, (quantia, emailUser))
        dbConn.commit()
    else:
       return

    return


# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# Main for test
if __name__ == '__main__':
    print("Menus Admin")
