# Importando sqlite
import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE kmControl(id INTEGER PRIMARY KEY AUTOINCREMENT, data DATE, calculo INT, kmInicial INT, kmFinal INT, kmMorto INT, kmRodado INT, peso FLOAT, entCol INT, dissel FLOAT, ganhos FLOAT, gastos FLOAT, manutencao FLOAT, saldo FLOAT, serie TEXT, imagem TEXT)")
    