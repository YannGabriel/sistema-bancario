#Verificação conta bancária


#opções fixas para ocorrer o programa
tipo_conta_bancaria = -1
valor_conta = 2500
SAQUE_MAXIMO = 500

#questionario de nome para acessar a conta

nome = input("\nInsira seu nome: ")

print(
  f"""
##########################################
  
Olá, {nome.title()}, seja bem vindo! Por favor,
digite seu valor de saque abaixo e seu tipo de conta!

##########################################
  """
)

#valor do saque (escolhido pelo usuário)

saque = float(input("Insira o valor que você deseja sacar: "))

#opção de saber o restante na conta

valor_restante_opcao = -1

valor_restante = valor_conta - saque

#estrutura de escolha de conta e valores

def saldo_invalido():
        print(f"""
    
Processando saque...
              
Seu saque não foi autorizado.
Obrigado por acessar nosso banco, tenha um ótimo dia!
      
              """)
        
if saque >= SAQUE_MAXIMO:
    print(saldo_invalido())

else:
    print("""
                                 
-------------------------------------------
                                  
Escolha seu tipo de conta bancária:  
[1] Conta Padrão 
[2] Conta Universitária
[0] Sair 

                                  """)

    tipo_conta_bancaria = int(input("Digite sua opção: "))

def conta_padrao():
    if saque <= valor_conta:
      print(f"""
            
Processando saque...
Seu saque no valor de {saque} foi autorizado

Deseja saber o restante de saldo em sua conta?

[1] Sim
[2] Não

            """)
      
    saldo_restante = int(input("Insira a sua opção: "))
        
    if saldo_restante == 1:
        print(f"""
-----------------------------------------
Você possui na sua conta: {valor_restante}

Obrigado por acessar nosso banco, tenha um ótimo dia!
                    """)

    else:
        print("Obrigado por acessar nosso banco, tenha um ótimo dia!")

def conta_universitaria():
    if saque < 300:
      print(f"""
            
Processando saque...
Seu saque no valor de {saque} foi autorizado
Obrigado por acessar nosso banco, tenha um ótimo dia!
            
            """)
    else:
      print("""
            
Seu saque deverá ser autorizado por seus responsaveis em nosso app.
Obrigado por acessar nosso banco, tenha um ótimo dia!

            """)




print("\n-------------------------------------------")

if tipo_conta_bancaria == 0:
    print("Obrigado por acessar! Volte sempre!")
elif tipo_conta_bancaria == 1:
    print(conta_padrao())
elif tipo_conta_bancaria == 2:
    print(conta_universitaria())





