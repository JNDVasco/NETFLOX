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
    cursor = db.connectToDB()
    cursor.execute("""SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'public'""")
    for table in cursor.fetchall():
        print(table)

    table = input("Qual a tabela? ->")

    print("Dados da tabela")
    postgreSQL_select_Query = "select * from %s" % table

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in mobile_records:
        print("Id = ", row[0], )
        print("Country = ", row[1])
        print("Last Update  = ", row[2], "\n")

if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    main()
