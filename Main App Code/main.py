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
import menus as draw
import database as db


# ==== startUp funtion ====
# ==== End startUp funtion ====

def main():
    cursor = db.connectToDB()

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    cursor.close()

    db.closeConnectionDB()


if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    main()
