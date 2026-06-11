import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

def gerar_dataset_vendas(n_registros=150, seed=42):
    """Gera um dataset sintético de vendas com dados propositalmente sujos,
    incluindo valores nulos, strings sujas, datas inválidas e outliers."""
    random.seed(seed)
    np.random.seed(seed)
    produtos = ['Notebook', 'Smartphone', 'Tablet', 'Monitor', 'Teclado',
    'Mouse']
    precos = { 'Notebook': 3500, 'Smartphone': 2200, 'Tablet': 1800,
    'Monitor': 1200, 'Teclado': 250, 'Mouse': 120 }
    categorias = { "Notebook": "Computadores", "Smartphone": "Celulares",
    "Tablet": "Celulares", "Monitor": "Computadores", "Teclado": "Periféricos",
    "Mouse": "Periféricos" }
    regioes = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]
    clientes = [f"Cliente_{i:03d}" for i in range(1, 31)]
    data_inicio = datetime(2024, 1, 1)
    dados = []

    for i in range(n_registros):
        produto = random.choice(produtos)
        quantidade = random.randint(1, 10)
        preco = precos[produto]
        data = data_inicio + timedelta(days=random.randint(0, 364))
        # Inserindo dados intencionalmente sujos para limpeza
        if random.random() < 0.05:
            quantidade = None # valor nulo
        if random.random() < 0.04:
            preco = None # valor nulo
        if random.random() < 0.03:
            produto = " " + produto # espaço extra (string suja)
        data_str = data.strftime("%Y-%m-%d") if random.random() > 0.02 else "DATA INVALIDA"
        dados.append({
        "id_venda": i + 1,
        "data_venda": data_str,
        "cliente": random.choice(clientes),
        "produto": produto,
        "categoria": categorias.get(produto.strip(), "Outros"),
        "regiao": random.choice(regioes),
        "quantidade": quantidade,
        "preco_unitario": preco})
    return pd.DataFrame(dados)

df_bruto = gerar_dataset_vendas()
os.makedirs('dados/raw', exist_ok=True) # Adicionado para garantir que o diretório exista
df_bruto.to_csv("dados/raw/vendas.csv", index=False)
print(f"Dataset gerado com {len(df_bruto)} registros.")
print(df_bruto.head())
