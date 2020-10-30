# ==============================================================
# Base de Dados - UCoimbra MiEEC 2020/2021
# Projeto: NETFLOX
# Gonçalo Cavaleiro - UC6969696969
# João Vasco        - UC2019236378
#
# Ficheiro: Main
#
# Descrição:
#
#
# Depêndencias              Versão
# ==============================================================


import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    print("BaseDeDados")

    var1 = config['BaseDeDados']['Host']
    var2 = config['BaseDeDados']['User']
    var3 = config['BaseDeDados']['DataBase']
    var4 = config['BaseDeDados']['Password']
    print(var1)
    print(var2)
    print(var3)
    print(var4)

    print("\nSection1")

    var1 = config['Section1']['Param1']
    var2 = config['Section1']['Param2']
    var3 = config['Section1']['Param3']
    var4 = config['Section1']['Param4']
    print(var1)
    print(var2)
    print(var3)
    print(var4)

    print("\nSection2")

    var1 = config['Section2']['Param1']
    var2 = config['Section2']['Param2']
    var3 = config['Section2']['Param3']
    var4 = config['Section2']['Param4']
    print(var1)
    print(var2)
    print(var3)
    print(var4)
