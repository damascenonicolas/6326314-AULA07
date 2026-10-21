# Sistema de Consulta de Desempenho Acadêmico

Este projeto consiste em um sistema desenvolvido em Python para extração e análise de desempenho acadêmico a partir dos dados de respostas exportados de formulários (Google Forms / Excel).

## Funcionalidades
- Leitura automática de dados de planilhas Excel (`.xlsx`).
- Busca individualizada de alunos via **RA**.
- Exibição de notas das avaliações regimentais (`Nota 1`, `Nota 2`) e dos Trabalhos Formativos (`TF01`, `TF02`).
- Cálculo automático da **Média Final** (Média Simples das 4 notas).
- Determinação da situação final do aluno (**APROVADO** para média ≥ 6.0 ou **REPROVADO** para média < 6.0).

## Estrutura do Projeto
```text
├── dados/
│   └── resultados.xlsx     # Planilha de respostas exportada
├── src/
│   └── consulta.py         # Script principal de busca e processamento
├── .gitignore              # Arquivos ignorados pelo Git
├── README.md               # Documentação do projeto
└── requirements.txt        # Dependências do projeto