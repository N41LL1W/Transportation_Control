# Importando sqlite
import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.dp')


# Inserir dados
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO kmControl (data, calculo, kmInicial, kmFinal, kmMorto, kmRodado, peso, entCol, dissel, " \
                "ganhos, gastos, manutencao, saldo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        cur.execute(query, i)


# Acessar Informações
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM kmControl"
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista.append(i)
    return lista


# lista = ['nome', 1]
'''
# Atualizar dados
with con:
    cur = con.cursor()
    query = "UPDATE kmControl SET nome=? WHERE id=?"
    cur.execute(query, lista)

# Deletar dados
with con:
    cur = con.cursor()
    query = "DELETA FROM kmControl WHERE id=?"
    cur.execute(query, lista)
'''
