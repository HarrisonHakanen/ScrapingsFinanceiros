from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import os
import re


acoes = pd.read_csv("acoesListadasB3.csv")
driver = webdriver.Chrome()



for ticker in acoes["Ticker"]:
    
    
    try:
        
        with open("ultimoAtivo.txt", "w") as arquivo:           
            arquivo.write("Ativo: "+ticker)
        
        
        driver.get("https://www.dadosdemercado.com.br/acoes/"+ticker+"/dividendos")
        
        dividendos_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"normal-table"))
        )
        
        body = dividendos_table.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME,"tr")
        
        
        tipo = []
        valor = []
        registro = []
        ex = []
        pagamento = []
        
        for tr in trs:
            
            tds = tr.find_elements(By.TAG_NAME,"td")
        
            
            count = 0
            for td in tds:
                
                if count == 0:
                    tipo.append(td.text)
                elif count == 1:
                    valor.append(td.text)
                elif count == 2:
                    registro.append(td.text)
                elif count == 3:
                    ex.append(td.text)
                elif count == 4:
                    pagamento.append(td.text)
                
                count +=1 
                
        dividendos = pd.DataFrame(list(zip(tipo,valor,registro,ex,pagamento)),columns=["Tipo","Valor","Registro","Ex","Pagamento"])
        dividendos.to_csv("dividendos\\"+ticker+".csv")
    
    
    except Exception as e:
        
        print(e)