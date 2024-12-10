class Conta:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor a ser depositado deve ser maior que zero.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("O valor a ser sacado deve ser maior que zero.")

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")


conta = Conta(100)
conta.depositar(50)
conta.sacar(30)
conta.mostrar_saldo()
conta.sacar(200) 
conta.depositar(-10) 

