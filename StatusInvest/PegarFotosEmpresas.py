from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import os
import requests


acoes = pd.read_csv("acoesListadasB3.csv")

driver = webdriver.Chrome()

for ticker in acoes["Ticker"]:
    try:

        driver.get("https://statusinvest.com.br/acoes/" + ticker)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.company-brand"))
        )

        data_img = element.get_attribute("data-img")

        if data_img.startswith("url("):

            image_path = data_img[4:-1]
        else:
            raise ValueError("Formato inesperado no atributo data-img")

        base_url = "https://statusinvest.com.br"
        image_url = base_url + image_path

        response = requests.get(image_url)
        if response.status_code == 200:

            image_name = ticker+".jpg"

            with open(os.path.join("Logos", image_name), "wb") as file:
                file.write(response.content)
            print(f"Imagem salva como {image_name}")
        else:
            print(f"Falha ao baixar a imagem. Código HTTP: {response.status_code} {image_url}")

            f = open("erros.txt", "a")
            f.write(f"Erro ao baixar imagem[{image_url}\n")
            f.close()

    except Exception as e:
        print(f"Erro ao tentar acessar o ativo {ticker}")

        f = open("erros.txt", "a")
        f.write(f"Erro ao acessar o ticker[{ticker}\n")
        f.close()

driver.quit()