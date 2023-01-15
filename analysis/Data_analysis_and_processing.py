import pandas as pd;
import os;

##=============== IMPORTING DATA BASE =================
table = pd.read_csv( os.path.join(os.path.dirname(__file__), "data/telecom_users.csv"));
table = table.drop("Unnamed: 0", axis=1); # droping a column (axis=1) and not a row (axis=0) 
# table = table.drop("3", axis=0); # droping a row (axis=0) number three
# print(table);
print(table.info()); # Show details of the column (number and data type of columns and number de non-nullable data)



##=============== DATA PROCESS: =================
# corrigindo coluna "TotalGasto" para que seus dados se tornem do tipo Float64 e nao mais Object (texto)

table["TotalGasto"] = pd.to_numeric(table["TotalGasto"], errors="coerce"); # 'coerce' forca a conversao de string para numerico, diferente do 'ignore' e 'raise'
print(table.info()); # Show details of the column (number and data type of columns and number de non-nullable data)



##=============== RESOLVENDO VALORES VAZIOS: =================
# Excluir colunas que tem TODOS os valores/linhas/registros vazios:
table = table.dropna(how="all", axis=1);
                   # how="any" ou seja, apague colunas que tem todos os valores vazios

# Excluir linhas que tem pelo penos 1 valor vazio:
table = table.dropna(how="any", axis=0);
                    # how="any" ou seja, apague linhas que tem pelo menos um valor vazio

# OBS: o metodo 'dropna' eh um metodo especial que apaga colunas e linhas com base nos seus dados/registros/tuplas
print(table.info());



##=============== ANÁLISE INICIAL: ===============
print(table["Churn"].value_counts(normalize=True ));
                                # com o parâmetro opcional 'normalize=True' retorna os valores em porcentagem


print(table["Churn"].value_counts(normalize=True).map("{:.2%}".format)  );
                                                # Formatando a porcetagem que representam a contagem de cancelamentos dos clientes



##=============== ANÁLISE DETALHADA DOS DADOS A PARTIR DA COMPARACAO DA COLUNA "Churn" COM OUTRAS ===============
import plotly.express as px; # 'plotly' eh a biblioteca necessaria para utilizar gráficos 

for column in table.columns:
    graph= px.histogram( data_frame=table, x=column, color="Churn", text_auto=True);
                        # 'data_frame' é a base de dados, 'x' é o nome da coluna que sera exibida no grafico, 'color' é a coluna que ficará em baixo (eino X horizontal)
    # OUTROS TIPO DE GRÁFICOS:
    # px.barplot
    # px.pie/piechart

    graph.show(); 
    # Exibe o grafico. Caso esteja rodando o corido no Jupyter, o grafico será gerado na propria janela, 
    # enquanto que em outro editor, o gráfico será exibido no browser atraves de um localhost (127.0.0.1:53276)



## CONCLUSOES A PARTIR DA ANALISE DOS DADOS:
"""
- Clientes que tem familias mariores tendem a cancelar menos
    - Promocoes diferencias para mais pessoas da mesma familia
- Os clientes nos primeiros meses tem uma tencendia muito maior a cancelar
    - Poder ser algum marketing intenso
    - Pode ser que a experiencia nos primeiros meses seja ruim
    - Posso fazer uma promocao em que nos primeiros meses do ano eh mais barato
- Tem algum problema no servico de fibra     
- Quanto mais servicos o cliente tem, menos ele cancela
    - Podemos oferecer mais servicos de graca ou por um preco muito menor
- Quase todos os cancelamentos estao no contrato mensal
    - Oferece desconto no anual, no de 2 anos
- No boleto o cancelamento é muito maior, oferece desconto no cartal
"""
