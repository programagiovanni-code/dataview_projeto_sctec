# Análise de Vendas e Comportamento de Clientes

## 📌 Visão Geral
Este projeto consiste na estruturação de um pipeline completo de análise de dados focado em vendas varejistas. O fluxo engloba desde a geração e extração dos dados brutos até a limpeza, tratamento de outliers, engenharia de atributos (features) e visualização de métricas de Business Intelligence (BI).

## 📂 Estrutura do Projeto

O repositório está organizado de forma modular para separar as etapas de Engenharia de Dados e Análise Exploratória:

* **`csv_vendas_maker.py`**: Script responsável por gerar/simular a base de dados bruta original.
* **`funcoes.py`**: Módulo contendo funções auxiliares, como o algoritmo baseado em Intervalo Interquartil (IQR) para o tratamento paramétrico de outliers.
* **`explorar_dados.ipynb`**: Notebook dedicado à etapa de ETL (Extração, Transformação e Carga). Realiza a higienização de valores nulos, padronização de datas, remoção de anomalias e geração da coluna de faturamento (`valor_total`).
* **`df_bi.ipynb`**: Notebook de Análise de Negócios e Dataviz. Contém agregações financeiras (agrupamento temporal e geográfico) e a categorização inteligente dos clientes (Tiers: Bronze, Prata e Ouro).
* **Base de Dados**: 
    * `vendas.csv`: Dataset bruto original.
    * `vendas_tratado.csv` / `vendas_tratado.json`: Datasets processados e prontos para consumo por modelos de IA ou dashboards.

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python 3.x**
* **Pandas:** Manipulação, agregação e estruturação de DataFrames.
* **NumPy:** Operações matemáticas e lógicas condicionais (`np.select`).
* **Matplotlib & Seaborn:** Construção das visualizações de dados (gráficos de barras agrupadas, linhas temporais, eixos duplos e grids de pizza).

## 🚀 Como Executar o Projeto

1. Certifique-se de ter as bibliotecas necessárias instaladas rodando o seguinte comando no seu terminal:
   `pip install pandas numpy matplotlib seaborn`

2. Execute o notebook `explorar_dados.ipynb` para processar a base bruta (`vendas.csv`) e gerar os arquivos tratados na pasta de destino.

3. Execute o notebook `df_bi.ipynb` para renderizar os painéis analíticos e tabelas de segmentação.

## 📊 Principais Entregas Analíticas
* **Sazonalidade:** Evolução do faturamento mensal, trimestral e semestral.
* **Desempenho de Produto/Categoria:** Identificação dos itens de maior receita e volume de saída.
* **Análise Geográfica:** Distribuição percentual de volume e clientes por região mapeada.
* **Segmentação de Clientes:** Mapeamento do Ticket Médio/Total Gasto e classificação automática (RFM simplificado) em camadas de fidelidade.

---
*Projeto desenvolvido como requisito avaliativo para o Módulo 1 (S08) do curso de Fundamentos de Dados, Programação e Análise Preditiva com Python.*