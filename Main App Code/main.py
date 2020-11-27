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
#
# Depêndencias              Versão
# ==============================================================
# ==== Import files ====

import database as db
import menus as menu


# ==== startUp funtion ====
# ==== End startUp funtion ====

def main():
    cursor, conn = db.connectToDB()

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    option = menu.firstPage()

    if option == 2:
        menu.newAccount(cursor, conn)
    cursor.close()
    conn.close()

    print("Fim, opção:", option)


if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    main()

    # integer = menu.getUserInput_Integer("Teste Inteiro: ", 20)
    # email = menu.getUserInput_Email("Teste Email: ", 24)
    # string = menu.getUserInput_String("Teste String: ", 28)
    #
    # print("Inteiro:", integer)
    # print("Email:", email)
    # print("String:", string)
