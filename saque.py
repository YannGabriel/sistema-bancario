#Verificação conta bancária
#definição padrão para escolha de conta
opcao = -1
valor_conta = 2500

nome = input("\nInsira seu nome: ")

print(
  f"""
##########################################
  
Olá, {nome.title()}, seja bem vindo! Por favor,
digite seu valor de saque abaixo e seu tipo de conta!

##########################################
  """
)

saque = float(input("Insira o valor que você deseja sacar: "))

#opção de saber o restante na conta

valor_restante_opcao = -1;

valor_restante = valor_conta - saque

#estrutura de escolha de conta e valores

while opcao != 0:

  print("""
                                  
-------------------------------------------
                                  
Escolha seu tipo de conta bancária:  
[1] Conta Padrão 
[2] Conta Universitária
[3] Conta Premium 
[0] Sair 

                                  """)
  
  tipo_conta_bancaria = int(input("Digite sua opção: "))

  print("\n-------------------------------------------")
  
  if tipo_conta_bancaria == 1:
    if saque <= valor_conta:
      print(f"""
            
Processando saque...
Seu saque no valor de {saque} foi autorizado
            """)
    
      while valor_restante_opcao != 0:
        saldo_restante = int(input("""
                                   
Deseja saber o saldo restante da conta?
[1] Sim
[2] Não
                                   
Insira sua opção: """))
        
        if saldo_restante == 1:
          print("""
-----------------------------------------
Você possui na sua conta: {valor_restante}

Obrigado por acessar nosso banco, tenha um ótimo dia!
                """)
          break
        else:
          print("Obrigado por acessar nosso banco, tenha um ótimo dia!")
          break
      break
      break

  elif tipo_conta_bancaria ==2:
    if saque < 300:
      print(f"""
            
Processando saque...
Seu saque no valor de {saque} foi autorizado
Obrigado por acessar nosso banco, tenha um ótimo dia!
            
            """)
      break
    else:
      print("""
            
Seu saque deverá ser autorizado por seus responsaveis em nosso app.
Obrigado por acessar nosso banco, tenha um ótimo dia!

            """)
      break

  elif tipo_conta_bancaria ==3:
      if saque <= 1000000:
        juros = saque + (saque * 0.08)
        print(f"""
              
Processando saque...")
Seu saque no valor de {saque + juros} foi autorizado
Obrigado por acessar nosso banco, tenha um ótimo dia!
              
              """)
        break
      else:
        print("""
              
Seu saque não foi autorizado.
Obrigado por acessar nosso banco, tenha um ótimo dia!
      
              """)
        break

  elif tipo_conta_bancaria ==0:
        print("Obrigado por acessar nosso banco, tenha um ótimo dia!")
        break