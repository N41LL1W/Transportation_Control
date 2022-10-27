# Importando sqlite
import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE kmControl(id INTEGER PRIMARY KEY AUTOINCREMENT, data DATE, calculo NUMBER, kmInicial NUMBER, kmFinal NUMBER, kmMorto NUMBER, kmRodado INT, peso DECIMAL, entCol INT, dissel DECIMAL, ganhos DECIMAL, gastos DECIMAL, manutencao DECIMAL, saldo DECIMAL, serie TEXT, imagem TEXT)")
    