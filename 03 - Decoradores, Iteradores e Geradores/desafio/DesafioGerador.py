'''

Crie um gerador que permita iterar sobre as transações de uma conta e retorne,
uma a uma, as transações que foram realizadas.
Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos). 

'''




from abc import ABC, abstractmethod
from datetime import datetime, date
from functools import wraps

# --------------------- DECORADOR ---------------------
def log_transacao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tipo = func.__name__
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{data_hora}] Transação: {tipo}")
        return func(*args, **kwargs)
    return wrapper

# --------------------- CLASSES DE TRANSACOES ---------------------
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @log_transacao
    def registrar(self, conta):
        return conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @log_transacao
    def registrar(self, conta):
        return conta.sacar(self.valor)

# --------------------- HISTÓRICO ---------------------
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def gerar_transacoes(self, tipo=None):
        for transacao in self.transacoes:
            if tipo is None or isinstance(transacao, tipo):
                yield transacao

# --------------------- CLASSE CONTA ---------------------
class Conta:
    def __init__(self, cliente, numero):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def saldo_atual(self):
        return self.saldo

    @log_transacao
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        self.historico.adicionar_transacao(Saque(valor))
        return True

    @log_transacao
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False
        self.saldo += valor
        self.historico.adicionar_transacao(Deposito(valor))
        return True

    @classmethod
    @log_transacao
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

# --------------------- CONTA CORRENTE ---------------------
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500.0, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    @log_transacao
    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques excedido.")
            return False
        if valor > (self.saldo + self.limite):
            print("Limite insuficiente.")
            return False
        self.saldo -= valor
        self.saques_realizados += 1
        self.historico.adicionar_transacao(Saque(valor))
        return True

# --------------------- CLIENTE ---------------------
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    @log_transacao
    def realizar_transacao(self, conta, transacao):
        sucesso = transacao.registrar(conta)
        if sucesso:
            conta.historico.adicionar_transacao(transacao)

    @log_transacao
    def adicionar_conta(self, conta):
        self.contas.append(conta)

# --------------------- PESSOA FÍSICA ---------------------
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


# Criar cliente
cliente1 = PessoaFisica("123.456.789-00", "João Silva", date(1990, 5, 20), "Rua das Flores, 123")

# Criar conta corrente
conta1 = ContaCorrente.nova_conta(cliente1, 1001)
cliente1.adicionar_conta(conta1)

# Realizar transações
cliente1.realizar_transacao(conta1, Deposito(1000))
cliente1.realizar_transacao(conta1, Saque(200))
cliente1.realizar_transacao(conta1, Saque(300))
cliente1.realizar_transacao(conta1, Deposito(500))

# Mostrar saldo
print(f"\nSaldo final: {conta1.saldo_atual()}")

# Gerador - todas transações
print("\nTodas as transações:")
for t in conta1.historico.gerar_transacoes():
    print(f"{type(t).__name__}: R$ {t.valor}")

# Gerador - apenas saques
print("\nApenas saques:")
for saque in conta1.historico.gerar_transacoes(Saque):
    print(f"Saque de R$ {saque.valor}")

# Gerador - apenas depósitos
print("\nApenas depósitos:")
for deposito in conta1.historico.gerar_transacoes(Deposito):
    print(f"Depósito de R$ {deposito.valor}")
