tipo_imovel=str(input("Digite o tipo de imovel:"))
if tipo_imovel != "comercial" and tipo_imovel != "casa" and tipo_imovel != "apartamento":
    print("tipo de imovel invalido!!!, digite outro tipo")
    exit()

consumodeagua=float(input("Digite o consumo de agua:"))

if tipo_imovel=="comercial":
    print("Tarifa comercial aplicada,consulte o plano corporativo")

elif (tipo_imovel=="apartamento") and consumodeagua <10:
    print("Consumo economico, excelente controle de agua!!!")

elif(tipo_imovel=="casa" or tipo_imovel=="apartamento") and consumodeagua <= 25:
    print("Consumo moderado, dentro do padrao residencial.")

else:
    print("Consumo excessivo, adote medidas de economia e verifique vazamentos!!!")

    








