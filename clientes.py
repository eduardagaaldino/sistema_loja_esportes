import sqlite3

def cadastrar_clientes(nome_cliente, telefone_cliente , cpf_cliente , endereco_cliente , id_funcionario, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute(f'''INSERT INTO clientes
                        (nome_cliente, telefone_cliente , cpf_cliente , endereco_cliente , id_funcionario )
                        VALUES ('{nome_cliente}', '{telefone_cliente}', '{cpf_cliente}', '{endereco_cliente}', '{id_funcionario}')''')

        conexao.commit()
        conexao.close()

        return("cliente cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar cliente" , erro)


def listar_clientes(banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()

        conexao.close()

        print("\n--- CLIENTES ---")

        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(
                    f"ID: {cliente[0]} | "
                    f"Nome: {cliente[1]} | "
                    f"telefone: {cliente[2]} | "
                    f"cpf: {cliente[3]} | "
                    f"endereco: {cliente[4]} |"
                    f"funcionarios relacionado: {cliente[5]} |"
                )

    except sqlite3.Error as erro:
        print(f"Erro ao listar cliente" , erro)

def atualizar_clientes(id_cliente, novo_nome_cliente, novo_telefone_cliente, novo_cpf_cliente, novo_endereco_cliente, novo_funcionario_vinculado, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''
        UPDATE clientes
        SET nome_cliente = '{novo_nome_cliente}',
            telefone_cliente = '{novo_telefone_cliente}',
            cpf_cliente = '{novo_cpf_cliente}',
            endereco_cliente = '{novo_endereco_cliente}',
            id_funcionario = '{novo_funcionario_vinculado}'
        WHERE id_cliente = {id_cliente}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            return("cliente atualizado com sucesso!")
        else:
            return("Nenhum cliente foi encontrado com esse ID!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!", erro)

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()

def excluir_clientes(id_cliente , banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''DELETE FROM clientes WHERE id_cliente = {id_cliente}'''

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            return "cliente excluído com sucesso!"
        else:
            return "Nenhum cliente foi encontrado com esse ID."

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!", erro)

    finally:
        conexao.close()

def menu_clientes():
    try:
        opcao = 0

        while opcao != 5:
            print("---------------------------------------------")
            print("1- cadastrar cliente ")
            print("2- listar cliente")
            print("3- atualizar cliente")
            print("4- excluir cliente")
            print("5- sair")
            opcao = int(input("escolha uma das opcoes a cima: "))
            print("---------------------------------------------")

            if opcao == 1:
                nome_cliente = input("digite o nome do cliente:")
                telefone_cliente = int(input("digite o telefone do cliente:"))
                cpf_cliente = int(input("digite o cpf do cliente:"))
                endereco_cliente = input("digite o endereco do cliente:")
                id_funcionario = int(input("digite o id do funcionario que esta vinculado:"))
                banco = 'teste_loja.db'
                cadastrar_clientes(nome_cliente, telefone_cliente, cpf_cliente, endereco_cliente , id_funcionario,  banco)

            elif opcao == 2:
                banco = 'teste_loja.db'
                listar_clientes(banco)
            
            elif opcao == 3:
                id_cliente = int(input("Digite o ID do cliente que deseja alterar: "))
                novo_nome_cliente = input("digite o novo nome do cliente:")
                novo_telefone_cliente = int(input("digite o novo telefone do cliente:"))
                novo_cpf_cliente = int(input("digite o novo cpf do cliente:"))
                novo_endereco_cliente = input("digite o novo endereco do cliente:")
                novo_funcionario_vinculado = int(input("digite o novo funcionario vinculado:"))
                banco = 'teste_loja.db'
                atualizar_clientes(id_cliente, novo_nome_cliente, novo_telefone_cliente, novo_cpf_cliente, novo_endereco_cliente, novo_funcionario_vinculado, banco)
            elif opcao == 4:
                id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))
                banco = 'teste_loja.db'
                excluir_clientes(id_cliente , banco)

    except ValueError:
        print("Erro: digite apenas numeros!")
    finally:
        print("------------------------------------------------")

menu_clientes()