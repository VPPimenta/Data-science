# %%
#importar as bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import seaborn as sns

# %%

#importar o dataset da pasta de origem. // dataset do kaggle sobre emprestimos bancarios
df = pd.read_csv('D:/DS_Vin/bankloan.csv')
df.head



# %%
#tratamento dos dados da tabela   //  Remoção de colunas sem valores e valores indesejados
df = df.drop(['Securities.Account', 'ZIP.Code', 'CD.Account'], axis=1) #Removendo Colunas que não utilizaremos na analise de dados
df = df.sort_values("Income") #Ordenando o dataframe pela renda
df



# %%
#tratar dados nulos e não utilizaveis criando um novo dataset removendo as linhas ou fazendo a médias dos valores para completar as lacunas

#Analisar correlação entre dados da tabela
sns.heatmap(df.corr())



# %%
#criar conjunto de dados para analise

df["Grupo_renda"] = pd.cut(df["Income"], [0, 20, 50, 70, 150, 1000],
       labels=["Baixa_Renda", "Classe_média_baixa", "Classe_Média", "Rico", "Super Rico"], ordered=False)

df["Grupo_idade"] = pd.cut(df["Age"], [18, 25, 33, 45, 60, 100],
       labels=["18-25", "25-33", "33-45", "45-60", "60+"], ordered=False)

#agrupar os dados (Dados em DF groupby)
df.sort_values("Grupo_renda")
df_renda = df.drop(["Grupo_idade"], axis = 1) 
df_renda = df_renda.groupby("Grupo_renda")


df_idade = df.drop(["Grupo_renda"], axis = 1) 
df_idade = df_idade.groupby("Grupo_idade")



# %%
#plotando e analisando
plt.figure(figsize=(10, 8)) 
sns.boxplot(x='Personal.Loan', 
            y='Income', 
            data=df) 
plt.ylabel("Renda", size=14) 
plt.xlabel("Emprestimo liberado", size=14) 
plt.title("Bank", size=18)

# %%
#plotando e analisando
plt.figure(figsize=(10, 8)) 
sns.boxplot(x='Online', 
            y='Education', 
            data=df) 
plt.ylabel("Educação", size=14) 
plt.xlabel("Conta Online", size=14) 
plt.title("Bank", size=18)

# %%
plt.figure(figsize=(10, 8)) 
sns.boxplot(x='Grupo_renda', 
            y='Mortgage', 
            data=df) 
plt.ylabel("Financiamento", size=14) 
plt.xlabel("Grupo", size=14) 
plt.title("Bank", size=18)
df_renda["Mortgage"].mean()

# %%
plt.figure(figsize=(10, 8)) 
sns.boxplot(x='Grupo_renda', 
            y='CCAvg', 
            data=df) 
plt.ylabel("Score Cartão", size=14) 
plt.xlabel("Grupo", size=14) 
plt.title("Bank", size=18)
df_renda["CCAvg"].mean()

# %%
plt.figure(figsize=(10, 8)) 
sns.boxplot(x='Grupo_idade', 
            y='Mortgage', 
            data=df) 
plt.ylabel("Financiamento", size=14) 
plt.xlabel("Grupo", size=14) 
plt.title("Bank", size=18)
df_idade["Mortgage"].mean()

