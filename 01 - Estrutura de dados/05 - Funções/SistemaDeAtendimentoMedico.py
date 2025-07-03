"""
  Descrição
Uma clínica médica quer automatizar seu sistema de atendimento. 
Crie uma função que organize os pacientes em ordem de prioridade com base na idade e na urgência do caso.

📌 Critérios de Prioridade:

Pacientes acima de 60 anos têm prioridade.
Pacientes que apresentam a palavra "urgente" na ficha têm prioridade máxima.
Os demais pacientes são atendidos por ordem de chegada.

Entrada
Um número inteiro n, representando a quantidade de pacientes.
n linhas seguintes, cada uma contendo os dados de um paciente no formato: nome, idade, status
nome: string representando o nome do paciente.
idade: número inteiro representando a idade do paciente.
status: string que pode ser "urgente" ou "normal".
Saída
A saída deve exibir a lista dos pacientes ordenada de acordo com as regras de prioridade, 
no formato: Ordem de Atendimento: nome1, nome2, nome3, ..
"""                                                                                                              

# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def prioridade(paciente):
    nome, idade, status = paciente
    if status == "urgente":
        return (0, idade)  # Urgentes têm prioridade máxima
    elif idade >= 60:
        return (1, idade)  # Idosos têm prioridade média
    else:
        return (2, idade)  # Demais pacientes têm prioridade mínima


# TODO: Exiba a ordem de atendimento com título e vírgulas:
print(pacientes.sort(key=prioridade))

print("Ordem de atendimento:")
for paciente in sorted(pacientes, key=prioridade):
    nome, idade, status = paciente
    print(f"{nome}, {idade}, {status}")