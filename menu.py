# > Listas para armazenar dados
culturas = []
formas = []
areas = []
insumos = []

# > Menu principal
menu = "  ◆ ◇ ◈ MENU PRINCIPAL ◈ ◇ ◆  "
largura2 = 80
opcoes = [
    "1 -> Cadastrar Culturas",
    "2 -> Listar Culturas",
    "3 -> Calcular Área de Plantio",
    "4 -> Calcular Insumos",
    "5 -> SAIR"
]

opcao = 0

while opcao != 5:

    # Mostrar o menu
    print("\n" + "╔" + "═" * (largura2 - 2) + "╗")
    print("║" + menu.center(largura2 - 2) + "║")
    print("╠" + "═" * (largura2 - 2) + "╣")
    for item in opcoes:
        print("║" + item.center(largura2 - 2) + "║")
    print("╚" + "═" * (largura2 - 2) + "╝")

    # Pedir opção do usuário
    try:
        opcao = int(input('Digite a opção desejada (1 a 5) 🎯: '))
        if opcao not in [1,2,3,4,5]:
            print("⚠️ Opção inválida! Digite de 1 a 5 ⚠️")
            continue  # volta para o menu
    except ValueError:
        print("⚠️ Opção inválida! Digite de 1 a 5 ⚠️")
        continue  # volta para o menu

    # Processar opção
    if opcao == 1:
        print("Você escolheu cadastrar culturas")
    elif opcao == 2:
        print("Você escolheu listar culturas")
    elif opcao == 3:
        print("Você escolheu calcular área de plantio")
    elif opcao == 4:
        print("Você escolheu calcular insumos")
    elif opcao == 5:
        print("Saindo do programa... ✅")
