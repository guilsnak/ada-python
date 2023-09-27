import pyodbc
from utils import *
# O código aqui tá orientado a função.

def retornar_cursor_banco_dados():
    connection = pyodbc.connect(retorna_string_conexao_banco_dados())
    cursor = connection.cursor() # cursor da IDE lá do banco de dados para inserção / manipulação no banco de dados
    return cursor, connection

def retorna_string_conexao_banco_dados():
    return(
        "DRIVER={SQL Server};"
        "SERVER=HOESQL633;"
        "DATABASE=SkillUp_GFIRMIN;"
        "Trusted_Connection=yes;"
    )

def select_banco_dados():
    cursor, connection = retornar_cursor_banco_dados()
    cursor.execute("select * from cliente") # dá pra usar a tabela usuario do mesmo DB
    clientes = cursor.fetchall() # retorna uma lista da consulta ao banco de dados.
    print(clientes)
    connection.commit()

def insert_banco_dados(cliente):
    cursor, connection = retornar_cursor_banco_dados()
    insert_query = '''
    INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, logradouro, complemento, bairro, cidade, estado, numero_residencia)
    VALUES (?, ?, ?, ? , ?, ?, ?, ?, ?, ?, ?);
    '''
    values = (cliente['nome'], cliente['cpf'], cliente['rg'], cliente['data_nascimento'], cliente['cep'], cliente['logradouro'], cliente['complemento'], cliente['bairro'], cliente['cidade'], cliente['estado'], cliente['numero_residencia'],)
    cursor.execute(insert_query,values)
    connection.commit()

    
def delete_banco_dados(cpf):
    cursor, connection = retornar_cursor_banco_dados()
    delete_query = "DELETE FROM cliente WHERE cpf = '" + cpf + "';"
    cursor.execute(delete_query)
    connection.commit()

def update_banco_dados(cpf):
    cursor, connection = retornar_cursor_banco_dados()
    
    atualiza_cliente = {
        "nome": input("Digite o Nome: "),
        "cpf": (cpf),        
        "rg": valida_rg(input ("Digite o RG: ")),
        "data_nascimento": valida_data_nascimento(),
        "cep": input("Digite o CEP:"),
        "numero_residencia": input("Digite o número da casa")
        }

    update_query = "UPDATE cliente SET nome = ?, cpf = ?, rg = ?, data_nascimento = ?, cep = ?, numero_residencia = ? WHERE cpf = '" + cpf + "';"
    
     
    set = (atualiza_cliente['nome'], atualiza_cliente['cpf'], atualiza_cliente['rg'], atualiza_cliente['data_nascimento'], atualiza_cliente['cep'],atualiza_cliente['numero_residencia'])
    cursor.execute(update_query, set)
    print("Esses serão os dados a serem atualizados: ", set)
    connection.commit()

def select_banco_dados_cpf(cpf):
    cursor, connection = retornar_cursor_banco_dados()
    select_query = "select * from cliente WHERE cpf = '" + cpf + "';"
    cursor.execute(select_query) 
    clientes = cursor.fetchall() 
    print(clientes)
    connection.commit()    


#cliente = {"nome": "Rodrigo Nestor", "cpf": "590834490", "rg": "092225402", "data_nascimento" : "1960-02-01", "cep" : "80050-200", "numero_residencia" : "160" }




#insert_banco_dados()
#select_banco_dados()
#delete_banco_dados()
#select_banco_dados()
#update_banco_dados(cliente["cpf"])
#update_banco_dados()

select_banco_dados_cpf('06648566914')