import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        consulta = 'SELECT * FROM agenda'
        self.cursor.execute(consulta)
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


agenda = AgendaDB('agenda.db')
agenda.inserir('Kaique', '111234')
agenda.inserir('Luiz', '111236')
agenda.inserir('Joao', '111237')
agenda.inserir('Fabricio Luiz', '111238')
agenda.inserir('Jose', '111238')


agenda.editar('Zed Gomes', '40028927', 24)
agenda.excluir(24)
agenda.buscar('Luiz')

agenda.fechar()
