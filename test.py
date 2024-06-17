 

def menu_inicial ():
  print(
  f"""
##########################################
  
Olá, seja bem vindo ao banco Seu dinheiro é Nosso! 
Já possui uma conta?
[1] Sim
[2] Não

##########################################
  """
)
  opcao_extrato = -1
  opcao_servico = -1
  numero_agencia_bancaria = [1]
  senhas = [1]
  opcao_conta_existente = int(input("Insira a opção: "))
  
  if opcao_conta_existente == 1:
    numero_agencia = int(input("Insira o número da sua agência bancária: "))
    if numero_agencia in numero_agencia_bancaria:
      print("Certo, agora forneça sua senha de acesso (4 digitos)")
      senha_acesso_conta_bancaria = int(input("Sua senha: "))
      if senha_acesso_conta_bancaria in senhas:
        print("""
Suas informações foram validadas e estam corretas!
Qual serviço deseja efetuar?
[1] saque
[2] deposito
[3] extrato
[0] sair
              """)
        opcao_servico = int(input("Insira a opção do serviço desejdao:"))
        if opcao_servico == 1:
          sacar()
    else:
      print("Alguma das opções acima estão inválidas e/ou incorretas!")

  
def sacar():
  saldo = 2500
  valor = float(input("Insira o valor que deseja sacar: "))
  SAQUE_MAXIMO = 500
  if valor > SAQUE_MAXIMO:
    print("O seu saque foi negado por exceder o valor limite!")
  else:
    print("""
Seu saque foi autorizado, deseja saber seu extrato?

[1] Sim
[2] Não
          """)
    
    opcao_extrato = int(input("Insira a sua opção: "))
    
    extrato = saldo - valor
    
    if opcao_extrato not in [1 , 2]:
      print("\nPor favor, escolha uma opção válida!")
       
    elif opcao_extrato == 1:
      print(f"Seu extrato é de: {extrato}")
      breakpoint
  print("Obrigado por acessa nosso banco!")


    
def main():
  menu_inicial()

main()