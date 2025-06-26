
# 1. Operadores Aritméticos

a = 10
b = 3

print("Soma:", a + b)  # Adição
print("Subtração:", a - b)  # Subtração
print("Multiplicação:", a * b)  # Multiplicação
print("Divisão:", a / b)  # Divisão
print("Divisão Inteira:", a // b)  # Divisão inteira
print("Módulo:", a % b)  # Módulo
print("Exponenciação:", a ** b)  # Exponenciação

# 2. Operadores de Atribuição
x = 5
x += 2  # x = x + 2
print("Atribuição com adição:", x)  # x agora é 7
x -= 3  # x = x - 3
print("Atribuição com subtração:", x)  # x agora é 4
x *= 2  # x = x * 2
print("Atribuição com multiplicação:", x)  # x agora é 8
x /= 4  # x = x / 4
print("Atribuição com divisão:", x)  # x agora é 2.0
x //= 2  # x = x // 2
print("Atribuição com divisão inteira:", x)  # x agora é 1.0
x %= 1  # x = x % 1
print("Atribuição com módulo:", x)  # x agora é 0.0
x **= 3  # x = x ** 3
print("Atribuição com exponenciação:", x)  # x agora é 0.0

# 3. Operadores de Comparação
a = 10
b = 20
print("Igual:", a == b)  # Igualdade
print("Diferente:", a != b)  # Diferença
print("Maior que:", a > b)  # Maior que
print("Menor que:", a < b)  # Menor que
print("Maior ou igual:", a >= b)  # Maior ou igual
print("Menor ou igual:", a <= b)  # Menor ou igual

# 4. Operadores Lógicos
x = True
y = False
print("E lógico:", x and y)  # E lógico
print("Ou lógico:", x or y)  # Ou lógico
print("Não lógico:", not x)  # Não lógico

# 5. Operadores de Identidade
a = [1, 2, 3]
b = a
c = a.copy()  # Cria uma cópia de 'a'
print("a é b:", a is b)  # Verifica se 'a' e 'b' são o mesmo objeto
print("a é c:", a is c)  # Verifica se 'a' e 'c' são o mesmo objeto
# Verifica se 'a' e 'c' são objetos diferentes
print("a é diferente de c:", a is not c)

# 6. Operadores de Membro
lista = [1, 2, 3, 4, 5]
print("1 está na lista:", 1 in lista)  # Verifica se 1 está na lista
# Verifica se 6 não está na lista
print("6 não está na lista:", 6 not in lista)

# 7. Operadores Bit a Bit
a = 5  # 0101 em binário
b = 3  # 0011 em binário
print("E bit a bit:", a & b)  # AND bit a bit (0101 & 0011 = 0001)
print("Ou bit a bit:", a | b)  # OR bit a bit (0101 | 0011 = 0111)
print("XOR bit a bit:", a ^ b)  # XOR bit a bit (0101 ^ 0011 = 0110)
# Desloca bits para a esquerda (0101 << 1 = 1010)
print("Deslocamento à esquerda:", a << 1)
# Desloca bits para a direita (0101 >> 1 = 0010)
print("Deslocamento à direita:", a >> 1)

# 8. Operadores de Associação


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

        def __str__(self):
            return f"Pessoa(nome={self.nome})"
