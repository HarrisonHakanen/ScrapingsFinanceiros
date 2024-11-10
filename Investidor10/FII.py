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

ticker_list = []
company_list = []

total_pages = 15
current_page = 1

try:

    for i in range(1,total_pages):

        if(i == 0):
            driver.get("https://investidor10.com.br/fiis/")
        else:
            driver.get("https://investidor10.com.br/fiis/?page="+str(i))


        empresas = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "actions-card"))
        )

        for empresa in empresas:

            ticker_name = empresa.find_element(By.CLASS_NAME,"ticker-name")
            ticker_name_text = driver.execute_script("return arguments[0].textContent;", ticker_name)

            company_name = empresa.find_element(By.CLASS_NAME,"actions-title")
            company_name_text = driver.execute_script("return arguments[0].textContent;", company_name)

            ticker_list.append(ticker_name_text.strip())
            company_list.append(company_name_text.strip())

    fiis = list(zip(ticker_list, company_list))
    df = pd.DataFrame(fiis, columns = ['Ticker', 'Nome'])
    df.to_csv("fii.csv")

finally:
    driver.quit()
    
    

