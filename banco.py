import sqlite3

def tabela_diretores (banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS diretores(
                        id_diretor INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_diretor TEXT NOT NULL,
                        telefone_diretor INTEGER NOT NULL,
                        cpf_diretor INTEGER NOT NULL,
                        endereco_diretor TEXT
                        )''')

        conexao.commit()
        return "tabela diretores criada!"

    except sqlite3.Error as erro:
        print("Erro no banco de dados!" , erro)

    finally:    
        conexao.close()

def tabela_funcionarios (banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS funcionarios(
                        id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_funcionario TEXT NOT NULL,
                        telefone_funcionario INTEGER NOT NULL,
                        cpf_funcionario INTEGER NOT NULL,
                        endereco_funcionario TEXT,
                        id_diretor INTEGER,
                        FOREIGN KEY (id_diretor) REFERENCES diretores(id_diretor)
                        )''')

        conexao.commit()
        return "tabela funcionarios criada!"

    except sqlite3.Error as erro:
        print("Erro no banco de dados!" , erro)

    finally:    
        conexao.close()


def tabela_clientes (banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS clientes(
                        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_cliente TEXT NOT NULL,
                        telefone_cliente INTEGER NOT NULL,
                        cpf_cliente INTEGER NOT NULL,
                        endereco_cliente TEXT,
                        id_funcionario INTEGER,
                        FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id_funcionario)
                        )''')
    
        conexao.commit()
        return"tabela clientes criada!"

    except sqlite3.Error  as erro:
        print(f"Erro no banco de dados!" , erro)


def tabela_estoque (banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS estoque(
                        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_produto TEXT NOT NULL
                        )''')

        conexao.commit()
        return"tabela estoque criada!"

    except sqlite3.Error  as erro:
        print("Erro no banco de dados!" , erro)


banco = "teste_loja.db"
mensagem1 = tabela_diretores(banco)
mensagem2 = tabela_funcionarios(banco)
mensagem3 = tabela_clientes(banco)
mensagem4 = tabela_estoque(banco)

print(mensagem1)
print(mensagem2)
print(mensagem3)
print(mensagem4)