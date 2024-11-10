import os
import pandas as pd

diretorio = "C:\\Users\\harri\\Documents\\Programacao\\Python\\InvestSite"

f = open("arquivoErros.txt", "r")


tickers_df = pd.read_csv("acoesListadasB3.csv")


ativosComErro = []
for index, row in tickers_df.iterrows():
    
    print(row)
    encontrou = False
    for tickerFolder in os.listdir(diretorio):
        
        if row["Ticker"] == tickerFolder:
            
            encontrou = True
    
    if not encontrou:
                
        ativosComErro.append(row["Ticker"])
        
ativosComErro_df = pd.DataFrame(ativosComErro,columns=["Ticker"])

ativosComErro_df.to_csv("ativosComErro.csv")