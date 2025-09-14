# ================================================================
# Projeto FarmTech - Análise de Dados em R
# Esse script lê os arquivos gerados pelo Python (culturas.csv e insumos.csv)
# e faz cálculos estatísticos simples + gráficos.
# ================================================================

# ---------- BLOCO 1: Carregar bibliotecas ----------
# O ggplot2 serve para fazer gráficos bonitos.
library(ggplot2)

# ---------- BLOCO 2: Ler os arquivos gerados pelo Python ----------
# Aqui eu mando o R abrir os arquivos CSV que estão na pasta "data/"
culturas <- read.csv("data/culturas.csv", stringsAsFactors = FALSE)
insumos  <- read.csv("data/insumos.csv", stringsAsFactors = FALSE)

# Conferindo as tabelas carregadas
print("Dados de culturas:")
print(culturas)
print("Dados de insumos:")
print(insumos)

# ---------- BLOCO 3: Estatísticas de Áreas ----------
# Calcular média e desvio padrão da área (em hectares) por cultura
estatisticas_area <- aggregate(area_ha ~ cultura, data = culturas,
                               FUN = function(x) c(media = mean(x), desvio = sd(x)))

# O aggregate retorna um formato meio estranho, então ajusto a tabela:
estatisticas_area <- do.call(data.frame, estatisticas_area)

print("📊 Estatísticas de Áreas (em hectares):")
print(estatisticas_area)

# ---------- BLOCO 4: Estatísticas de Insumos ----------
# Calcular média de quantidade de insumos por cultura/produto
estatisticas_insumos <- aggregate(quantidade ~ cultura + produto, data = insumos,
                                  FUN = mean)

print("📊 Estatísticas de Insumos (quantidade média):")
print(estatisticas_insumos)

# ---------- BLOCO 5: Gráficos ----------
# Gráfico 1: área média por cultura
ggplot(estatisticas_area, aes(x = cultura, y = area_ha.media, fill = cultura)) +
  geom_bar(stat = "identity") +
  labs(title = "Área média por cultura", y = "Área (ha)", x = "Cultura")

# Gráfico 2: quantidade média de insumos
ggplot(estatisticas_insumos, aes(x = cultura, y = quantidade, fill = produto)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Média de insumos aplicados", y = "Quantidade", x = "Cultura")

# ================================================================
# FIM DO SCRIPT
# ================================================================
