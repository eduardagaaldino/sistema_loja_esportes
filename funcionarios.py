import sqlite3

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
            id_diretor = '{novo_diretor_vinculado}
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
                novo_diretor_vinculado = int(input("digite o novo funcionario vinculado:"))
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

menu_funcionarios()