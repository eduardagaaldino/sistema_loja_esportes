import sqlite3

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

menu_diretores()