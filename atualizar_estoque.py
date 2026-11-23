
def atualizar_estoque(id_produto, quantidade, banco, operacao):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT estoque FROM produtos
            WHERE id_produto = ?
        """, (id_produto,))

        produto = cursor.fetchone()

        if produto is None:
            return "Produto não encontrado!"

        estoque_atual = produto[0]

        if quantidade <= 0:
            return "Digite uma quantidade válida!"

        if operacao == "entrada":
            novo_estoque = estoque_atual + quantidade

        elif operacao == "saida":
            if quantidade > estoque_atual:
                return "Estoque indisponível!"

            novo_estoque = estoque_atual - quantidade

        else:
            return "Operação inválida!"

        cursor.execute("""
            UPDATE produtos
            SET estoque = ?
            WHERE id_produto = ?
        """, (novo_estoque, id_produto))

        conexao.commit()

        return "Estoque atualizado com sucesso!"

    except sqlite3.Error as erro:
        return f"Erro no banco de dados: {erro}"

    finally:
        conexao.close()
