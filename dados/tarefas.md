1 - df: Visualização da tabela para noções gerais, nome das colunas, quantidade de linhas e colunas
----> Insight: já deu para ver um primeiro NaN em quantidade.

2 - df.info(): Conferir a quantidade de nulos e o tipo de dados conferindo com a vizualização anterior:
----> Insights: data_venda em formato object | quantidade e preço unitário tem nulos

3 - df.nunique()Conferir valores unicos, ver se bate com o df, achar suas categorias (discreto e continuo) e vizualizações das discretas.
----> Insight: data e id_vento são continuo, id_venda tem a mesma quantidade de linhas logo ele não se repete e pode ser o indice, o resto é discreto

4 - Vizualização dos valores em cada coluna e como se repetem e em que proporção:
----> Insights: 
* Data que mais se repete é 2024-05-15 (5x mais), data invalida (4)
* Os clientes são 30
* Notebook é o item mais vendido, tem 1 tablet e 2 smartphone escrito errado
* As categorias estão bem acirradas em repetição, mas celulares está na frente e periféricos atrás.
* Região Sudeste e Norte afrente, sul e sudeste atrás
* As quantidades transitam entre 1 e 10 sendo 8, 4 e 2 as que mais se repetem e 1 e 10 os que menos se repetem
* Os preços unitários variam entre 3500 e 120, os valores estão proximos mas o que mais aparece é 3500 e o que menos aparece 250
