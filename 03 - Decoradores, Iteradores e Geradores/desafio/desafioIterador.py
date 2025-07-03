

from datetime import date

# Importe ou defina PessoaFisica, ContaCorrente, Deposito antes de usar
from desafio.desafioDecoradores import PessoaFisica, ContaCorrente, Deposito
# Exemplo de importação (ajuste conforme a estrutura do seu projeto):
# from seu_modulo import PessoaFisica, ContaCorrente, Deposito

class ContaIterador:
    def __init__(self, clientes):
        self.clientes = clientes
        self.cliente_index = 0
        self.conta_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.cliente_index < len(self.clientes):
            cliente = self.clientes[self.cliente_index]
            if self.conta_index < len(cliente.contas):
                conta = cliente.contas[self.conta_index]
                self.conta_index += 1
                return {
                    "cliente": getattr(cliente, 'nome', 'N/A'),
                    "numero": conta.numero,
                    "saldo": conta.saldo_atual(),
                    "tipo_conta": type(conta).__name__,
                    "agencia": conta.agencia
                }
            else:
                self.cliente_index += 1
                self.conta_index = 0
        raise StopIteration


# Criando lista de clientes do banco
clientes_banco = []

# Criar dois clientes
cliente1 = PessoaFisica("111.222.333-44", "João", date(1990, 1, 1), "Rua A")
cliente2 = PessoaFisica("555.666.777-88", "Maria", date(1985, 2, 2), "Rua B")

# Criar contas para os clientes
conta1 = ContaCorrente.nova_conta(cliente1, 101)
conta2 = ContaCorrente.nova_conta(cliente2, 102)
cliente1.adicionar_conta(conta1)
cliente2.adicionar_conta(conta2)

# Depositar valores
cliente1.realizar_transacao(conta1, Deposito(800))
cliente2.realizar_transacao(conta2, Deposito(1200))

# Adiciona os clientes à "base de dados" do banco
clientes_banco.extend([cliente1, cliente2])


# Iterar sobre todas as contas do banco
print("\n== Informações das Contas no Banco ==")
for conta_info in ContaIterador(clientes_banco):
    print(f"Cliente: {conta_info['cliente']}, "
          f"Nº Conta: {conta_info['numero']}, "
          f"Saldo: R$ {conta_info['saldo']:.2f}, "
          f"Tipo: {conta_info['tipo_conta']}, "
          f"Agência: {conta_info['agencia']}")
