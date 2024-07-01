
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas =  []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        
class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self.saldo
    
    @property
    def numero(self):
        return self.numero
    
    @property
    def agencia(self):
        return self.agencia
    
    @property
    def cliente(self):
        return self.cliente
    
    @property
    def histrico(self):
        return self.historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("Saque não autorizado! O valor necessário excede o que há na conta!")
        elif valor > 0:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Desculpe, tivemos um erro na operação! Tente novamente.")
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Deposito autorizado com sucesso!")
        else:
            print("Algum erro ocorreu no processo, por favor tente novamente!")
            return False
        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes
             if transacao["tipo"] == Saque.__name__]
        )
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques
        if excedeu_limite:
            print("Operação não autorizada, pois o limite foi ultrapassado/atingido!")
        elif excedeu_saques:
            print("Operação não autoizada, pois o limite de saques foi atingido!")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""
    Agência: {self.agencia}
    C/C: {self.numero}
    Titular = {self.cliente.nome}
    """
            
class Historico:
    def __init__(self):
        self.transacoes = []
        
    @property
    def transacoes(self):
        return self.transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data" : datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )
    
class Transacao(ABC):
        @property
        @abstractproperty
        def valor(self):
            pass
        
        @abstractclassmethod
        def registrar(self, conta):
            pass
            
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
      
    @property  
    def valor(self):
        return self.valor

    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
class Deposito(Transacao):
    
    def __init__(self, valor):
        self.valor = valor
        
    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
def menu_inicial():
    print(
  f"""
##########################################
  
Olá, seja bem vindo ao banco Seu dinheiro é Nosso! 
Selecione a opção desejada abaixo:
[1] Sacar
[2] Depositar
[3] Extrato
[4] Nova conta
[5] Novo Usuário
[6] Listar contas
[0] sair

##########################################
  """
)

    opcao = int(input("Insira uma opção: "))
    return opcao

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta!")
        return
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente não encontrado!")
        return
    
    valor = float(input("Insira o valor do depósito desejado: "))
    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
    
def sacar(clientes):
     cpf = input("Informe seu CPF: ")
     cliente = filtrar_cliente(cpf, clientes)
     if not cliente:
        print("Cliente não encontrado!")
        return
    
     valor = float(input("Insira o valor do saque desejado: "))
     transacao = Saque(valor)
    
     conta = recuperar_conta_cliente(cliente)
     if not conta:
        return
    
     cliente.realizar_transacao(conta, transacao)
                
def exibir_extrato (clientes):
    cpf = input("Informe seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("====== EXTRATO ======")
    transacoes = conta.historico.transacoes
    extrato = ""
    
    if not transacoes:
        extrato = "Não há movimentações na sua conta!"
    else:
        for transacao in transacoes:
            extrato += f"{transacao['tipo']}: R${transacao['valor']:.2f}"
    print(extrato)
    print(f"Saldo: R${conta.saldo}")
    print("=================================")
    
def novo_cliente(clientes):
    cpf = input("Insira seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("Já existe um usuário cadastrado com as informações acima!")
        return
    nome = input("Insira seu nome: ")
    data_nascimento = input("Insira a sua data de nascimento (xx/xx/xxxx): ")
    endereco = input("Insira seu endereço - logadouro / nº / bairro / cidade / estado(sigla): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("Usuário criado com sucesso, agora você pode acessar sua conta!")

def criar_conta(numero_conta, clientes, contas):
     cpf = input("Informe seu CPF: ")
     cliente = filtrar_cliente(cpf, clientes )
     if not cliente:
        print("Cliente não encontrado!")
        return
     conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
     contas.append(conta)
     cliente.contas.append(conta)
     
     print("Conta Criada com sucesso!")
     
def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []
        
    while True:
        opcao = menu_inicial()
        
        if opcao == 1:
            sacar(clientes)
            
        elif opcao == 2:
            depositar(clientes)
            
        elif opcao == 3:
            exibir_extrato(clientes)
            
        elif opcao == 4:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
    
        elif opcao == 5:
            novo_cliente(clientes)
            
        elif opcao == 6:
            listar_contas(contas)
            
main()