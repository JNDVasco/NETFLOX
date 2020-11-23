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
        userInfo = menu.newAccount()

        print("Nome:", userInfo[0])
        print("Email:", userInfo[1])
        print("Password:", userInfo[2])

        command = "INSERT INTO cliente(nome, email, password) VALUES ('%s','%s','%s')" % (
            userInfo[0], userInfo[1], userInfo[2])

        cursor.execute(command)

        # Importante! Torna as alterações à base de dados persistentes
        conn.commit()

    # my_password = userInfo[2].encode('UTF-8')
    # my_data = b"mainString"
    #
    # print("key:  {}".format(my_password))
    # print("data: {}".format(my_data))
    # encrypted = pwd.encrypt(my_password, my_data)
    # print("\nenc:  {}".format(encrypted))
    # decrypted = pwd.decrypt(my_password, encrypted)
    # print("dec:  {}".format(decrypted))
    # print("\ndata match: {}".format(my_data == decrypted))
    # print("\nSecond round....")
    # encrypted = pwd.encrypt(my_password, my_data)
    # print("\nenc:  {}".format(encrypted))
    # decrypted = pwd.decrypt(my_password, encrypted)
    # print("dec:  {}".format(decrypted))
    # print("\ndata match: {}".format(my_data == decrypted))

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
