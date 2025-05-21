#
# Aula Comentarios
#

"""
DocString
E escrever o que eu
quiser
asdfasdfd
"""
''' Usar para escrever suas notas '''
# Permite escrever um comentário
print(123)  # Na frente
# Abaixo
print(456)

#
#Aulas Print
#

# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="", end='#')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""
print(1234)
# Aspas simples
print('Leandro Benitti')
print(1, 'Leandro "Benitti"')
# Aspas duplas
print("Leandro Benitti")
print(2, "Leandro 'Benitti'")
# Escape
print("Leandro \"Benitti\"")
# r
print(r"Leandro \"Benitti\"")

print()
#
#Aulas Tipo de dados
#

# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.
# print(11) # int
# print(-11) # int
# print(0)
# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
# print(1.1, 10.11)
# print(0.0, -1.5)
# A função type mostra o tipo que o Python
# inferiu ao valor.
print(type('Leandro'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))

# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que
# questiona se um valor é igual a outro
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))

print()
#
#Aulas Conversao
#

# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')

print()
#
#Aulas Introdução de Variaveis 
#

# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão
# nome_completo = 'Luiz Otávio Miranda'
# soma_dois_mais_dois = 2 + 2
# int_um = bool('1')
# print(int_um, type(int_um))
# print(nome_completo, soma_dois_mais_dois)
nome = 'Leandro'
idade = 29
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)

print()
#
#Aulas Aritimetica
#

adicao = 10 + 10
print('Adição', adicao)
subtracao = 10 - 5
print('Subtração', subtracao)
multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)
divisao = 10 / 3  # float
print('Divisão', divisao)
divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)
exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)
modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print()
#
#Aulas Concatenação(+) e repetição(*)
#

concatenacao = 'Leandro' + ' ' + 'Benitti'
print(concatenacao)
a_dez_vezes = 'A' * 10
tres_vezes_leandro = 3 * 'Leandro'
print(a_dez_vezes)
print(tres_vezes_leandro)

print()
#
#Aulas Precedencia
#

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

print()
#
#Aulas f-strings
#

nome = 'Leandro Benitti'
altura = 1.64
peso = 99
imc = peso / altura ** 2
"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

print()
#
#Aulas Formato
#

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)

print()
#
#Aulas Coleta de dados
#

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
print(f'A soma dos números é: {int_numero_1 + int_numero_2}')

print()
#
#Aulas if elif else
#

# if / elif      / else
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')

print()
#
#Aulas 
#