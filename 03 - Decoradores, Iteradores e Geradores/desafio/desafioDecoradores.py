from abc import ABC, abstractmethod
from datetime import datetime, date
from functools import wraps

# Decorador para log de transações
def log_transacao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tipo = func.__name__
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{data_hora}] Transação: {tipo}")
        return func(*args, **kwargs)
    return wrapper

# Transações
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

# Histórico de transações
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# Conta bancária base
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
            print("Valor de depósito inválido.")
            return False
        self.saldo += valor
        self.historico.adicionar_transacao(Deposito(valor))
        return True

    @classmethod
    @log_transacao
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

# Conta corrente (com limite e limite de saques)
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

# Cliente
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

# Pessoa Física
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


# Criar cliente
cliente1 = PessoaFisica("123.456.789-00", "João Silva", date(1990, 5, 20), "Rua A, 123")

# Criar conta
conta1 = ContaCorrente.nova_conta(cliente1, 1001)
cliente1.adicionar_conta(conta1)

# Realizar transações
cliente1.realizar_transacao(conta1, Deposito(1000))
cliente1.realizar_transacao(conta1, Saque(200))

# Mostrar saldo e histórico
print(f"Saldo final: {conta1.saldo_atual()}")
print("Histórico de transações:")
for t in conta1.historico.transacoes:
    print(f"{type(t).__name__} - valor: {t.valor}")
