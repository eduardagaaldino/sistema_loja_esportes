import sqlite3

def cadastrar_produtos(nome_produto, marca_produto, preco_produto, estoque, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute(f'''INSERT INTO diretores
                        (nome_produto, marca_produto, preco_produto, estoque )
                        VALUES ('{nome_produto}', '{marca_produto}', '{preco_produto}', '{estoque}')''')

        conexao.commit()
        conexao.close()

        return("produto cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar produto" , erro)


def listar_produtos(banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        conexao.close()

        print("\n--- PRODUTOS ---")

        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(
                    f"ID: {produto[0]} | "
                    f"Nome: {produto[1]} | "
                    f"marca: {produto[2]} | "
                    f"preco: {produto[3]} | "
                    f"estoque: {produto[4]} |"
                )

    except sqlite3.Error as erro:
        print(f"Erro ao listar produtos" , erro)


def atualizar_produtos(id_produto, novo_nome_produto, nova_marca_produto, novo_preco_produto, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''
        UPDATE produtos
        SET nome_produto = '{novo_nome_produto}',
            marca_produto = '{nova_marca_produto}',
            preco_produto = '{novo_preco_produto}',
        WHERE id_produto = {id_produto}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            return("produto atualizado com sucesso!")
        else:
            return("Nenhuma produto foi encontrado com esse ID!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!", erro)

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()

def atualizar_estoque(id_produto, novo_estoque, banco, operacao):  #criar operacao entrada e saida
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''
        UPDATE produtos
            estoque = '{novo_estoque}'
        WHERE id_produto = {id_produto}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            return("produto atualizado com sucesso!")
        else:
            return("Nenhuma produto foi encontrado com esse ID!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!", erro)

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:


def excluir_diretores(id_produto, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''DELETE FROM produtos WHERE id_produto = {id_produto}'''

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            return "produto excluído com sucesso!"
        else:
            return "Nenhum produtor foi encontrado com esse ID."

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!", erro)

    finally:
        conexao.close()

# terminar menu
def menu_produtos():
    try:
        opcao = 0
        estoque = 0

        while opcao != 5:
            print("---------------------------------------------")
            print("1- cadastrar produto")
            print("2- listar produto ")
            print("3- atualizar produto ")
            print("4- atualizar estoque ")
            print("5- excluir produto ")
            print("6- sair")
            opcao = int(input("escolha uma das opcoes a cima: "))
            print("---------------------------------------------")

            if opcao == 1:
                nome_produto = input("digite o nome do produto: ")
                marca_produto = int(input("digite a marca do produto:"))
                preco_produto = float(input("digite o preco do produto: R$"))
                estoque = int(input("qual quantidade a em estoque?: "))
                banco = 'teste_loja.db'
                cadastrar_produtos(nome_produto, marca_produto, preco_produto, estoque, banco)

            elif opcao == 2:
                banco = 'teste_loja.db'
                listar_produtos(banco)
            
            elif opcao == 3:
                id_produto = int(input("Digite o ID do produto que produto alterar: "))
                novo_nome_produto = input("digite o novo nome do produto:")
                nova nova_marca_produto = int(input("digite a nova marca do produto:"))
                novo_preco_produto = int(input("digite o novo preco do produto:"))
                banco = 'teste_loja.db'
                atualizar_produtos(id_produto, novo_nome_produto, nova_marca_produto, novo_preco_produto, banco)

            elif opcao == 4:
                id_produto = int(input("Digite o ID do produto que deseja alterar o estoque: "))
                novo_estoque = int(input("digite o novo estoque: "))
                atualizar_estoque(id_produto, novo_estoque, banco)

            elif opcao == 4:
                id_produto = int(input("Digite o ID do produto que deseja excluir: "))
                banco = 'teste_loja.db'
                excluir_produto(id_produto, banco)

    except ValueError:
        print("Erro: digite apenas numeros!")
    finally:
        print("------------------------------------------------")

menu_produtos()