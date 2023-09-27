#linha_notafiscal = 'Pão de queijo R$2.00'
#print(linha_notafiscal.split(' R$')[1])

#def compra(preco,quantidade,saldo):
    #saldo = saldo -(preco*quantidade)
    #return saldo.preco_produto = 10.90
    #meusaldo = 100.00
    #quantidade_produto = 2
    #saldofinal = compra(preco_produto,quantidade_produto,meusaldo).print(saldofinal)

#num = '+55 (11) 9788-7888'
#print(num[0:4])
#print(num[1:3])

#print(num.split('+55 ', '(11)'))
#open(,a)

#string1 = 'Ola'
#string2 = 'ola'
#resultado = string2 > string1
#print(resultado)

#import argparse
#parser = argparse.ArgumentParser(description='Process some integers.')
#parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
#parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max,help='sum the integers (default: find the max)')
#args = parser.parse_args().print(args.accumulate(args.integers))

import sys
def compra(preco,quantidade,saldo):
    saldo = saldo -(preco*quantidade)
    return saldo
preco_produto = sys.argv[0]
meusaldo = sys.argv[1]
quantidade_produto = sys.argv[2]
saldofinal = compra(preco_produto,quantidade_produto,meusaldo)
print(saldofinal)
        







