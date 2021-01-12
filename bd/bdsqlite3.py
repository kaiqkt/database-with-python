import sqlite3

conexao = sqlite3.connect('bd.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 45.5))
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#                {'id': None, 'nome': 'Gabriel', 'peso': 125.0})
# conexao.commit()

# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {'nome': 'Joana', 'id': 2}
# )
#
# conexao.commit()
#
# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     {'id': 2}
# )

conexao.commit()

cursor.execute('SELECT * FROM clientes')

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()
