import os
import pandas as pd

diretorio = "C:\\Users\\harri\\Documents\\Programacao\\Python\\InvestSite"

f = open("arquivoErros.txt", "r")


ativosComErro = []

encontrou = False
for tickerFolder in os.listdir(diretorio):
    
    if os.path.isdir(tickerFolder):
        
        qtd_arquivos = 0        
        for arquivo in os.listdir(diretorio+"\\"+tickerFolder):
            
            if ".csv" in arquivo:
                          
                qtd_arquivos += 1
        
    
        if qtd_arquivos < 6:
            
            print(tickerFolder+" tem "+str(qtd_arquivos))
            ativosComErro.append(tickerFolder)
        

ativosComErro_df = pd.DataFrame(ativosComErro,columns=["Ticker"])

ativosComErro_df.to_csv("ativosComErro.csv")