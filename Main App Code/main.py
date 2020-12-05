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


    # menu.artigoDisponiveisUser(cursor, conn)
    #
    menu.firstPage()

    print("já sai")
    cursor.close()
    conn.close()

if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    cursor, conn = db.connectToDB()

    dbStatus = conn.get_dsn_parameters()
    print(dbStatus['dbname'], "@", dbStatus['host'], sep="")

    for i in range(3):
        print("Iniciando em {timeLeft}".format(timeLeft = (3 - i)))
        time.sleep(1)

    main(cursor, conn)
