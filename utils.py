from datetime import datetime
from validate_docbr import CPF
import re #Regular Expressions
import requests 


def valida_cpf(cpf_input):
    cpf = CPF()
    
    while True:

        cpf_input = re.sub('[-.]', '', cpf_input) # método sub da biblioteca re que remove caracteres
        resultado = cpf.validate(cpf_input)
        if resultado:
            cpf_formatado = f'{cpf_input[:3]}.{cpf_input[3:6]}.{cpf_input[6:9]}-{cpf_input[9:]}' # I) conceito f strings (feature para manipular strings no python). Em python, uma string contem a mesma propriedade de listas, onde cada elemento da lista pode ser acessado separadamente.  II) intervalo aberto, ou seja, nao inclui o ultimo elemento da lista
            return cpf_formatado
        else:
            cpf_input = input("CPF inválido. Digite novamente: ")
            
        # formas de sair do laço: CONTINUE, BREAK, RETURN, ALTERACAO CONDICAO
        
    
    #validate-docbr
    #https://pypi.org/project/validate-docbr/
    
def valida_rg(rg_input):
    #formato esperado xx.xxx.xxx-x
    padrao_rg =  r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$' # emprego de regex no 'braço'. Sem importe de biblioteca específica.

    while True:
        rg_input = re.sub('[-.]','', rg_input)

        rg_input = f'{rg_input[:2]}.{rg_input[2:5]}.{rg_input[5:8]}-{rg_input[8:]}'


        if re.match(padrao_rg,rg_input):
            return rg_input
        else:
            rg_input = input("RG inválido. Digite novamente: ")



    
def valida_data_nascimento():
    
    while True:
        # o enquanto "verdadeiro" usado aqui não é específico a nenhuma variável. Ele será executado interminavelmente até atingir o return (da linha XX) na função.
        data_nascimento_input = input("Digite a data de nascimento.")        
        try:
            data_convertida = datetime.strptime(data_nascimento_input, '%d/%m/%Y').date()
            data_atual = datetime.now().date()

            if data_convertida < data_atual:
                return data_convertida.strftime('%d/%m/%Y') # formata para string a data
            else:
                print("Data inválida. Digite a data novamente.")
          
        except ValueError as e:
            print("Formato de data inválido. Você recebeu o erro: ", e , "Tente novamente." )


    
def valida_busca_cep(cep_input): 
    url = f'https://viacep.com.br/ws/{cep_input}/json'

    response = requests.get(url, verify= False) # a requests é uma biblioteca do Python para chamadas de API. A response recebe um dicionário de resposta da chamada.
    # print(response['cep']) # printa o valor da chave 'cep' do dicionário que retorna da API em formato json.

    if response.status_code == 200:
        data = response.json()

        endereco = {
            "CEP": data['cep'],
            "Logradouro": data['logradouro'],
            "Bairro": data['bairro'],
            "Cidade": data['localidade'],
            "Estado": data['uf'] 
        }
        return endereco



