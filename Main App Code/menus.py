import time

from blessed import Terminal

# Create the terminal
term = Terminal()

# Border, keeps everything a bit more together
borderX = term.width // 5
borderY = term.height // 6

# Colors
#   orangered2
#   turquoise1
#
#


# print(term.home + term.on_blue + term.clear) Clear Screen

# ==== First Pages ====

# Status: SemiDone
def firstPage():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body
    strToPrint = "Bem-vindo ao NetFLOX"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 5) + term.orangered2 + strToPrint)

    strToPrint = "== Utilizadores =="
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 7) + term.turquoise1 + strToPrint)

    strToPrint = "[1] -> Fazer login"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 8) + term.turquoise1 + strToPrint)

    strToPrint = "[2] -> Criar Conta"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 9) + term.turquoise1 + strToPrint)

    strToPrint = "== Administradores =="
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 12) + term.turquoise1 + strToPrint)

    strToPrint = "[3] -> Fazer login"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 13) + term.turquoise1 + strToPrint)

    # Footer text
    strToPrint = "Escolha o que deseja fazer a partir das opções de cima"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 16) + term.turquoise1 + strToPrint)

    strToPrint = "Página Inicial V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def newAccount():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Footer text
    strToPrint = "Nova conta user V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)

    # Main Body
    strToPrint = "Criar conta no NetFLOX"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 5) + term.orangered2 + strToPrint)

    strToPrint = "Nome utilizador: "
    username = input(term.move_xy((term.width // 2) - 11, borderY + 7) + term.turquoise1 + strToPrint)

    strToPrint = "Email: "
    email = input(term.move_xy((term.width // 2) - 11, borderY + 9) + term.turquoise1 + strToPrint)

    strToPrint = "Password: "
    password = input(term.move_xy((term.width // 2) - 11, borderY + 11) + term.turquoise1 + strToPrint)

    print(term.home + term.on_black + term.clear)

    return username, email, password

# ==== User Menus ====

# Status: SemiDone
def mainMenuUser(username, balance, unreadMessages):
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body
    # User info
    strToPrint = "Bem-vindo, " + username + "."
    print(term.move_xy(borderX, borderY + 2) + term.turquoise1 + strToPrint)

    strToPrint = "Saldo disponível: " + str(balance / 100) + "€"
    print(term.move_xy(borderX, borderY + 3) + term.turquoise1 + strToPrint)

    # Menus
    strToPrint = "Escolha a opção pretendida"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 5) + term.orangered2 + strToPrint)

    strToPrint = "[1] -> Artigos "
    print(term.move_xy((term.width // 2) - (10), borderY + 7) + term.turquoise1 + strToPrint)

    strToPrint = "[2] -> Ver artigos"
    print(term.move_xy((term.width // 2) - (10), borderY + 8) + term.turquoise1 + strToPrint)

    strToPrint = "[3] -> Artigos atuais"
    print(term.move_xy((term.width // 2) - (10), borderY + 9) + term.turquoise1 + strToPrint)

    strToPrint = "[4] -> Histórico e Estatísticas"
    print(term.move_xy((term.width // 2) - (10), borderY + 12) + term.turquoise1 + strToPrint)

    strToPrint = "[5] -> Caixa de Entrada (" + str(unreadMessages) + ")"
    print(term.move_xy((term.width // 2) - (10), borderY + 15) + term.turquoise1 + strToPrint)

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoDisponiveisUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoDisponiveisSearchUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoAlugarUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoDetalhesUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoAtuaisUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoAtuaisSearchUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoHistoryUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def inboxUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def readMessageUser():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# ==== Admin Menus ====
# Status: notDone
def mainMenuAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoGestaoAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoCorrigirPrecoAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoAddRemoveAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def artigoVerAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def aumentarSaldoAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def estatisticasAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def inboxAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Status: notDone
def sendMessageAdmin():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    # Header text
    strToPrint = "Aplicação NetFLOX"
    print(term.move_xy(borderX, borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    # Main Body

    # Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


# Main for test
if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    firstPage()
    time
    output = newAccount()
    # Reset when leaving
    print(term.home + term.on_black + term.white + term.clear)
    print(output)
