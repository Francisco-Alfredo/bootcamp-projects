#Otimiza o sistema de contas bancárias, com funcionalidades de depósito, saque, extrato, criação de usuários e contas, e listagem de contas usando funções para modularizar o código.
# O programa deve ter um menu interativo que permita ao usuário escolher a ação desejada, e deve ser capaz de lidar com erros de entrada de forma adequada.
#Deve ter também uma função main():

def menu():
    menu = """\n
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair
    ==========================
    """
    print(menu)
    return input("Escolha uma opção: ").lower().strip()

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios, nome, cpf, data_nascimento):
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("\n@@@ Já existe um usuário com esse CPF. @@@")
        return

    usuarios.append({
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento
    })
    print("\n=== Usuário criado com sucesso! ===")

def criar_conta(usuarios, contas, numero_conta, agencia, cpf):
    if any(conta['numero'] == numero_conta for conta in contas):
        print("\n@@@ Já existe uma conta com esse número. @@@")
        return

    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    if not usuario:
        print("\n@@@ Usuário não encontrado. @@@")
        return

    contas.append({
        'numero': numero_conta,
        'agencia': agencia,
        'usuario': usuario
    })
    print("\n=== Conta criada com sucesso! ===")