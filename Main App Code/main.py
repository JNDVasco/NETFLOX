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

    command = "INSERT INTO cliente(id_cliente,nome, email, password) VALUES (2,'%s','%s','%s')" % (
        userInfo[0], userInfo[1], userInfo[2])

    cursor.execute(command)

    # Importante! Torna as alterações à base de dados persistentes
    conn.commit()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    main()
