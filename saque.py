

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


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_limite_excedido = valor > saldo
    limite_excedido = valor > limite
    limite_saques_excedido = numero_saques >= limite_saques
    
    if saldo_limite_excedido:
        print("O valor excedeu o saldo que você possui na sua conta!")
    elif limite_excedido:
        print("O valor desejado excede o limite diário!")
    elif limite_saques_excedido: 
        print("Você já atingiu o número de saques diários!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        print("Seu saque foi autorizado!")
    else:
        print("Operação falhou, tente novamente!")
        
    return saldo , extrato
            
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato  += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else: 
        print("Operação falhou, tente novamente!")
        
    return saldo , extrato   
    
def exibir_extrato (saldo, / , * , extrato):
    print("\n############# EXTRATO ############\n")
    print("Não foram realizados nenhum movimento na sua conta!" if not extrato else extrato)
    print(f"Seu saldo é de: {saldo:.2f}")
    print("\n##################################\n")
    
def main():
    LIMITE_SAQUES = 3
    agencia = "0001"
    usuarios = []
    contas = []
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    
    while True:
        opcao = menu_inicial()
        
        if opcao == 1:
            valor = float(input("Informe o valor que deseja sacar: "))
            
            saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )
            
        elif opcao == 2:
            valor = float(input("Informe o valor que deseja depositar: "))
            
            saldo , extrato = depositar(saldo, valor, extrato)
            
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
            
            
main()