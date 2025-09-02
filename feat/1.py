''' ATIVIDADE 1 / Raízes da Inteligência - Preparando o terreno '''

# Banner
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

# >CABEÇALHO SECUNDÁRIO

titulo2 = "| ◈ Bem Vindo ao Sistema de Gerenciamento de Culturas ◈ |"
largura = 80

print("=" * largura)
print(titulo2.center(largura))
print("=" * largura)

# >LISTA PARA ARMAZENAR DADOS

culturas = [] # nomes das culturas
formas = [] # figura geométrica para cada cultura (Retângulo ou Círculo)
areas = [] # áreas plantadas em hectares
insumos = [] # insumos aplicados

# >MENU PRINCIPAL E VALIDAÇÃO DE OPÇÃO

opcao = 0 # >Variável de controle do menu

while opcao != 5:
    # >MENU
    menu = " ⚙  MENU PRINCIPAL ⚙ "
    largura2 = 80

    print(menu.center(largura2))
    print("=" * largura2)