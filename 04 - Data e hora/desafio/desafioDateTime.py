'''
[media pointer="file-service://file-LcEixfDj3eHmWT6PWJ7BYN"]
Com os novos conhecimentos adquiridos sobre data e hora, você foi encarregado de implementar as seguintes funcionalidades no sisetma:
Estabelecer um limite de 10 transações diárias para uma conta
Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.
Mostre no extrato, a data e hora de todas as transações.

Funcionalidades a implementar
Limite de 10 transações por dia por conta

Bloquear novas transações após o limite diário

Registrar data/hora de cada transação

Mostrar extrato com data e hora das transações

'''


# Modificar a classe Historico para armazenar data/hora
from datetime import datetime


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "transacao": transacao,
            "data_hora": datetime.now()
        })

    def gerar_transacoes(self, tipo=None):
        for item in self.transacoes:
            transacao = item["transacao"]
            if tipo is None or isinstance(transacao, tipo):
                yield item


# Decorator para logar transações (pode ser expandido conforme necessário)
def log_transacao(func):
    def wrapper(self, *args, **kwargs):
        resultado = func(self, *args, **kwargs)
        # Aqui você pode adicionar logs adicionais se desejar
        return resultado
    return wrapper

# Adicionar verificação de limite diário de transações na classe Conta


class Conta:
    LIMITE_TRANSACOES_DIARIAS = 10

    def __init__(self, cliente, numero):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def _transacoes_hoje(self):
        hoje = datetime.now().date()
        return sum(1 for item in self.historico.transacoes if item["data_hora"].date() == hoje)

    def _pode_transacionar(self):
        return self._transacoes_hoje() < self.LIMITE_TRANSACOES_DIARIAS

    @log_transacao
    def sacar(self, valor):
        if not self._pode_transacionar():
            print("Limite de transações diárias atingido.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        self.historico.adicionar_transacao(Conta.Saque(valor))
        return True

    @log_transacao
    def depositar(self, valor):
        if not self._pode_transacionar():
            print("Limite de transações diárias atingido.")
            return False
        if valor <= 0:
            print("Valor inválido.")
            return False
        self.saldo += valor
        self.historico.adicionar_transacao(Conta.Deposito(valor))
        return True

    # Definição das classes Saque e Deposito
    class Saque:
        def __init__(self, valor):
            self.valor = valor

        def __repr__(self):
            return f"Saque de R${self.valor:.2f}"

    class Deposito:
        def __init__(self, valor):
            self.valor = valor

        def __repr__(self):
            return f"Depósito de R${self.valor:.2f}"

def exibir_extrato(conta):
    print(f"\n📄 Extrato da Conta {conta.numero}:")
    for item in conta.historico.gerar_transacoes():
        transacao = item["transacao"]
        data = item["data_hora"].strftime('%Y-%m-%d %H:%M:%S')
        print(f"{data} - {type(transacao).__name__}: R$ {transacao.valor}")

# Definir a classe PessoaFisica
from datetime import date

class PessoaFisica:
    def __init__(self, cpf, nome, nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        if isinstance(transacao, Conta.Deposito):
            conta.depositar(transacao.valor)
        elif isinstance(transacao, Conta.Saque):
            conta.sacar(transacao.valor)

# Criar cliente e conta
cliente = PessoaFisica("000.000.000-00", "Carlos", date(1988, 3, 15), "Av. Central")
conta = Conta(cliente, 777)
cliente.adicionar_conta(conta)

# Fazer 11 depósitos para testar o limite diário
for i in range(11):
    print(f"\nTransação {i+1}:")
    cliente.realizar_transacao(conta, Conta.Deposito(50))

# Mostrar extrato
exibir_extrato(conta)


# Criar cliente e conta
cliente = PessoaFisica("000.000.000-00", "Carlos", date(1988, 3, 15), "Av. Central")
conta = Conta(cliente, 777)
cliente.adicionar_conta(conta)

# Fazer 11 depósitos para testar o limite diário
for i in range(11):
    print(f"\nTransação {i+1}:")
    cliente.realizar_transacao(conta, Conta.Deposito(50))

# Mostrar extrato
exibir_extrato(conta)
