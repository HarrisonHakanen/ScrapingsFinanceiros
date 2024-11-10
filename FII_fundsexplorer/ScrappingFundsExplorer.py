from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import os
import re



driver = webdriver.Chrome()
driver.get("https://www.fundsexplorer.com.br/funds")
fii_list = []

try:
    fundos = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "tickerBox__title"))
    )
    

    for fundo in fundos:
        texto = driver.execute_script("return arguments[0].textContent;", fundo)
        fii_list.append(texto.strip())
        
    fii_list_df = pd.DataFrame(fii_list,columns=["FII"])

    fii_list_df.to_csv("fii.csv")
    

finally:
    driver.quit()
    
    

