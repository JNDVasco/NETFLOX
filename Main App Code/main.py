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
import time

from passlib.hash import sha256_crypt


# ==== startUp funtion ====
# ==== End startUp funtion ====

def main():
    cursor, conn = db.connectToDB()

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    menu.artigoDisponiveisUser(cursor, conn)

    print("já sai")

    time.sleep(20)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    main()
