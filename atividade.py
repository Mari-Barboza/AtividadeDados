class Cliente:
    def __init__(self, nome, endereco, cpf, telefone):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._telefone = telefone

    # Getters e Setters
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_endereco(self):
        return self._endereco

    def set_endereco(self, endereco):
        self._endereco = endereco

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone


class Conta:
    def __init__(self, numero_conta, saldo, cliente):
        self._numero_conta = numero_conta
        self._saldo = saldo
        self._cliente = cliente

    # Método para depósito
    def depositar(self, valor):
        self._saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self._saldo}")

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso. Saldo atual: R${self._saldo}")
        else:
            print("Saldo insuficiente")

    # Método para exibir saldo
    def exibir_saldo(self):
        print(f"O saldo da conta {self._numero_conta} é: R${self._saldo}")

    # Método para transferir entre contas
    def transferir(self, valor, conta_destino):
        if self._saldo >= valor:
            self.sacar(valor)
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor} para a conta {conta_destino._numero_conta} realizada com sucesso")
        else:
            print("Saldo insuficiente para realizar a transferência.")


# Simulação de dois clientes e duas contas
cliente1 = Cliente("Marina Barboza", "Rua A, 123", "123.321.123-12", "(11)99999-9999")
cliente2 = Cliente("Alicia Jaja", "Rua B, 567", "567.765.567-56", "(11)99999-9999")

conta1 = Conta(1001, 100, cliente1)
conta2 = Conta(1002, 500, cliente2)

# Exibir saldo inicial
conta1.exibir_saldo()
conta2.exibir_saldo()

# Depositar e sacar
conta1.depositar(200)
conta2.sacar(100)

# Transferir dinheiro entre contas
conta1.transferir(300, conta2)
