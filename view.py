#importacao
import sqlite3 as lite

#conexao
con = lite.connect('dados.db')

#inserindo dados
def inserir_form():
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,dados)


atualiza_dados = ['carro', 'garagem', 'carro que comprei em 2000', 'Marca bmw', '27/08/2000', 'xxxxxx', 'c:imagens']
#atualizar dados 
def atualizar(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=? "
        cur.execute(query,i)



#deletar dados
def  deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE * FROM inventario WHERE id=?"
        cur.execute(query, deletar_dados)


#ver dados
def ver_form():
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

#ver dados individual
def ver_item(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)

    return ver_dados_individual