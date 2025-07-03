"""
Uma pousada deseja automatizar seu sistema de reservas. Crie uma função que receba 
uma lista de quartos disponíveis e uma lista de reservas solicitadas. 
A função deve verificar quais reservas podem ser aceitas e quais devem ser recusadas 
por falta de disponibilidade.

Entrada
Uma lista contendo os números dos quartos disponíveis.
Uma lista contendo os números dos quartos solicitados pelos clientes.
Saída
Uma mensagem informando quais reservas foram confirmadas e quais foram recusadas.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.
"""

def processar_reservas(quartos_disponiveis, reservas_solicitadas):
    #Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, quartos_disponiveis))
    #Entrada das reservas solicitadas
    reservas_disponiveis = list(map(int, reservas_solicitadas))


    # Lista para armazenar reservas confirmadas e recusadas
    reservas_confirmadas = []
    reservas_recusadas = []

    # Processa cada reserva solicitada
    for reserva in reservas_disponiveis:
        if reserva in quartos_disponiveis:
            reservas_confirmadas.append(reserva)
            quartos_disponiveis.remove(reserva) # Remove o quarto da lista de disponíveis
        else:
            reservas_recusadas.append(reserva)

    # Exibe as reservas confirmadas e recusadas
    print("Reservas confirmadas:", reservas_confirmadas)
    print("Reservas recusadas:", reservas_recusadas)

# Chamada da função com exemplos de entrada
quartos_disponiveis = [101, 102, 103, 104, 105]
reservas_solicitadas = [102, 103, 106, 101, 104, 107]
processar_reservas(quartos_disponiveis, reservas_solicitadas)
