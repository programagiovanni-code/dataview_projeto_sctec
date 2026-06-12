## MiniProjeto avaliato SCTEC - DataView
## O que o projeto analisa
## Objetivos
## Ferramentas utilizadas
- Python 3.10+
- VS Code
- Bibliotecas: pandas, numpy, matplotlib e seaborn.
- Módulos: re, datetime, os, random
- GitHub para versionamento
## Instruções
1. Instale o Python 3.10+ e o VS Code.
2. Instale as bibliotecas mencionadas em "Ferramentas utilizadas:
3. Importe as bibliotecas e módulos mencionados em 'Ferramentas utilizadas'
## Estrutura do projeto
projeto/
|-- data/
| |-- raw/ # Dataset bruto gerado/baixado
| |-- processed/
| | |-- v1_com_outliers/ # Dados de limpeza geral, outliers mantidos
| | |-- v2_outliers_tratado/ # Limpeza v1 + tratamento de outliers
| |-- final/ # Dataset escolhido para uso futuro
|-- notebooks/
| |-- dataview.ipynb # Notebook principal de EDA
|-- outputs/
| |-- metricas_por_mes.csv
| |-- segmentacao_clientes.csv
| |-- estatisticas_gerais.json
| |-- graficos/
|-- README.md
## Video explicativo

## PARA MINHA ORGANIZAÇÃO
Extensões e ferramentas utilizadas: ??

1) Foi criado um script para a criação aleatória de um arquivo CSV com valores randomizados incluindo 'erros propositais' para treino de tratamento de dados.
--> Alterações do código sctec: import os

item 4.1 (data/raw, data/processed com v1 e v2, e data/final).

Colocar no README
--> objetivo do projeto,
--> Instruções de instalação e execução
--> Conceitos de Python utilizados 
--> Análise de dados aplicados
--> Links para o repositório e vídeo

Pastas do projeto: data/raw, data/processed com v1 e v2, e data/final

!!Dados que tem a mesma quantidade de elementos (ex: data) usar um contador

Vou ter que estudar: outliers (IQR ou z-score)