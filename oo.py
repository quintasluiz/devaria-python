class ContaBancaria:
    def __init__(self, tipo, conta, agencia):
        self.tipo = tipo
        self.conta = conta
        self.agencia = agencia

    def exibirDadosDaConta(self):
        print( f'Informações da conta Tipo: {self.tipo} Conta: {self.conta} Agencia: {self.agencia}')

if __name__ == '__main__':
    conta1 = ContaBancaria('corrente', 6548, '57002')
    conta1.exibirDadosDaConta()

''' print(f'Conta criada Tipo: {conta1.tipo} Conta: {conta1.conta} Agencia: {conta1.agencia}')

    conta2 = ContaBancaria('poupança', 3449, '97889')
    print( f'Conta criada Tipo: {conta2.tipo} Conta: {conta2.conta} Agencia:{conta2.agencia}') '''

