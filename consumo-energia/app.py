print('============ Calculadora de Consumo Elétrico')

aparelho= input("Digite o nome do aparelho:")
potencia=float ( input("Digite a potencia do aparelho:"))
horas= float(input("Digite o tempo médio de uso diário:"))

consumo_mensal=(potencia*horas*30)/1000

print("\n====== Resultado======")
print(f"Aparelho:{aparelho}")
print(f"consumo mensal:{consumo_mensal:.2f} kWh/mes")


 