
#Para inicializar a biblioteca do colorama
from colorama import Fore, Style, init

#Listas de referência
nivel_reservatorio = ["Nível 1", "Nível 2", "Nível 3", "Nível 4", "Nível 5"]
situacao = ["Muito baixo", "Baixo", "Médio", "Alto", "Muito alto"]

print("--- SISTEMA DE MONITORAMENTO DE RESERVATÓRIO ---")
print("O nível do reservarório está: ")

#Simulação com um valor definido no código
#Você pode trocar para "1", "2", "4" e "5" para testar cada regra
nivel_escolhido = "5"

#Validação usando if, elif e else
if nivel_escolhido == "1":
    print(Fore.RED + "Muito baixo (Crítico)")
elif nivel_escolhido == "2":
    print(Fore.YELLOW + "Baixo")
elif nivel_escolhido == "3":
    print(Fore.GREEN + "Médio")
elif nivel_escolhido == "4":
    print(Fore.CYAN + "Alto")
elif nivel_escolhido == "5":
    print(Fore.BLUE + "Muito alto")
else:
    print(Fore.RED + "Opção inválida! Por favor, digite um número entre 1 e 5.")

print(Style.RESET_ALL)
