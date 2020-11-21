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
import menus as draw
import passwordEncryption as pwd
import random

# ==== startUp funtion ====
# ==== End startUp funtion ====

def main():
    cursor, conn = db.connectToDB()

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    userInfo = draw.newAccount()

    print("Nome:", userInfo[0])
    print("Email:", userInfo[1])
    print("Password:", userInfo[2])


    my_password = b"%s" % (userInfo[2])
    my_data = b"mainString"

    print("key:  {}".format(my_password))
    print("data: {}".format(my_data))
    encrypted = pwd.encrypt(my_password, my_data)
    print("\nenc:  {}".format(encrypted))
    decrypted = pwd.decrypt(my_password, encrypted)
    print("dec:  {}".format(decrypted))
    print("\ndata match: {}".format(my_data == decrypted))
    print("\nSecond round....")
    encrypted = pwd.encrypt(my_password, my_data)
    print("\nenc:  {}".format(encrypted))
    decrypted = pwd.decrypt(my_password, encrypted)
    print("dec:  {}".format(decrypted))
    print("\ndata match: {}".format(my_data == decrypted))


    command = "INSERT INTO cliente(id_cliente,nome, email, password) VALUES (,'%s','%s','%s')" % (
        userInfo[0], userInfo[1], userInfo[2])

    cursor.execute(command)

    # Importante! Torna as alterações à base de dados persistentes
    conn.commit()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    main()
