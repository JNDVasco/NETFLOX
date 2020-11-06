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


# ==== startUp funtion ====
# ==== End startUp funtion ====

def main():
    cursor = db.connect()
    cursor.execute("""SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'public'""")
    for table in cursor.fetchall():
        print(table)


if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    main()
