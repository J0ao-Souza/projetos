#Solicita o valor da compra
valordacompra=float(input("Digite o valor da compra:"))

#cria a variavel do desconto 
valordesconto= 0

#cria a variavel do valor final apos os descontos
valorfinal= 0

#estrutura de condiçao para o valor do desconto e calculo final
if valordacompra<200:
    valordesconto=5
    valorfinal=valordacompra*0.95

elif valordacompra <300:
     valordesconto=10
     valorfinal=valordacompra*0.9

else:
     valordesconto=15
     valorfinal=valordacompra*0.85



#exibe todos os resultados
print("============ Calculadora de descontos ============")
print(f"valor do desconto: {valordesconto}%")
print(f"Valor da compra: R$ {valordacompra:.2f}")
print(f"Valor final: R$ {valorfinal:.2f}")