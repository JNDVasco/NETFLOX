import configparser
import time
import psycopg2

def main(cur, dbConn):
    print("Faz as coisas aqui, cur  é o cursor, dbConn é a conexão à base de dados")


# ======================================================================================================================
def connectToDB():
    config = configparser.ConfigParser()
    config.read('config.ini')

    configParams = config.items("PostgresDB_Credentials")

    dbParams = {}

    for i in configParams:
        dbParams[i[0]] = i[1]

    db = psycopg2.connect(**dbParams)

    dbCursor = db.cursor()

    return dbCursor, db


# ======================================================================================================================


if __name__ == '__main__':
    print("==== NetFLOX starting! ====")
    cursor, conn = connectToDB()

    dbStatus = conn.get_dsn_parameters()
    print(dbStatus['dbname'], "@", dbStatus['host'], sep="")

    time.sleep(1)

    main(cursor, conn)

    cursor.close()
    conn.close()

    print("==== FIM ====")
    time.sleep(2)
    print("\033c")


# ----------------------------------------------------------------------------------------------------------------------
 #ADMIN artigos

SELECT ID_Art, Preco, Tempo_para_ver FROM artigos WHERE id_art = {id}".format(id=out)



#-----------------------------------------------------------------------------------------------------------------------
 # ADMIN muda preço

 SELECT ID_Art, Preco, Preco_anterior, Data FROM Artigos, Historico_Artigos

    Artigos.ID_Art = Historico_Artigos.ID_Art
    Preco = Preco_anterior
    print ("introduzir novo preco: " NovoPreco )
    NovoPreco = Preco
    print("data da mudança: " data )
#-----------------------------------------------------------------------------------------------------------------------
#Ver estatisticas

    SELECT * FROM Estatistica ORDER BY ID_Estatistica

#-----------------------------------------------------------------------------------------------------------------------
#tabela estatisticas

    SELECT Total_Clientes, total_art_por_tipo, Valor_Total_Compra, tempo_total_alugado, Tipo_mais_alugado, ID_Pessoa, ID_Art, Tipo, Sum(Preco) FROM Estatistica, Artigos, Cliente

    Total_Clientes = count(Cliente.ID_pessoa)
    Total_art_por_tipo = max(ID_Art)

    #idk?


#Total clientes

    INSERT INTO Estatistica (Total_Clientes)
    VALUES (count(Cliente.ID_pessoa))

    cursor.fetchone()

#Total artigos

    INSERT INTO Estatistica (Total_Artigos)
    VALUES (count(Artigos.ID_Art))

    cursor.fetchone()

#Valor Total alugado

    INSERT INTO Estatistica (Valor_Total_Alugado)
    VALUES(sum(aluguer.preco))
    WHERE data = true

    cursor.fetchone()

#Valor total Alugueres

    INSERT INTO Estatistica (Valor_Total_alugueres)
    VALUES(sum(aluguer.preco))

    cursor.fetchone()


#Total artigo por tipo (filmes)

    INSERT INTO Estatistica (total_art_por_tipo)
    VALUES(count(Artigos.Tipo))

    WHERE Tipo = 'Filme'

    Total_Artigos - Total_art_por_tipo = series

    cursor.fetchone

    print("series:", series, " filmes:", Total_art_por_tipo)


#Tempo total alugado

    INSERT INTO Estatistica (tempo_total_alugado)
    VALUES(sum(aluguer.Tempo_Para_Ver))

    cursor.fetchone()

# FUNÇÃO POR ADICIONAR A ESTATISTICA










#-----------------------------------------------------------------------------------------------------------------------
#aumenta saldo

    SELECT Saldo, ID_Pessoa FROM Cliente
    X= input("id da pessoa que quer mudar o saldo:")
    WHERE X=ID_pessoa

    NovoSaldo = input("Quanto quer aumentar? ")
    NovoSaldo = Saldo+NovoSaldo
    Saldo = NovoSaldo

    cursor.fetchone

#-----------------------------------------------------------------------------------------------------------------------

#elimina produto nao alugado


    SELECT ID_Art FROM Aluguer, Artigos
    ID = input("ID do artigo que quer eliminar:")

    if (ID != Aluguer.ID_Art) and (ID != Artigos.ID_Art)
    DELETE FROM Artigos
    WHERE ID = ID_Art
    else print("produto já alugado, não pode ser eliminado")

#-----------------------------------------------------------------------------------------------------------------------





