import os
import csv
import time

# ---------- UTIL (funções de apoio) ----------
def caixa_msg(texto, largura=80):

    """
    Exibe uma mensagem dentro de uma caixa bonitinha no terminal.
    Usada para dar feedback visual (tipo banners).
    """

    print("\n" + "╔" + "═" * (largura - 2) + "╗")
    print("║" + texto.center(largura - 2) + "║")
    print("╚" + "═" * (largura - 2) + "╝")

def leia_cultura(msg="Digite a cultura (Milho/Cana): "):

    """
        Pergunta ao usuário qual cultura quer cadastrar (Milho ou Cana).
        Valida para não deixar digitar qualquer coisa.
        """

    while True:
        nome = input(msg).strip().lower()
        if nome in ("milho", "cana"):
            return nome.capitalize() # devolve formatado: "Milho" ou "Cana"
        caixa_msg("⚠️ Cultura inválida! Use apenas 'Milho' ou 'Cana'.")

def leia_float_positivo(msg):

    """
       Lê um número decimal (float) do usuário, garante que seja > 0.
       Substitui vírgula por ponto para evitar erro (ex: 2,5 -> 2.5).
       """

    while True:
        s = input(msg).strip().replace(",", ".")
        try:
            valor = float(s)
            if valor > 0:
                return valor
            caixa_msg("⚠️ O valor deve ser maior que zero.")
        except ValueError:
            caixa_msg("⚠️ Valor inválido! Digite um número (ex: 12.5).")

def leia_int_intervalo(msg, minimo, maximo):

    """
       Lê um número inteiro e só aceita se estiver dentro do intervalo dado.
       Usado para menus e escolhas de opções.
       """

    while True:
        s = input(msg).strip()
        try:
            v = int(s)
            if minimo <= v <= maximo:
                return v
            caixa_msg(f"⚠️ Valor fora do intervalo ({minimo} a {maximo}).")
        except ValueError:
            caixa_msg("⚠️ Digite um número inteiro válido.")

# ---------- I/O CSV (entrada e saída de arquivos) ----------
DATA_DIR = "data" # pasta onde os arquivos CSV vão ficar

def garantir_pasta():

    """
      Cria a pasta 'data' se ela não existir, para armazenar os CSVs.
    """

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def salvar_csvs(culturas, formas, areas, insumos):

    """
        Salva os dados atuais em dois arquivos CSV:
        - culturas.csv -> nome, forma geométrica, área (em ha)
        - insumos.csv -> insumos calculados por cultura
        """

    garantir_pasta()

    # ---- salvar culturas ----
    with open(os.path.join(DATA_DIR, "culturas.csv"), mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["cultura", "forma", "area_ha"])
        for c, forma, area in zip(culturas, formas, areas):
            writer.writerow([c, forma if forma else "", f"{area:.4f}" if area is not None else ""])

    # ---- salvar insumos ----
    with open(os.path.join(DATA_DIR, "insumos.csv"), mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["cultura", "produto", "quantidade", "unidade"])
        for i, lista in enumerate(insumos):
            cultura = culturas[i]
            for produto, quantidade, unidade in lista:
                writer.writerow([cultura, produto, f"{quantidade:.4f}", unidade])

def carregar_csvs():

    """
      Carrega dados de culturas e insumos dos arquivos CSV, se existirem.
      Retorna 4 listas paralelas:
      - culturas (nomes)
      - formas (geometria usada)
      - areas (em hectares)
      - insumos (lista de listas com produtos e quantidades)
      """

    culturas = []
    formas = []
    areas = []
    insumos = []
    if not os.path.exists(DATA_DIR):
        return culturas, formas, areas, insumos
    cult_file = os.path.join(DATA_DIR, "culturas.csv")
    insumo_file = os.path.join(DATA_DIR, "insumos.csv")

    # --- ler culturas ---
    if os.path.exists(cult_file):
        with open(cult_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                culturas.append(row.get("cultura", "").strip())
                formas.append(row.get("forma", "").strip() or None)
                a = row.get("area_ha", "").strip()
                areas.append(float(a) if a else None)

    # --- ler insumos ---
    if os.path.exists(insumo_file):
        insumos = [[] for _ in culturas] # cria listas vazias do mesmo tamanho
        with open(insumo_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cultura = row.get("cultura", "").strip()
                produto = row.get("produto", "").strip()
                quantidade = float(row.get("quantidade", "0") or 0)
                unidade = row.get("unidade", "").strip()
                if cultura in culturas:
                    idx = culturas.index(cultura)
                    insumos[idx].append((produto, quantidade, unidade))
    else:
        # if no insumo file, ensure insumos length matches culturas
        insumos = [[] for _ in culturas]
    return culturas, formas, areas, insumos

# ---------- LÓGICA (parte matemática/negócio) ----------
def calcular_area_por_forma():

    """
        Pergunta ao usuário qual forma geométrica quer usar para calcular a área:
        - Retângulo = base x altura
        - Triângulo = (base x altura)/2
        Depois converte de m² para hectares (1 ha = 10.000 m²).
        Retorna: (nome_da_forma, area_em_hectares, area_em_m2)

    """

    print("\nFormas geométricas disponíveis:")
    print("1 -> Retângulo (base x altura)")
    print("2 -> Triângulo (base x altura / 2)")
    forma = leia_int_intervalo("➔ Escolha a forma (1 ou 2): ", 1, 2)
    base_m = leia_float_positivo("📏 Base (em metros): ")
    altura_m = leia_float_positivo("📐 Altura (em metros): ")

    if forma == 1:
        area_m2 = base_m * altura_m
        nome_forma = "Retângulo"
    else:
        area_m2 = (base_m * altura_m) / 2
        nome_forma = "Triângulo"

    area_ha = area_m2 / 10000.0  # conversão para hectares
    return nome_forma, area_ha, area_m2



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

# ---------- MAIN (fluxo principal) ----------
def main():
    largura = 80
    # cabeçalho simples
    print("=" * largura)
    print("| Bem Vindo ao Sistema de Gerenciamento de Culturas |".center(largura))
    print("=" * largura)
    time.sleep(0.6)

    # tenta carregar dados de execuções anteriores
    culturas, formas, areas, insumos = carregar_csvs()

    # menu de opções
    menu = "  ◆ ◇ ◈ MENU PRINCIPAL ◈ ◇ ◆  "
    opcoes = [
        "1 -> Cadastrar Culturas",
        "2 -> Listar Culturas",
        "3 -> Calcular Área de Plantio (usar base/altura em metros)",
        "4 -> Calcular Insumos",
        "5 -> Atualizar Dados",
        "6 -> Deletar Dados",
        "7 -> Listar Insumos",
        "8 -> SALVAR & SAIR"
    ]

    opcao = 0
    while opcao != 8:
        # exibe menu
        print("\n" + "╔" + "═" * (largura - 2) + "╗")
        print("║" + menu.center(largura - 2) + "║")
        print("╠" + "═" * (largura - 2) + "╣")
        for item in opcoes:
            print("║" + item.center(largura - 2) + "║")
        print("╚" + "═" * (largura - 2) + "╝")

        opcao = leia_int_intervalo('➔ Digite a opção desejada (1 a 8): ', 1, 8)

        # ---- OPÇÃO 1: cadastrar cultura ----
        if opcao == 1:
            caixa_msg("Cadastro de Culturas")
            nome = leia_cultura()
            area = leia_float_positivo("📐 Área plantada (em hectares): ")
            culturas.append(nome)
            areas.append(area)
            formas.append(None)
            insumos.append([])
            caixa_msg(f"✅ {nome} cadastrada com área {area:.4f} ha.")

        # ---- OPÇÃO 2: listar culturas ----
        elif opcao == 2:
            caixa_msg("Listagem de Culturas")
            if not culturas:
                caixa_msg("📭 Nenhuma cultura cadastrada.")
            else:
                for i, (c, a) in enumerate(zip(culturas, areas), start=1):
                    forma_text = formas[i-1] if formas[i-1] else "—"
                    area_text = f"{a:.4f} ha" if a is not None else "—"
                    print(f"{i:02d}. {c:<8} | Área: {area_text} | Forma: {forma_text}")

        # ---- OPÇÃO 3: calcular área com base/altura ----
        elif opcao == 3:
            caixa_msg("Calcular Área de Plantio")
            if not culturas:
                caixa_msg("📭 Nenhuma cultura cadastrada.")
                continue
            for i, c in enumerate(culturas, start=1):
                print(f"{i}. {c}")
            escolha = leia_int_intervalo("➔ Escolha a cultura pelo número: ", 1, len(culturas)) - 1
            nome_forma, area_ha, area_m2 = calcular_area_por_forma()
            formas[escolha] = nome_forma
            areas[escolha] = area_ha
            caixa_msg(f"✅ Área de {culturas[escolha]}: {area_m2:.2f} m² = {area_ha:.4f} ha ({nome_forma})")

        # ---- OPÇÃO 4: calcular insumos ----
        elif opcao == 4:
            caixa_msg("Calcular Insumos")
            if not culturas:
                caixa_msg("📭 Nenhuma cultura cadastrada.")
                continue

            for i, c in enumerate(culturas, start=1):
                print(f"{i}. {c}")
            escolha = leia_int_intervalo("➔ Escolha a cultura pelo número: ", 1, len(culturas)) - 1
            if areas[escolha] is None:
                caixa_msg("⚠️ Área não calculada! Use a opção 3 primeiro ou atualize a área.")
                continue

            cultura = culturas[escolha]
            # regra fixa de exemplo: cada cultura tem insumo e taxa própria
            if cultura == "Milho":
                taxa = 20.0  # unidades por hectare
                unidade = "kg"
                produto = "Fertilizante NPK"
            else:  # Cana
                taxa = 30.0
                unidade = "L"
                produto = "Herbicida"

            total = areas[escolha] * taxa
            insumos[escolha].append((produto, total, unidade))
            caixa_msg(f"🌱 {total:.2f} {unidade} de {produto} para {cultura} (área {areas[escolha]:.4f} ha)")
            # salvar automático para persistência
            salvar_csvs(culturas, formas, areas, insumos)

        # ---- OPÇÃO 5: atualizar dados ----
        elif opcao == 5:
            caixa_msg("Atualizar Dados")
            if not culturas:
                caixa_msg("📭 Nenhuma cultura cadastrada.")
                continue
            for i, c in enumerate(culturas, start=1):
                print(f"{i}. {c}")
            escolha = leia_int_intervalo("➔ Escolha a cultura para atualizar pelo número: ", 1, len(culturas)) - 1
            nome = leia_cultura()
            area = leia_float_positivo("📐 Nova área (em hectares): ")
            culturas[escolha] = nome
            areas[escolha] = area
            formas[escolha] = None
            insumos[escolha] = [] # limpa insumos ao atualizar
            caixa_msg(f"✅ Cultura atualizada: {nome}, Área: {area:.4f} ha")
            salvar_csvs(culturas, formas, areas, insumos)

        # ---- OPÇÃO 6: deletar dados ----
        elif opcao == 6:
            caixa_msg("Deletar Dados")
            if not culturas:
                caixa_msg("📭 Nenhuma cultura cadastrada.")
                continue
            for i, c in enumerate(culturas, start=1):
                print(f"{i}. {c}")
            escolha = leia_int_intervalo("➔ Escolha a cultura para deletar pelo número: ", 1, len(culturas)) - 1
            nome = culturas[escolha]
            # remove de todas as listas paralelas
            del culturas[escolha]; del areas[escolha]; del formas[escolha]; del insumos[escolha]
            caixa_msg(f"✅ Cultura {nome} deletada com sucesso!")
            salvar_csvs(culturas, formas, areas, insumos)

        # ---- OPÇÃO 7: listar insumos ----
        elif opcao == 7:
            caixa_msg("Listagem de Insumos")
            if not culturas:
                caixa_msg("📭 Nenhuma cultura cadastrada.")
                continue
            for c, ins in zip(culturas, insumos):
                print(f"🌱 {c}:")
                if not ins:
                    print("   ➔ Nenhum insumo aplicado")
                else:
                    for prod, qt, un in ins:
                        print(f"   ➔ {qt:.2f} {un} de {prod}")

        # ---- OPÇÃO 8: salvar e sair ----
        elif opcao == 8:
            caixa_msg("Salvando dados e saindo... ✅")
            salvar_csvs(culturas, formas, areas, insumos)
            break

# Ponto de entrada: só executa main() se rodar diretamente (python farmtech.py)
if __name__ == "__main__":
    main()