##Descrição
#Uma empresa quer criar um organizador de eventos que divida os 
#participantes em grupos de acordo com o tema escolhido.
#Entrada
#Lista de participantes e o tema escolhido por cada um.
#Saída
#Dicionário agrupando os participantes por tema.

eventos = []

def adicionar_participante(nome, tema):
    """Adiciona um participante à lista de eventos."""
    eventos.append({'nome': nome, 'tema': tema})


def organizar_eventos():
    """Organiza os participantes por tema."""
    organizados = {}
    for participante in eventos:
        tema = participante['tema']
        if tema not in organizados:
            organizados[tema] = []
        organizados[tema].append(participante['nome'])
    return organizados

def exibir_eventos(organizacao):
    """Exibe os eventos organizados."""
    for tema, participantes in organizacao.items():
        print(f'Tema: {tema}')
        for participante in participantes:
            print(f' - {participante}')
        print()  # Linha em branco para separar temas

# Exemplo de uso
adicionar_participante('Alice', 'Tecnologia')
adicionar_participante('Bob', 'Saúde')
adicionar_participante('Charlie', 'Tecnologia')
adicionar_participante('Diana', 'Saúde')
adicionar_participante('Eve', 'Educação')

organizacao = organizar_eventos()
exibir_eventos(organizacao)



