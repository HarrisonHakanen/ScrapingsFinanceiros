import os
import pandas as pd

diretorio = "C:\\Users\\harri\\Documents\\Programacao\\Python\\InvestSite"
f = open("arquivoErros.txt", "r")

ativosComErro = []
for x in f:
    if "Ativo" in x:
        linhaSplit = x.split(":")
        ativo = linhaSplit[1].replace(" ","").replace("\n","")
        encontrou = False
        
        for tickerFolder in os.listdir(diretorio):
            
            if ativo == tickerFolder:
                encontrou = True
                    
                    
        if encontrou == False:
            ativosComErro.append(ativo)
          
ativosComErro = sorted(set(ativosComErro))
ativosDf = pd.DataFrame(ativosComErro,columns=["Ticker"])

ativosDf.to_csv("ativosComErro.csv")