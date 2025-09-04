# > Inicialização e Cabeçalho

import time
def caixa_msg(texto, largura=80):
    print("\n" + "╔" + "═" * (largura - 2) + "╗")
    print("║" + texto.center(largura - 2) + "║")
    print("╚" + "═" * (largura - 2) + "╝")

def leia_cultura(msg="Digite a cultura (Milho/Cana): "):
    """Aceita apenas Milho ou Cana (case-insensitive). Retorna capitalizado."""
    while True:
        nome = input(msg).strip().lower()
        if nome in ("milho", "cana"):
            return nome.capitalize()
        print("⚠️ Cultura inválida! Use apenas 'Milho' ou 'Cana'.")

def leia_float_positivo(msg):
    """Lê float > 0 com validação e mensagens amigáveis."""
    while True:
        try:
            valor = float(input(msg).replace(",", "."))
            if valor > 0:
                return valor
            print("⚠️ O valor deve ser maior que zero.")
        except ValueError:
            print("⚠️ Valor inválido! Digite um número (ex: 12.5).")

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
    print(linha.center(80)) #CONFIGURA A CENTRALIZAÇÃO DO CABEÇALHO.

titulo2 = "| Bem Vindo ao Sistema de Gerenciamento de Culturas |"
largura = 80

print("=" * largura)
print(titulo2.center(largura))
print("=" * largura)

# > Listas para armazenar dados
culturas = []
formas = []
areas = []
insumos = []

time.sleep(2.0)
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

        #  LEITURA SEGURA DE OPÇÃO
        while True:
            try:
                opcao = int(input('  ➔  Digite a opção desejada (1 a 5) 🎯 : '))
                if 1 <= opcao <= 5:
                    break
                print("⚠️ Opção inválida! Digite um número de 1 a 5.")
            except ValueError:
                print("⚠️ Entrada não numérica! Digite um número de 1 a 5.")

# PROCESSAR OPÇÃO

if opcao == 1:
    caixa_msg("Você escolheu cadastrar culturas")

    # --- CADASTRO DE CULTURA ---
    nome = leia_cultura("🌾 Cultura (Milho/Cana): ")
    area = leia_float_positivo("📐 Área plantada (em hectares): ")

    culturas.append(nome)
    areas.append(area)
    formas.append(None)
    insumos.append([])  # lista vazia para insumos

    print(f"✅ {nome} cadastrada com área de {area:.2f} ha.")

elif opcao == 2:
    caixa_msg("Listagem de culturas")
    if not culturas:
        print("📭 Nenhuma cultura cadastrada ainda.")
    else:
        for i, (c, a) in enumerate(zip(culturas, areas), start=1):
            print(f"{i:02d}. {c:<5} | área: {a:.2f} ha")

elif opcao == 3:
    caixa_msg("Você escolheu calcular área de plantio")
    # aqui vamos implementar cálculo de área geométrica depois

elif opcao == 4:
    caixa_msg("Você escolheu calcular insumos")
    # aqui vamos implementar cálculo de insumos depois

elif opcao == 5:
    caixa_msg(" ◆ ◇ ◈ Saindo do programa ◈ ◇ ◆ ")
