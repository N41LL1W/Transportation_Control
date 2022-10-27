# Importando sqlite
import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.dp')

# CRUD
    # Creatu = Inserir / Criar
    # Ready = Acessar / Mostrar
    # Update = Atualizar
    # DELETE = Deletar / Apagar



# Inserir dados
with con:
    cur = con.cursor()
    query = "INSERT INTO kmControl (data, calculo, kmInicial, kmFinal, kmMorto, kmRodado, peso, entCol, dissel, ganhos, gastos, manutencao, saldo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(query, lista)

# Acessar Informações
with con:
    cur = con.cursor()
    query = "SELECT * FROM kmControl"
    cur.execute(query)
    info = cur.fetchall()
    print(info)


lista = ['nome', 1]

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