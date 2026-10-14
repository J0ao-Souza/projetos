import colorama


nivel_atual=3

mensagens=[
    "Muito baixo",
    "baixo",
    "normal",
    "alto",
    "Muito alto"
]

def definir_cor(nivel):
    if nivel == 1:
        return colorama.Fore.RED
    elif nivel == 2:
        return colorama.Fore.YELLOW
    elif nivel  == 3:
        return colorama.Fore.GREEN
    elif nivel == 4:
        return colorama.Fore.CYAN
    elif nivel == 5:
        return colorama.Fore.BLUE

print(definir_cor(nivel_atual)+ mensagens[nivel_atual-1] )
print(colorama.Style.RESET_ALL)
