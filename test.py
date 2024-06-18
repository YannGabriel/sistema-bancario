

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

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else: 
        print("Operação falhou, tente novamente!")
        
    return saldo , extrato   
    
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
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Seu saque foi autorizado!")
        
    else:
        print("Operação falhou, tente novamente!")
        
    return saldo, extrato
            
def exibir_extrato (saldo, *, extrato):
    print("\n############# EXTRATO ############\n")
    print("Não foram realizados nenhum movimento na sua conta!" if not extrato else extrato)
    print(f"Seu saldo é de: R${saldo:.2f}")
    print("\n##################################\n")
    
def novo_usuario(usuarios):
    cpf = input("Insira seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe um usuário cadastrado com as informações acima!")
        return
    nome = input("Insira seu nome: ")
    data_nascimento = input("Insira a sua data de nascimento (xx/xx/xxxx): ")
    endereco = input("Insira seu endereço - logadouro / nº / bairro / cidade / estado(sigla): ")
    
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso, agora você pode acessar sua conta!")

def filtrar_usuario(cpf, usuarios):
    filtro_usuarios = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return filtro_usuarios[0] if filtro_usuarios else None
        
def nova_conta(agencia, numero_conta, usuario):
    cpf = input("Insira o CPF que deseja criar a conta: ")
    usuario = filtrar_usuario(cpf, usuario)
    if usuario:
        print("\nSua conta foi criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuario não encontrado, crie seu perfil e tente novamente!")
    
def listar_contas(contas):
    for conta in contas:
        linha_conta = f"""
Agência: {conta['agencia']}
C/C: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}
              """
        print(linha_conta)
        
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
            
            saldo, extrato , saque(
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
            
        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = nova_conta(agencia, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
            
        elif opcao == 5:
            novo_usuario(usuarios)
            
        elif opcao == 6:
            listar_contas(contas)
            
main()

