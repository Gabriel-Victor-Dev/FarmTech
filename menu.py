import time


# ---------------- FUNÇÕES ----------------
def caixa_msg(texto, largura=80):
    """
    Exibe uma mensagem dentro de uma caixa bonita no terminal.

    Parâmetros:
    texto : str  -> texto que será exibido dentro da caixa
    largura : int -> largura total da caixa (default=80)
    """
    print("\n" + "╔" + "═" * (largura - 2) + "╗")
    print("║" + texto.center(largura - 2) + "║")
    print("╚" + "═" * (largura - 2) + "╝")


def leia_cultura(msg="Digite a cultura (Milho/Cana): "):
    """
    Lê e valida o nome da cultura.

    Aceita apenas 'Milho' ou 'Cana' (case-insensitive).
    Retorna o nome da cultura capitalizado.
    """
    while True:
        nome = input(msg).strip().lower()
        if nome in ("milho", "cana"):
            return nome.capitalize()
        caixa_msg("⚠️ Cultura inválida! Use apenas 'Milho' ou 'Cana'.")


def leia_float_positivo(msg):
    """
    Lê um número decimal positivo (>0) com validação.

    Converte vírgula em ponto automaticamente.
    Exibe mensagem de erro em caso de entrada inválida.
    """
    while True:
        try:
            valor = float(input(msg).replace(",", "."))
            if valor > 0:
                return valor
            caixa_msg("⚠️ O valor deve ser maior que zero.")
        except ValueError:
            caixa_msg("⚠️ Valor inválido! Digite um número (ex: 12.5).")


titulo = """
███████╗ █████╗ ██████╗ ███╗   ███╗████████╗███████╗ ██████╗██╗  ██╗
██╔════╝██╔══██╗██╔══██╗████╗ ████║╚══██╔══╝██╔════╝██╔════╝██║  ██║
█████╗  ███████║██████╔╝██╔████╔██║   ██║   █████╗  ██║     ███████║
██╔══╝  ████═██║██╔══██╗██║╚██╔╝██║   ██║   ██╔══╝  ██║     ██╔══██║
██║     ██║  ██║██║  ██║██║ ╚═╝ ██║   ██║   ███████╗╚██████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝

███████╗ ██████╗ ██╗     ██╗   ██╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔════╝██╔═══██╗██║     ██║   ██║╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
███████╗██║   ██║██║     ██║   ██║   ██║   ██║██║   ██║██╔██╗ ██║███████╗
╚════██║██║   ██║██║     ██║   ██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║
███████║╚██████╔╝███████╗╚██████╔╝   ██║   ██║╚██████╔╝██║ ╚████║███████║
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""

for linha in titulo.splitlines():
    print(linha.center(80))  # CONFIGURA A CENTRALIZAÇÃO DO CABEÇALHO.

# ---------------- CABEÇALHO ----------------
titulo2 = "| Bem Vindo ao Sistema de Gerenciamento de Culturas |"
largura = 80
print("=" * largura)
print(titulo2.center(largura))
print("=" * largura)

# ---------------- LISTAS ----------------
culturas = []  # armazena nomes das culturas cadastradas
formas = []    # armazena forma geométrica usada para cálculo da área
areas = []     # armazena área de plantio em hectares
insumos = []   # armazena insumos aplicados (lista de tuplas por cultura)

time.sleep(1)

# ---------------- MENU ----------------
menu = "  ◆ ◇ ◈ MENU PRINCIPAL ◈ ◇ ◆  "
opcoes = [
    "1 -> Cadastrar Culturas",
    "2 -> Listar Culturas",
    "3 -> Calcular Área de Plantio",
    "4 -> Calcular Insumos",
    "5 -> Atualizar Dados",
    "6 -> Deletar Dados",
    "7 -> Listar Insumos",
    "8 -> SAIR"
]

opcao = 0

while opcao != 8:

    # Exibe o menu centralizado em caixa
    print("\n" + "╔" + "═" * (largura - 2) + "╗")
    print("║" + menu.center(largura - 2) + "║")
    print("╠" + "═" * (largura - 2) + "╣")
    for item in opcoes:
        print("║" + item.center(largura - 2) + "║")
    print("╚" + "═" * (largura - 2) + "╝")

    # LEITURA SEGURA DE OPÇÃO
    while True:
        try:
            opcao = int(input('➔ Digite a opção desejada (1 a 8): '))
            if 1 <= opcao <= 8:
                break
            caixa_msg("⚠️ Opção inválida! Digite um número de 1 a 8.")
        except ValueError:
            caixa_msg("⚠️ Entrada não numérica! Digite um número de 1 a 8.")

    # ---------------- OPÇÕES ----------------
    if opcao == 1:  # Cadastrar cultura
        caixa_msg("Cadastro de Culturas")
        nome = leia_cultura()
        area = leia_float_positivo("📐 Área plantada (em hectares): ")
        culturas.append(nome)
        areas.append(area)
        formas.append(None)  # ainda sem forma geométrica definida
        insumos.append([])   # lista vazia de insumos
        caixa_msg(f"✅ {nome} cadastrada com área {area:.2f} ha.")

    elif opcao == 2:  # Listar culturas
        caixa_msg("Listagem de Culturas")
        if not culturas:
            caixa_msg("📭 Nenhuma cultura cadastrada.")
        else:
            for i, (c, a) in enumerate(zip(culturas, areas), start=1):
                print(f"{i:02d}. {c:<5} | Área: {a:.2f} ha | Forma: {formas[i-1]}")

    elif opcao == 3:  # Calcular área de plantio
        caixa_msg("Calcular Área de Plantio")
        if not culturas:
            caixa_msg("📭 Nenhuma cultura cadastrada.")
        else:
            for i, c in enumerate(culturas, start=1):
                print(f"{i}. {c}")
            escolha = int(input("➔ Escolha a cultura pelo número: ")) - 1

            print("\nFormas geométricas disponíveis:")
            print("1 -> Retângulo")
            print("2 -> Triângulo")
            forma = int(input("➔ Escolha a forma (1 ou 2): "))

            base = leia_float_positivo("📏 Base (m): ")
            altura = leia_float_positivo("📐 Altura (m): ")

            if forma == 1:
                area = base * altura
                formas[escolha] = "Retângulo"
            elif forma == 2:
                area = (base * altura) / 2
                formas[escolha] = "Triângulo"
            else:
                caixa_msg("⚠️ Forma inválida!")
                continue

            areas[escolha] = area
            caixa_msg(f"✅ Área de {culturas[escolha]}: {area:.2f} m² ({formas[escolha]})")

    elif opcao == 4:  # Calcular insumos
        caixa_msg("Calcular Insumos")
        if not culturas:
            caixa_msg("📭 Nenhuma cultura cadastrada.")
        else:
            for i, c in enumerate(culturas, start=1):
                print(f"{i}. {c}")
            escolha = int(input("➔ Escolha a cultura pelo número: ")) - 1

            if areas[escolha] is None:
                caixa_msg("⚠️ Área não calculada! Use a opção 3 primeiro.")
            else:
                # regras de insumos por cultura
                if culturas[escolha] == "Milho":
                    taxa = 20
                    unidade = "kg"
                    produto = "Fertilizante NPK"
                elif culturas[escolha] == "Cana":
                    taxa = 30
                    unidade = "L"
                    produto = "Herbicida"

                total = areas[escolha] * taxa  # calcula insumo baseado em hectares
                insumos[escolha].append((produto, total, unidade))
                caixa_msg(f"🌱 {total:.2f} {unidade} de {produto} para {culturas[escolha]}")

    elif opcao == 5:  # Atualizar dados de uma cultura
        caixa_msg("Atualizar Dados")
        if not culturas:
            caixa_msg("📭 Nenhuma cultura cadastrada.")
        else:
            for i, c in enumerate(culturas, start=1):
                print(f"{i}. {c}")
            escolha = int(input("➔ Escolha a cultura para atualizar pelo número: ")) - 1
            nome = leia_cultura()
            area = leia_float_positivo("📐 Nova área (em hectares): ")
            culturas[escolha] = nome
            areas[escolha] = area
            formas[escolha] = None
            insumos[escolha] = []
            caixa_msg(f"✅ Cultura atualizada: {nome}, Área: {area:.2f} ha")

    elif opcao == 6:  # Deletar dados de uma cultura
        caixa_msg("Deletar Dados")
        if not culturas:
            caixa_msg("📭 Nenhuma cultura cadastrada.")
        else:
            for i, c in enumerate(culturas, start=1):
                print(f"{i}. {c}")
            escolha = int(input("➔ Escolha a cultura para deletar pelo número: ")) - 1
            del culturas[escolha]
            del areas[escolha]
            del formas[escolha]
            del insumos[escolha]
            caixa_msg("✅ Cultura deletada com sucesso!")

    elif opcao == 7:  # Listar insumos aplicados
        caixa_msg("Listagem de Insumos")
        if not culturas:
            caixa_msg("📭 Nenhuma cultura cadastrada.")
        else:
            for c, ins in zip(culturas, insumos):
                print(f"🌱 {c}:")
                if not ins:
                    print("   ➔ Nenhum insumo aplicado")
                else:
                    for prod, qt, un in ins:
                        print(f"   ➔ {qt:.2f} {un} de {prod}")

    elif opcao == 8:  # Sair
        caixa_msg("Saindo do programa. Até logo! ✅")