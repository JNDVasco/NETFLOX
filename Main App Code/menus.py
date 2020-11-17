import time

from blessed import Terminal

# Create the terminal
term = Terminal()

# Border, keeps everything a bit more together
borderX = term.width // 5
borderY = term.height // 6


# print(term.home + term.on_blue + term.clear) Clear Screen

def firstPage():
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    print(term.move_xy(borderX, borderY) + term.orangered2 + "Aplicação NetFLOX")

    #Header text
    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bem-vindo ao NetFLOX"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 5) + term.orangered2 + strToPrint)

    #Main Body
    strToPrint = "== Utilizadores =="
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 7) + term.aqua + strToPrint)

    strToPrint = "Fazer login"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 8) + term.aqua + strToPrint)

    strToPrint = "Criar Conta"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 9) + term.aqua + strToPrint)

    strToPrint = "== Administradores =="
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 12) + term.turquoise3 + strToPrint)

    strToPrint = "Fazer login"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 13) + term.turquoise3 + strToPrint)

    #Footer text
    strToPrint = "Escolha o que deseja fazer a partir das opções de cima"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 16) + term.turquoise3 + strToPrint)

    strToPrint = "Página Inicial V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


def mainMenuUser(username, balance):
    # Always clear the screen first
    print(term.home + term.on_black + term.clear)

    print(term.move_xy(borderX, borderY) + term.orangered2 + "Aplicação NetFLOX")

    #Header text
    strToPrint = "Bases de Dados 2020/2021"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), borderY) + term.orangered2 + strToPrint)

    strToPrint = "Bem-vindo ao NetFLOX"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 5) + term.orangered2 + strToPrint)

    #Main Body
    strToPrint = "== Utilizadores =="
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 7) + term.aqua + strToPrint)

    strToPrint = "Fazer login"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 8) + term.aqua + strToPrint)

    strToPrint = "Criar Conta"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 9) + term.aqua + strToPrint)

    strToPrint = "== Administradores =="
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 12) + term.turquoise3 + strToPrint)

    strToPrint = "Fazer login"
    print(term.move_xy((term.width // 2) - (len(strToPrint) // 2), borderY + 13) + term.turquoise3 + strToPrint)

    #Footer text
    strToPrint = "Menu Inicial User V1"
    print(term.move_xy(borderX, term.height - borderY) + term.orangered2 + strToPrint)

    strToPrint = "JNDVasco"
    print(term.move_xy(term.width - (borderX + len(strToPrint)), term.height - borderY) + term.orangered2 + strToPrint)


if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    firstPage()
    time.sleep(40)
    # Reset when leaving
    print(term.home + term.on_black + term.white + term.clear)
