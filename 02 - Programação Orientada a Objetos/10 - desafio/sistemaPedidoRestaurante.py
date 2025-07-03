'''
Descrição
Crie uma classe Pedido que represente um pedido em um restaurante, contendo os itens pedidos e um método para calcular o valor total da conta.

Entrada
Lista de itens e seus respectivos preços.
Saída
O valor total da conta.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.
'''

class Pedido:
    def __init__(self):
        self.itens = []  
    
    # Método para adicionar um item (preço) à lista
    def adicionar_item(self, preco):
        self.itens.append(preco)

    # Método para calcular o total da conta
    def calcular_total(self):
        return sum(self.itens)


quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    pedido.adicionar_item(float(preco))  # Chamada correta do método

# Exibe o total com duas casas decimais
print(f"{pedido.calcular_total():.2f}")
