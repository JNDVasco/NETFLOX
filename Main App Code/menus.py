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
import textwrap
import time

from blessed import Terminal

# Create the terminal
term = Terminal()
# Create the text wrapper
wrapper = textwrap.TextWrapper(width=25)
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
def clearScreen(menuName):
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

# Status: SemiDone
def mainMenuUser(username, balance, unreadMessages):
    clearScreen("Menu Inicial User V1")

    # Main Body
    # User info
    strToPrint = "Bem-vindo, " + username + "."
    print(term.move_xy(borderX, borderY + 2) + term.lightcyan + strToPrint)

    strToPrint = "Saldo disponível: " + str(balance / 100) + "€"
    print(term.move_xy(borderX, borderY + 3) + term.lightcyan + strToPrint)

    # Menus
    strToPrint = "Escolha a opção pretendida"
    print(term.center(term.move_y(borderY + 6) + term.palegreen1 + strToPrint))

    strToPrint = "[1] -> Ver artigos"
    print(term.move_xy((term.width // 2) - 15, borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "[2] -> Artigos atuais"
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


# Status: notDone
def verArtigosUser():
    # Always clear the screen first
    clearScreen("Artigos User V1")
    # Main Body

    strToPrint = "Escolha a opção pretendida"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 6) + term.palegreen1 + strToPrint)

    strToPrint = "[1] -> Ver artigos disponíveis"
    print(term.move_xy((term.width // 2) - 15, borderY + 9) + term.lightcyan + strToPrint)

    strToPrint = "[2] -> Pesquisar Artigo"
    print(term.move_xy((term.width // 2) - 15, borderY + 10) + term.lightcyan + strToPrint)

    strToPrint = "[3] -> Alugar Artigo"
    print(term.move_xy((term.width // 2) - 15, borderY + 11) + term.lightcyan + strToPrint)

    strToPrint = "[4] -> Consultar Detalhes"
    print(term.move_xy((term.width // 2) - 15, borderY + 12) + term.lightcyan + strToPrint)

    strToPrint = "[5] -> Menu Principal"
    print(term.move_xy((term.width // 2) - 15, borderY + 14) + term.lightcyan + strToPrint)

    strToPrint = "Escolha uma das opções a cima"

    option = getUserInput_Integer(strToPrint, 17, 5)


def pesquisarArtigosUser(cursor, dbcon):

    searchType = "None"

    # Always clear the screen first
    clearScreen("Pesquisa de Artigos User V1")
    # Main Body

    strToPrint = "Escolha a forma de peesquisa pretendida"
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


def artigoDisponiveisUser(cursor, dbcon):
    clearScreen("Artigos User V1")

    strToPrint = "Artigos disponíveis"
    print(term.move_xy((term.width // 2) - 10, borderY + 5) + term.palegreen1 + strToPrint)

    command = "SELECT id_art,titulo FROM artigos ORDER BY id_art ASC"  # Get all the content ordered by the id
    cursor.execute(command)
    data = cursor.fetchall()
    total = cursor.rowcount

    counter = 0
    exit = False
    limit = 5
    linha = 0

    for i in range(total // 2):
        if not exit:
            print(term.move_xy((term.width // 2) - 35,
                               borderY + 7 + linha) + term.lightcyan + "[" + str(data[counter][0]) + "] -> " +
                  data[counter][1])

            counter = counter + 1

            print(term.move_xy((term.width // 2) + 15,
                               borderY + 7 + linha) + term.lightcyan + "[" + str(data[counter][0]) + "] -> " +
                  data[counter][1])

            counter = counter + 1

            linha = linha + 1  # Avança para a próxima linha

            if i >= limit:
                strToPrint = "Quer mais? (Sim/Não)"
                out = getUserInput_String(strToPrint, 16)
                out = out.lower()
                if out == "sim":
                    clearScreen("Artigos User V1")
                    linha = 0
                    limit = limit + 6
                else:
                    strToPrint = "Quer consultar os detalhes? (Sim/Não)"
                    out = getUserInput_String(strToPrint, 16)
                    out = out.lower()
                    if out == "sim":
                        strToPrint = "Dê-me o número do filme"
                        out = getUserInput_Integer(strToPrint, 16)
                        command = "SELECT titulo, detalhes FROM artigos WHERE id_art = {id}".format(id=out)
                        cursor.execute(command)
                        name, details = cursor.fetchone()
                        strToPrint = "Filme" + name
                        print(term.move_xy((term.width // 2) - 35, borderY + 5) + term.lightcyan + strToPrint)

                        strToPrint = "Detalhes" + details
                        strToPrint = wrapper.fill(text=strToPrint)
                        print(term.move_xy((term.width // 2) - 35, borderY + 7) + term.lightcyan + strToPrint)
                        exit = True
                    else:
                        exit = True

                        print("Voltando ao main")
    return


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
