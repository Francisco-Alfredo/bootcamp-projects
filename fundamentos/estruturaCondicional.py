
#O que são estruturas condicionais?
# Estruturas condicionais são blocos de código que permitem executar diferentes ações com base em condições específicas.
# Elas são fundamentais para a lógica de programação, permitindo que o programa tome decisões e execute diferentes caminhos de código.
# Estruturas condicionais em Python

x = 10
if x > 0:
    print("x é positivo")

# A estrutura condicional if é usada para verificar se uma condição é verdadeira. Se for, o bloco de código indentado será executado.
# Exemplo de estrutura condicional if-else

if x > 0:
    print("x é positivo")
else:
    print("x é negativo ou zero")

# A estrutura if-else permite executar um bloco de código se a condição for verdadeira e outro bloco se for falsa.
# Exemplo de estrutura condicional if-elif-else

if x > 0:
    print("x é positivo")
    if x > 5:
        print("x é maior que 5")
    else:
        print("x é menor ou igual a 5")

# A estrutura if-elif-else permite verificar múltiplas condições. Se a primeira condição for falsa, a próxima será verificada, e assim por diante.
# Exemplo de estrutura condicional aninhada

if x > 0:
    print("x é positivo")
elif x < 0:
    print("x é negativo")
else:
    print("x é zero")

# Estruturas condicionais aninhadas permitem que você coloque uma estrutura condicional dentro de outra, criando uma hierarquia de decisões.
# Exemplo de uso de operadores lógicos em estruturas condicionais
if x > 0 and x < 10:
    print("x está entre 0 e 10")

# Operadores lógicos como and, or e not podem ser usados para combinar condições em estruturas condicionais.
# Exemplo de uso de operadores de comparação
if x >= 0 and x <= 10:
    print("x está entre 0 e 10, inclusive")

# Operadores de comparação como >, <, >=, <=, == e != são usados para comparar valores em estruturas condicionais.
# Exemplo de uso de operadores de identidade
lista = [1, 2, 3]
if x is not None:
    print("x não é None")

# O operador is é usado para verificar se duas variáveis referenciam o mesmo objeto na memória.
# Exemplo de uso de operadores de membro
if 1 in lista:
    print("1 está na lista")

# O operador in é usado para verificar se um valor está presente em uma coleção, como uma lista ou um dicionário.
# Exemplo de uso de operadores bit a bit

a = 5  # 0101 em binário
b = 3  # 0011 em binário
if a & b:  # AND bit a bit
    print("O resultado do AND bit a bit é:", a & b)

# Operadores bit a bit como &, |, ^, ~, << e >> são usados para realizar operações em bits individuais de números inteiros.
# Exemplo de uso de operadores ternários
resultado = "Positivo" if x > 0 else "Negativo ou zero"
print("Resultado:", resultado)

# O operador ternário é uma forma concisa de escrever uma estrutura condicional simples, retornando um valor com base em uma condição.
# Exemplo de uso de estruturas condicionais com listas

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")

# Estruturas condicionais também podem ser usadas em loops, permitindo que você execute ações diferentes com base em condições dentro de uma iteração.
# Exemplo de uso de estruturas condicionais com dicionários

pessoa = {"nome": "João", "idade": 30}
if pessoa["idade"] >= 18:
    print(f"{pessoa['nome']} é maior de idade")

# Estruturas condicionais podem ser usadas para verificar condições em dicionários, permitindo que você tome decisões com base nos valores das chaves.
# Exemplo de uso de estruturas condicionais com funções
def verificar_numero(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Zero"
print(verificar_numero(x))

# Estruturas condicionais também podem ser usadas dentro de funções para retornar valores com base em condições específicas.
# Exemplo de uso de estruturas condicionais com exceções
numeros = [1, 2, 3, 4, 5]
pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", pares)

# Estruturas condicionais podem ser usadas para tratar exceções, permitindo que você lide com erros de forma controlada e evite que o programa falhe inesperadamente.
# Exemplo de uso de estruturas condicionais com listas por compreensão
try:
    resultado = 10 / x
except ZeroDivisionError:
    print("Erro: Divisão por zero")


