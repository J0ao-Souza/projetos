excelente=0
bom=0
ruim=0



for i in range(50):
    print("Bem vindo a pesquisa de opinião!")
    print("Digite as informaçoes abaixo e nos de sua opiniao!(!-Excelente, 2-Bom, 3-Ruim)")
    nome=str(input("Digite seu nome: "))
    idade=int(input("Digite sua idade:"))
    print("Escolha uma das alternativas para sua opiniao:")
    print("1. Excelente")
    print("2. Bom")
    print("3. Ruim")
    opiniao=int(input("Digite sua opinião:(1-3) "))
    while opiniao!=1 and opiniao!=2 and opiniao !=3:
        print("Opinião inválida! Digite apenas 1, 2 ou 3.")
        opiniao=int(input("Digite sua opinião:(1-3) "))
    if opiniao==1:
        excelente +=1
    elif opiniao==2:
        bom+=1
    elif opiniao==3:
        ruim+=1



print("Resultados da pesquisa:")
print(f"Excelente: {excelente}")
print(f"Bom: {bom}")
print(f"Ruim: {ruim}")