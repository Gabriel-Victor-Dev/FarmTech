🌱 FarmTech Solutions

Bem-vindo ao projeto da Startup FarmTech Solutions!
Sistema para gerenciamento de culturas agrícolas, utilizando Python para cadastro e cálculo de insumos e R para análise estatística.

farmtech/
├── python-app/        # Código Python
│
└── main.py        # Programa principal: cadastro, cálculo de áreas e insumos
├── r-app/             # Código R
│   └── analise.R      # Script R para calcular estatísticas básicas
├── data/              # Arquivos CSV gerados pelo Python
│   ├── culturas.csv
│   └── insumos.csv
└── README.md          # Este arquivo

⚙️ Como Rodar
💻 Python

Abra o terminal na pasta python-app/

Execute: python main.py

Use o menu para:

Cadastrar culturas 🌾

Calcular áreas (Retângulo/Triângulo) 📐

Calcular insumos 🌱

Arquivos CSV serão gerados automaticamente em ../data/

📊 R

Abra o terminal na pasta r-app/

Execute: Rscript analise.R

O script vai ler os CSVs gerados pelo Python e mostrar:

Média das áreas e insumos 📊

Desvio padrão ⚡

Total de insumos necessários 🧪

📌 Funcionalidades

✅ Cadastro de culturas (Milho e Cana)
✅ Cálculo de áreas plantadas (Retângulo e Triângulo)
✅ Cálculo de insumos por cultura
✅ Exportação automática para CSV
✅ Análise estatística em R

💡 Observações

Os arquivos CSV gerados pelo Python estão em data/ e são usados pelo R.

Versionamento com Git: faça commits frequentes e sincronize com o GitHub.

Este projeto simula um ambiente de desenvolvimento colaborativo em equipe.

🔧 Dicas FarmTech

Mantenha Python e R organizados em python-app/ e r-app/

Use mensagens claras nos commits (ex: git commit -m "Adiciona cálculo de insumos")

Sempre verifique os CSVs gerados antes de rodar o R