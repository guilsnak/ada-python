from utils import valida_cpf, valida_rg, valida_data_nascimento, valida_busca_cep
from banco_dados import * 


def menu_cliente():
    validador_menu = True
    lista_cliente = [] ##variavel de escopo global, pois esta fora do while
    
    while validador_menu:
        print("Menu Cliente"
              "\n1 - Cadastrar Cliente"
              "\n2 - Alterar Cliente"
              "\n3 - Buscar Cliente"
              "\n4 - Deletar Cliente"
              "\n5 - Listar Clientes"
              "\n6 - Voltar ao menu anterior")
        opcao = int(input("Digite a opção desejada: "))
        if opcao ==1:
            cliente_dicionario = {
                "Nome": input("Digite o Nome: "),
                "CPF": valida_cpf(input ("Digite o CPF: ")),
                "RG": valida_rg(input ("Digite o RG: ")),
                "Nascimento": valida_data_nascimento(),
                "Endereco": valida_busca_cep(input("Digite o CEP:")),
                "Numero": input("Digite o número da casa")

            }
            lista_cliente.append(cliente_dicionario)
            print(lista_cliente)
        elif opcao ==2:
            try: 
                cpf = (valida_cpf(input ("Digite o CPF do cliente que pretende atualizar: ")))
                update_banco_dados(cpf)
            except:
                print("Erro ao cadastrar o cliente. Por favor, tente novamente. ")         
        
        elif opcao ==3:
            try:
                cpf = (valida_cpf(input("Digite o CPF do cliente que deseja consultar: ")))
                select_banco_dados_cpf(cpf)
            except:
                print("Erro ao consultar o cliente. Tente novamente mais tarde.")
           
        elif opcao ==4:
            try:
                cpf = (valida_cpf(input("Digite o CPF do cliente que deseja deletar: ")))
                delete_banco_dados(cpf)
            except:
                print("Erro ao deletar o cliente da base de dados. Tente novamente mais tarde.")
            
        elif opcao ==5:
            try:
                select_banco_dados()
            except: 
                print("Erro ao listar todos os clientes. Tente novamente mais tarde.")
        
        elif opcao ==6:
            print("Encerrando a execução do programa.")
            validador_menu = False
        else:
            print("Opção inválida.")

        # Ctrl + Shift + Alt e dai seleciona seta pra cima e pra baixo para alterar várias linhas de código de uma vez. Serve para comentar várias linhas de uma única vez.

        #viacep.com.br (API)
