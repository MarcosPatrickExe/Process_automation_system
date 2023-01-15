import pandas as pd;
import os;

## IMPORTING DATA BASE
table = pd.read_csv( os.path.join(os.path.dirname(__file__), "data/telecom_users.csv"));
table = table.drop("Unnamed: 0", axis=1); # droping a column (axis=1) and not a row (axis=0) 
# table = table.drop("3", axis=0); # droping a row (axis=0) number three
# print(table);
print(table.info()); # Show details of the column (number and data type of columns and number de non-nullable data)



## DATA PROCESS:
# corrigindo coluna "TotalGasto" para que seus dados se tornem do tipo Float64 e nao mais Object (texto)

table["TotalGasto"] = pd.to_numeric(table["TotalGasto"], errors="coerce"); # 'coerce' forca a conversao de string para numerico, diferente do 'ignore' e 'raise'
print(table.info()); # Show details of the column (number and data type of columns and number de non-nullable data)



## RESOLVENDO VALORES VAZIOS:
# Excluir colunas que tem TODOS os valores/linhas/registros vazios:
table = table.dropna(how="all", axis=1);
                   # how="any" ou seja, apague colunas que tem todos os valores vazios

# Excluir linhas que tem pelo penos 1 valor vazio:
table = table.dropna(how="any", axis=0);
                    # how="any" ou seja, apague linhas que tem pelo menos um valor vazio

# OBS: o metodo 'dropna' eh um metodo especial que apaga colunas e linhas com base nos seus dados/registros/tuplas
print(table.info());



## ANÁLISE INICIAL:
print(table["Churn"].value_counts(normalize=True ));
                                # com o parâmetro opcional 'normalize=True' retorna os valores em porcentagem

