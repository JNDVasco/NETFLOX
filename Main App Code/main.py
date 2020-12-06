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

def main(cur, dbConn):

    userOption = menu.firstPage()

    if userOption == 1:
        menu.userLogin()

    elif userOption == 2:
        menu.newAccount()

    elif userOption == 3:
        menu.adminLogin()

    cur.close()
    dbConn.close()


if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    cursor, conn = db.connectToDB()

    dbStatus = conn.get_dsn_parameters()
    print(dbStatus['dbname'], "@", dbStatus['host'], sep="")

    time.sleep(1)

    main(cursor, conn)

    print("==== FIM ====")
    time.sleep(2)
    print("\033c")
