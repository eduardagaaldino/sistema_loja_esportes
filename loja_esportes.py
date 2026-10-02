import sqlite3

#tabelas
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


def tabela_produtos (banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS produtos(
                        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_produto TEXT NOT NULL,
                        marca_produto TEXT NOT NULL,
                        preco_produto REAL NOT NULL,
                        estoque INTEGER NOT NULL
                        )''')

        conexao.commit()
        return"produtos estoque criada!"

    except sqlite3.Error  as erro:
        print("Erro no banco de dados!" , erro)


banco = "teste_loja.db"
mensagem1 = tabela_diretores(banco)
mensagem2 = tabela_funcionarios(banco)
mensagem3 = tabela_clientes(banco)
mensagem4 = tabela_produtos(banco)

print(mensagem1)
print(mensagem2)
print(mensagem3)
print(mensagem4)


#diretores
def cadastrar_diretores(nome_diretor, telefone_diretor , cpf_diretor , endereco_diretor , banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute(f'''INSERT INTO diretores
                        (nome_diretor, telefone_diretor , cpf_diretor , endereco_diretor )
                        VALUES ('{nome_diretor}', '{telefone_diretor}', '{cpf_diretor}', '{endereco_diretor}')''')

        conexao.commit()
        conexao.close()

        return("diretor cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar diretor" , erro)


def listar_diretores(banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM diretores")
        diretores = cursor.fetchall()

        conexao.close()

        print("\n--- DIRETORES ---")

        if not diretores:
            print("Nenhum diretor cadastrado.")
        else:
            for diretor in diretores:
                print(
                    f"ID: {diretor[0]} | "
                    f"Nome: {diretor[1]} | "
                    f"telefone: {diretor[2]} | "
                    f"cpf: {diretor[3]} | "
                    f"endereco: {diretor[4]} |"
                )

    except sqlite3.Error as erro:
        print(f"Erro ao listar diretores" , erro)

def atualizar_diretores(id_diretor, novo_nome_diretor, novo_telefone_diretor, novo_cpf_diretor, novo_endereco_diretor, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''
        UPDATE diretores
        SET nome_diretor = '{novo_nome_diretor}',
            telefone_diretor = '{novo_telefone_diretor}',
            cpf_diretor = '{novo_cpf_diretor}',
            endereco_diretor = '{novo_endereco_diretor}'
        WHERE id_diretor = {id_diretor}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            return("diretor atualizado com sucesso!")
        else:
            return("Nenhuma diretor foi encontrado com esse ID!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!", erro)

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()

def excluir_diretores(id_diretor , banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''DELETE FROM diretores WHERE id_diretor = {id_diretor}'''

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            return "diretor excluído com sucesso!"
        else:
            return "Nenhum diretor foi encontrado com esse ID."

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!", erro)

    finally:
        conexao.close()

def menu_diretores():
    try:
        opcao = 0

        while opcao != 5:
            print("---------------------------------------------")
            print("1- cadastrar diretor")
            print("2- listar diretor ")
            print("3- atualizar diretor ")
            print("4- excluir diretor ")
            print("5- sair")
            opcao = int(input("escolha uma das opcoes a cima: "))
            print("---------------------------------------------")

            if opcao == 1:
                nome_diretor = input("digite o nome do diretor:")
                telefone_diretor = int(input("digite o telefone do diretor:"))
                cpf_diretor = int(input("digite o cpf do diretor:"))
                endereco_diretor = input("digite o endereco do diretor:")
                banco = 'teste_loja.db'
                cadastrar_diretores(nome_diretor, telefone_diretor , cpf_diretor , endereco_diretor , banco)

            elif opcao == 2:
                banco = 'teste_loja.db'
                listar_diretores(banco)
            
            elif opcao == 3:
                id_diretor = int(input("Digite o ID do diretor que deseja alterar: "))
                novo_nome_diretor = input("digite o novo nome do diretor:")
                novo_telefone_diretor = int(input("digite o novo telefone do diretor:"))
                novo_cpf_diretor = int(input("digite o novo cpf do diretor:"))
                novo_endereco_diretor = input("digite o novo endereco do diretor:")
                banco = 'teste_loja.db'
                atualizar_diretores(id_diretor, novo_nome_diretor, novo_telefone_diretor, novo_cpf_diretor, novo_endereco_diretor, banco)

            elif opcao == 4:
                id_diretor = int(input("Digite o ID do diretor que deseja excluir: "))
                banco = 'teste_loja.db'
                excluir_diretores(id_diretor , banco)

    except ValueError:
        print("Erro: digite apenas numeros!")
    finally:
        print("------------------------------------------------")


#funcionarios
def cadastrar_funcionarios(nome_funcionario, telefone_funcionario , cpf_funcionario , endereco_funcionario , id_diretor, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute(f'''INSERT INTO funcionarios
                        (nome_funcionario, telefone_funcionario , cpf_funcionario , endereco_funcionario , id_diretor )
                        VALUES ('{nome_funcionario}', '{telefone_funcionario}', '{cpf_funcionario}', '{endereco_funcionario}', '{id_diretor}')''')

        conexao.commit()
        conexao.close()

        return("funcionario cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar funcionario" , erro)


def listar_funcionarios(banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM funcionarios")
        funcionarios = cursor.fetchall()

        conexao.close()

        print("\n--- FUNCIONARIOS ---")

        if not funcionarios:
            print("Nenhum funcionario cadastrado.")
        else:
            for funcionario in funcionarios:
                print(
                    f"ID: {funcionario[0]} | "
                    f"Nome: {funcionario[1]} | "
                    f"telefone: {funcionario[2]} | "
                    f"cpf: {funcionario[3]} | "
                    f"endereco: {funcionario[4]} |"
                    f"diretor relacionado: {funcionario[5]} |"
                )

    except sqlite3.Error as erro:
        print(f"Erro ao listar funcionarios" , erro)

def atualizar_funcionarios(id_funcionario, novo_nome_funcionario, novo_telefone_funcionario, novo_cpf_funcionario, novo_endereco_funcionario, novo_diretor_vinculado, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''
        UPDATE funcionarios
        SET nome_funcionario = '{novo_nome_funcionario}',
            telefone_funcionario = '{novo_telefone_funcionario}',
            cpf_funcionario = '{novo_cpf_funcionario}',
            endereco_funcionario = '{novo_endereco_funcionario}'
            id_diretor = '{novo_diretor_vinculado}'
        WHERE id_funcionario = {id_funcionario}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            return("funcionario atualizado com sucesso!")
        else:
            return("Nenhum funcionario foi encontrado com esse ID!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!", erro)

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()

def excluir_funcionarios(id_funcionario , banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''DELETE FROM funcionarios WHERE id_funcionario = {id_funcionario}'''

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            return "funcionario excluído com sucesso!"
        else:
            return "Nenhum funcionario foi encontrado com esse ID."

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!", erro)

    finally:
        conexao.close()

def menu_funcionarios():
    try:
        opcao = 0

        while opcao != 5:
            print("---------------------------------------------")
            print("1- cadastrar funcionario ")
            print("2- listar funcionario")
            print("3- atualizar funcionario")
            print("4- excluir funcionario")
            print("5- sair")
            opcao = int(input("escolha uma das opcoes a cima: "))
            print("---------------------------------------------")

            if opcao == 1:
                nome_funcionario = input("digite o nome do funcionario:")
                telefone_funcionario = int(input("digite o telefone do funcionario:"))
                cpf_funcionario = int(input("digite o cpf do funcionario:"))
                endereco_funcionario = input("digite o endereco do funcionario:")
                id_diretor = int(input("digite o id do diretor que esta vinculado:"))
                banco = 'teste_loja.db'
                cadastrar_funcionarios(nome_funcionario, telefone_funcionario, cpf_funcionario , endereco_funcionario , id_diretor,  banco)

            elif opcao == 2:
                banco = 'teste_loja.db'
                listar_funcionarios(banco)
            
            elif opcao == 3:
                id_funcionario = int(input("Digite o ID do funcionario que deseja alterar: "))
                novo_nome_funcionario = input("digite o novo nome do funcionario:")
                novo_telefone_funcionario = int(input("digite o novo telefone do funcionario:"))
                novo_cpf_funcionario= int(input("digite o novo cpf do funcionario:"))
                novo_endereco_funcionario = input("digite o novo endereco do funcionario:")
                novo_diretor_vinculado = int(input("digite o novo diretor vinculado:"))
                banco = 'teste_loja.db'
                atualizar_funcionarios(id_funcionario, novo_nome_funcionario, novo_telefone_funcionario, novo_cpf_funcionario, novo_endereco_funcionario, novo_diretor_vinculado, banco)

            elif opcao == 4:
                id_funcionario = int(input("Digite o ID do funcionario que deseja excluir: "))
                banco = 'teste_loja.db'
                excluir_funcionarios(id_funcionario , banco)

    except ValueError:
        print("Erro: digite apenas numeros!")
    finally:
        print("------------------------------------------------")


#clientes


menu_diretores()
menu_funcionarios()

