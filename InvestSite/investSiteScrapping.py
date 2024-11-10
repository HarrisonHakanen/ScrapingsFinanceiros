from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import os
import re


def resumoEmpresa(driver):
    data = []
    empresa = []
    razaoSocial = []
    situacao_registro = []
    situacao_emissor = []
    segmento_listagem = []
    atividade = []
    volume_financeiro = []
    setor = []
    subsetor = []
    segmento = []
    indices = []


    market_cap_empresa = []
    divdend_yield = []

    tabelaNome = "tabela_resumo_empresa"

    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, tabelaNome))
    )

    body = tabela.find_element(By.TAG_NAME, "tbody")
    trs = body.find_elements(By.TAG_NAME, "tr")

    for tr in trs:

        esquerda = tr.find_element(By.CLASS_NAME, "esquerda")
        direita = tr.find_element(By.CLASS_NAME, "direita")

        if esquerda.text == "Empresa":
            empresa.append(direita.text)

        elif esquerda.text == "Razão Social":
            razaoSocial.append(direita.text)

        elif esquerda.text == "Situação Registro":
            situacao_registro.append(direita.text)

        elif esquerda.text == "Situação Emissor":
            situacao_emissor.append(direita.text)

        elif esquerda.text == "Segmento de Listagem":
            segmento_listagem.append(direita.text)

        elif esquerda.text == "Atividade":
            atividade.append(direita.text)

        elif esquerda.text == "Volume Financeiro Transacionado":
            volume_financeiro.append(direita.text)

        elif esquerda.text == "Setor":
            setor.append(direita.text)

        elif esquerda.text == "Subsetor":
            subsetor.append(direita.text)

        elif esquerda.text == "Segmento":
            segmento.append(direita.text)

        elif esquerda.text == "Participação em Índices":
            indices.append(direita.text)





    return pd.DataFrame(
        zip(empresa,razaoSocial,situacao_registro,situacao_emissor,segmento_listagem,atividade,
            volume_financeiro,setor,subsetor,segmento,indices),
        columns=["empresa","razaoSocial","situacao_registro","situacao_emissor","segmento_listagem",
                 "atividade","volume_financeiro","setor","subsetor","segmento","indices"])


def resumoEmpresaPrecosRelativos(driver):
    
    data = []
    preco_lucro = []
    preco_vpa = []
    preco_receita_liq = []
    preco_fco = []
    preco_ativo_total = []
    preco_fcf = []
    preco_ebit = []
    preco_capital_giro = []
    ev_ebit = []
    ev_ebitda = []
    preco_ncav = []
    ev_receita_liquida = []
    ev_fcf = []
    ev_ativo_total = []

    market_cap_empresa = []
    divdend_yield = []
    
    tabelaNome = "tabela_resumo_empresa_precos_relativos"
    
    
    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, tabelaNome))
    )
    
    body = tabela.find_element(By.TAG_NAME, "tbody")
    trs = body.find_elements(By.TAG_NAME,"tr")
    
    
    for tr in trs:
        
        esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
        direita = tr.find_element(By.CLASS_NAME,"direita")
        
        if esquerda.text == "Preço/Lucro":
            preco_lucro.append(direita.text)
            
        elif esquerda.text == "Preço/VPA":
            preco_vpa.append(direita.text)
            
        elif esquerda.text == "Preço/Receita Líquida":
            preco_receita_liq.append(direita.text)
        
        elif esquerda.text == "Preço/FCO":
            preco_fco.append(direita.text)

        elif esquerda.text == "Preço/FCF":
            preco_fcf.append(direita.text)
            
        elif esquerda.text == "Preço/Ativo Total":
            preco_ativo_total.append(direita.text)

        elif esquerda.text == "Preço/EBIT":
            preco_ebit.append(direita.text)

        elif esquerda.text == "Preço/Capital Giro":
            preco_capital_giro.append(direita.text)

        elif esquerda.text == "EV/EBIT":
            ev_ebit.append(direita.text)

        elif esquerda.text == "EV/EBITDA":
            ev_ebitda.append(direita.text)

        elif esquerda.text == "Preço/NCAV":
            preco_ncav.append(direita.text)

        elif esquerda.text == "EV/Receita Líquida":
            ev_receita_liquida.append(direita.text)

        elif esquerda.text == "EV/FCF":
            ev_fcf.append(direita.text)

        elif esquerda.text == "EV/Ativo Total":
            ev_ativo_total.append(direita.text)

        elif esquerda.text == "Market Cap Empresa":
            market_cap_empresa.append(direita.text
                                      )
        elif esquerda.text == "Dividend Yield":
            divdend_yield.append(direita.text)
    
    
    select_element = tabela.find_element(By.CLASS_NAME, "data_tabela")
    select_object = Select(select_element)
    
    
    all_options = select_object.options
    current_selected = select_object.first_selected_option
    current_index = all_options.index(current_selected)
    
    
    data.append(all_options[0].text)
    
    while current_index < len(all_options) - 1:
        
        print(current_index)
        
        data.append(all_options[current_index + 1].text)
        
        next_option = all_options[current_index + 1]
        next_option.click()
        
        current_index +=1
        
        time.sleep(1)
        
        tabela = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, tabelaNome))
        )
        
        body = tabela.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME,"tr")
        
        
        for tr in trs:
            
            esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
            direita = tr.find_element(By.CLASS_NAME,"direita")

            if esquerda.text == "Preço/Lucro":
                preco_lucro.append(direita.text)

            elif esquerda.text == "Preço/VPA":
                preco_vpa.append(direita.text)

            elif esquerda.text == "Preço/Receita Líquida":
                preco_receita_liq.append(direita.text)

            elif esquerda.text == "Preço/FCO":
                preco_fco.append(direita.text)

            elif esquerda.text == "Preço/FCF":
                preco_fcf.append(direita.text)

            elif esquerda.text == "Preço/Ativo Total":
                preco_ativo_total.append(direita.text)

            elif esquerda.text == "Preço/EBIT":
                preco_ebit.append(direita.text)

            elif esquerda.text == "Preço/Capital Giro":
                preco_capital_giro.append(direita.text)

            elif esquerda.text == "EV/EBIT":
                ev_ebit.append(direita.text)

            elif esquerda.text == "EV/EBITDA":
                ev_ebitda.append(direita.text)

            elif esquerda.text == "Preço/NCAV":
                preco_ncav.append(direita.text)

            elif esquerda.text == "EV/Receita Líquida":
                ev_receita_liquida.append(direita.text)

            elif esquerda.text == "EV/FCF":
                ev_fcf.append(direita.text)

            elif esquerda.text == "EV/Ativo Total":
                ev_ativo_total.append(direita.text)

            elif esquerda.text == "Market Cap Empresa":
                market_cap_empresa.append(direita.text
                                          )
            elif esquerda.text == "Dividend Yield":
                divdend_yield.append(direita.text)



    return pd.DataFrame(zip(data,preco_lucro,preco_vpa,preco_receita_liq,preco_fco,preco_fcf,preco_ativo_total,preco_ebit,
        preco_capital_giro,ev_ebit,ev_ebitda,preco_ncav,ev_receita_liquida,ev_fcf,ev_ativo_total,
        market_cap_empresa,divdend_yield),
                 columns=["data","preco_lucro","preco_vpa","preco_receita_liq","preco_fco","preco_fcf",
                          "preco_ativo_total","preco_ebit","preco_capital_giro","ev_ebit","ev_ebitda",
                          "preco_ncav","ev_receita_liquida","ev_fcf","ev_ativo_total",
                          "market_cap_empresa","divdend_yield"])


def resumoEmpresaDre12Meses(driver):
    
    data = []
    receita_liquida = []
    resultado_bruto = []
    ebit = []
    depreciacao = []
    ebitda = []
    lucro_liquido = []
    lucro_acao = []
    
    tabelaNome = "tabela_resumo_empresa_dre_12meses"
    
    
    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, tabelaNome))
    )
    
    body = tabela.find_element(By.TAG_NAME, "tbody")
    trs = body.find_elements(By.TAG_NAME,"tr")
    
    
    for tr in trs:
        
        esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
        direita = tr.find_element(By.CLASS_NAME,"direita")
        
        if esquerda.text == "Receita Líquida":            
            receita_liquida.append(direita.text)
            
        elif esquerda.text == "Resultado Bruto":
            resultado_bruto.append(direita.text)
            
        elif esquerda.text == "EBIT":
            ebit.append(direita.text)
        
        elif esquerda.text == "Depreciação e Amortização":
            depreciacao.append(direita.text)
            
        elif esquerda.text == "EBITDA":
            ebitda.append(direita.text)
            
        elif esquerda.text == "Lucro Líquido":
            lucro_liquido.append(direita.text)
            
        elif esquerda.text == "Lucro/Ação":
            lucro_acao.append(direita.text)
            
    
    
    select_element = tabela.find_element(By.CLASS_NAME, "data_tabela")
    select_object = Select(select_element)
    
    
    all_options = select_object.options
    current_selected = select_object.first_selected_option
    current_index = all_options.index(current_selected)
    
    data.append(all_options[0].text)
    
    
    while current_index < len(all_options) - 1:
        
        print(current_index)
        
        data.append(all_options[current_index + 1].text)
        
        next_option = all_options[current_index + 1]
        next_option.click()
        
        current_index +=1
        
        time.sleep(1)
        
        tabela = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, tabelaNome))
        )
        
        body = tabela.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME,"tr")
        
        
        for tr in trs:
            
            esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
            direita = tr.find_element(By.CLASS_NAME,"direita")
            
            if esquerda.text == "Receita Líquida":
                receita_liquida.append(direita.text)
                
            elif esquerda.text == "Resultado Bruto":
                resultado_bruto.append(direita.text)
                
            elif esquerda.text == "EBIT":
                ebit.append(direita.text)
            
            elif esquerda.text == "Depreciação e Amortização":
                depreciacao.append(direita.text)
                
            elif esquerda.text == "EBITDA":
                ebitda.append(direita.text)
                
            elif esquerda.text == "Lucro Líquido":
                lucro_liquido.append(direita.text)
                
            elif esquerda.text == "Lucro/Ação":
                lucro_acao.append(direita.text)
                
        
        
        
    return pd.DataFrame(zip(data,receita_liquida,resultado_bruto,ebit, depreciacao,ebitda,
                            lucro_liquido,lucro_acao),
                 columns=["data","receita_liquida","resultado_bruto","ebit", "depreciacao","ebitda",
                                         "lucro_liquido","lucro_acao"])


def resumoEmpresaDre3Meses(driver):
    
    data = []
    receita_liquida = []
    resultado_bruto = []
    ebit = []
    depreciacao = []
    ebitda = []
    lucro_liquido = []
    lucro_acao = []
    
    tabelaNome = "tabela_resumo_empresa_dre_3meses"
    
    
    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, tabelaNome))
    )
    
    body = tabela.find_element(By.TAG_NAME, "tbody")
    trs = body.find_elements(By.TAG_NAME,"tr")
    
    
    for tr in trs:
        
        esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
        direita = tr.find_element(By.CLASS_NAME,"direita")
        
        if esquerda.text == "Receita Líquida":
            receita_liquida.append(direita.text)
            
        elif esquerda.text == "Resultado Bruto":
            resultado_bruto.append(direita.text)
            
        elif esquerda.text == "EBIT":
            ebit.append(direita.text)
        
        elif esquerda.text == "Depreciação e Amortização":
            depreciacao.append(direita.text)
            
        elif esquerda.text == "EBITDA":
            ebitda.append(direita.text)
            
        elif esquerda.text == "Lucro Líquido":
            lucro_liquido.append(direita.text)
            
        elif esquerda.text == "Lucro/Ação":
            lucro_acao.append(direita.text)
            
    
    
    select_element = tabela.find_element(By.CLASS_NAME, "data_tabela")
    select_object = Select(select_element)
    
    
    all_options = select_object.options
    current_selected = select_object.first_selected_option
    current_index = all_options.index(current_selected)
    
    data.append(all_options[0].text)
    
    
    while current_index < len(all_options) - 1:
        
        print(current_index)
        
        data.append(all_options[current_index + 1].text)
        
        next_option = all_options[current_index + 1]
        next_option.click()
        
        current_index +=1
        
        time.sleep(1)
        
        tabela = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, tabelaNome))
        )
        
        body = tabela.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME,"tr")
        
        
        for tr in trs:
            
            esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
            direita = tr.find_element(By.CLASS_NAME,"direita")
            
            if esquerda.text == "Receita Líquida":
                receita_liquida.append(direita.text)
                
            elif esquerda.text == "Resultado Bruto":
                resultado_bruto.append(direita.text)
                
            elif esquerda.text == "EBIT":
                ebit.append(direita.text)
            
            elif esquerda.text == "Depreciação e Amortização":
                depreciacao.append(direita.text)
                
            elif esquerda.text == "EBITDA":
                ebitda.append(direita.text)
                
            elif esquerda.text == "Lucro Líquido":
                lucro_liquido.append(direita.text)
                
            elif esquerda.text == "Lucro/Ação":
                lucro_acao.append(direita.text)
                
        
    return pd.DataFrame(zip(data,receita_liquida,resultado_bruto,ebit, depreciacao,ebitda,
                            lucro_liquido,lucro_acao),
                 columns=["data","receita_liquida","resultado_bruto","ebit", "depreciacao","ebitda",
                                         "lucro_liquido","lucro_acao"])



def resumoEmpresaMargensRetornos(driver):
    
    data = []
    ret_sem_cap_tang_ini = []
    ret_sem_cap_invest_ini = []
    ret_sem_cap_tang_ini_pre_imp = []
    ret_sem_cap_invest_ini_pre_imp = []
    ret_patrimonio_liq_inicial = []
    ret_sem_ativo_inicial = []
    margem_bruta = []
    margem_liquida = []
    margem_ebit = []
    margem_ebitda = []
    giro_ativo_inicial = []
    alavancagem_financeira = []
    passivo_patrimonio_liq = []
    divida_liquida_ebitda = []
    
    
    tabelaNome = "tabela_resumo_empresa_dre_3meses"
    
    
    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, tabelaNome))
    )
    
    body = tabela.find_element(By.TAG_NAME, "tbody")
    trs = body.find_elements(By.TAG_NAME,"tr")
    
    
    for tr in trs:
        
        esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
        direita = tr.find_element(By.CLASS_NAME,"direita")
        
        if esquerda.text == "Retorno s/ Capital Tangível Inicial":
            ret_sem_cap_tang_ini.append(direita.text)
            
        if esquerda.text == "Retorno s/ Capital Investido Inicial":
            ret_sem_cap_invest_ini.append(direita.text)
            
        if esquerda.text == "Retorno s/ Capital Tangível Inicial Pré-Impostos":
            ret_sem_cap_tang_ini_pre_imp.append(direita.text)
            
        if esquerda.text == "Retorno s/ Capital Investido Inicial Pré-Impostos":
            ret_sem_cap_invest_ini_pre_imp.append(direita.text)
            
        if esquerda.text == "Retorno s/ Patrimônio Líquido Inicial":
            ret_patrimonio_liq_inicial.append(direita.text)
        
        if esquerda.text == "Retorno s/ Ativo Inicial":
            ret_sem_ativo_inicial.append(direita.text)
            
        elif esquerda.text == "Margem Bruta":
            margem_bruta.append(direita.text)
        
        elif esquerda.text == "Margem Líquida":
            margem_liquida.append(direita.text)
            
        elif esquerda.text == "Margem EBIT":
            margem_ebit.append(direita.text)
        
        elif esquerda.text == "Margem EBITDA":
            margem_ebitda.append(direita.text)
        
        elif esquerda.text == "Giro do Ativo Inicial":
            giro_ativo_inicial.append(direita.text)
        
        elif esquerda.text == "Alavancagem Financeira":
            alavancagem_financeira.append(direita.text)
    
        elif esquerda.text == "Passivo/Patrimônio Líquido":
            passivo_patrimonio_liq.append(direita.text)
            
        elif esquerda.text == "Dívida Líquida/EBITDA":
            divida_liquida_ebitda.append(direita.text)
    
    
    select_element = tabela.find_element(By.CLASS_NAME, "data_tabela")
    select_object = Select(select_element)
    
    
    all_options = select_object.options
    current_selected = select_object.first_selected_option
    current_index = all_options.index(current_selected)
    
    data.append(all_options[0].text)
    
    
    while current_index < len(all_options) - 1:
        
        print(current_index)
        
        data.append(all_options[current_index + 1].text)
        
        next_option = all_options[current_index + 1]
        next_option.click()
        
        current_index +=1
        
        time.sleep(1)
        
        tabela = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, tabelaNome))
        )
        
        body = tabela.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME,"tr")
        
        
        for tr in trs:
            
            esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
            direita = tr.find_element(By.CLASS_NAME,"direita")
            
            
            
            if esquerda.text == "Retorno s/ Capital Tangível Inicial":
                ret_sem_cap_tang_ini.append(direita.text)
                
            if esquerda.text == "Retorno s/ Capital Investido Inicial":
                ret_sem_cap_invest_ini.append(direita.text)
                
            if esquerda.text == "Retorno s/ Capital Tangível Inicial Pré-Impostos":
                ret_sem_cap_tang_ini_pre_imp.append(direita.text)
                
            if esquerda.text == "Retorno s/ Capital Investido Inicial Pré-Impostos":
                ret_sem_cap_invest_ini_pre_imp.append(direita.text)
                
            if esquerda.text == "Retorno s/ Patrimônio Líquido Inicial":
                ret_patrimonio_liq_inicial.append(direita.text)
            
            if esquerda.text == "Retorno s/ Ativo Inicial":
                ret_sem_ativo_inicial.append(direita.text)
                
            elif esquerda.text == "Margem Bruta":
                margem_bruta.append(direita.text)
            
            elif esquerda.text == "Margem Líquida":
                margem_liquida.append(direita.text)
                
            elif esquerda.text == "Margem EBIT":
                margem_ebit.append(direita.text)            
            
            elif esquerda.text == "Margem EBITDA":
                margem_ebitda.append(direita.text)
            
            elif esquerda.text == "Giro do Ativo Inicial":
                giro_ativo_inicial.append(direita.text)
            
            elif esquerda.text == "Alavancagem Financeira":
                alavancagem_financeira.append(direita.text)
        
            elif esquerda.text == "Passivo/Patrimônio Líquido":
                passivo_patrimonio_liq.append(direita.text)
                
            elif esquerda.text == "Dívida Líquida/EBITDA":
                divida_liquida_ebitda.append(direita.text)
        
        
        
    return pd.DataFrame(zip(data,ret_sem_cap_tang_ini,ret_sem_cap_invest_ini,ret_sem_cap_tang_ini_pre_imp,
    ret_sem_cap_invest_ini_pre_imp,ret_patrimonio_liq_inicial,ret_sem_ativo_inicial,
    margem_bruta,margem_liquida,margem_ebit,margem_ebitda,giro_ativo_inicial,
    alavancagem_financeira,passivo_patrimonio_liq,divida_liquida_ebitda),
                 columns=["data","ret_sem_cap_tang_ini","ret_sem_cap_invest_ini","ret_sem_cap_tang_ini_pre_imp",
                 "ret_sem_cap_invest_ini_pre_imp","ret_patrimonio_liq_inicial","ret_sem_ativo_inicial",
                 "margem_bruta","margem_liquida","margem_ebit","margem_ebitda","giro_ativo_inicial",
                 "alavancagem_financeira","passivo_patrimonio_liq","divida_liquida_ebitda"])



def resumoEmpresaBp(driver):
    
    data = []
    ativo_total = []
    patrimonio_liq = []
    vlr_patrimonial_acao = []
    acoes_ordinarias = []
    acoes_preferenciais = []
    total = []
    acoes_ordinarias_tesouraria = []
    acoes_preferenciais_tesouraria = []
    total_tesouraria = []
    acoes_ordinarias_excecao = []
    acoes_preferenciais_excecao = []
    total_excecao = []
    
    tabelaNome = "tabela_resumo_empresa_bp"
    
    
    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, tabelaNome))
    )
    
    body = tabela.find_element(By.TAG_NAME, "tbody")
    trs = body.find_elements(By.TAG_NAME,"tr")
    
    
    for tr in trs:
        
        esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
        direita = tr.find_element(By.CLASS_NAME,"direita")
        
        if esquerda.text == "Ativo Total":
            ativo_total.append(direita.text)
            
        elif esquerda.text == "Patrimônio Líquido":
            patrimonio_liq.append(direita.text)
            
        elif esquerda.text == "Valor Patrimonial da Ação":
            vlr_patrimonial_acao.append(direita.text)
        
        elif esquerda.text == "Ações Ordinárias":
            acoes_ordinarias.append(direita.text)
            
        elif esquerda.text == "Ações Preferenciais":
            acoes_preferenciais.append(direita.text)
            
        elif esquerda.text == "Total":
            total.append(direita.text)
            
        elif esquerda.text == "Ações Ordinárias em Tesouraria":
            acoes_ordinarias_tesouraria.append(direita.text)
        
        elif esquerda.text == "Ações Preferenciais em Tesouraria":
            acoes_preferenciais_tesouraria.append(direita.text)
        
        elif esquerda.text == "Total em Tesouraria":
            total_tesouraria.append(direita.text)
        
        elif esquerda.text == "Ações Ordinárias (Exceto Tesouraria)":
            acoes_ordinarias_excecao.append(direita.text)
        
        elif esquerda.text == "Ações Preferenciais (Exceto Tesouraria)":
            acoes_preferenciais_excecao.append(direita.text)
        
        elif esquerda.text == "Total (Exceto Tesouraria)":
            total_excecao.append(direita.text)
    
    
    select_element = tabela.find_element(By.CLASS_NAME, "data_tabela")
    select_object = Select(select_element)
    
    
    all_options = select_object.options
    current_selected = select_object.first_selected_option
    current_index = all_options.index(current_selected)
    
    data.append(all_options[0].text)
    
    
    while current_index < len(all_options) - 1:
        
        print(current_index)
        
        data.append(all_options[current_index + 1].text)
        
        next_option = all_options[current_index + 1]
        next_option.click()
        
        current_index +=1
        
        time.sleep(1)
        
        tabela = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, tabelaNome))
        )
        
        body = tabela.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME,"tr")
        
        
        for tr in trs:
            
            esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
            direita = tr.find_element(By.CLASS_NAME,"direita")
            
            if esquerda.text == "Ativo Total":
                ativo_total.append(direita.text)
                
            elif esquerda.text == "Patrimônio Líquido":
                patrimonio_liq.append(direita.text)
                
            elif esquerda.text == "Valor Patrimonial da Ação":
                vlr_patrimonial_acao.append(direita.text)
            
            elif esquerda.text == "Ações Ordinárias":
                acoes_ordinarias.append(direita.text)
                
            elif esquerda.text == "Ações Preferenciais":
                acoes_preferenciais.append(direita.text)
                
            elif esquerda.text == "Total":
                total.append(direita.text)
                
            elif esquerda.text == "Ações Ordinárias em Tesouraria":
                acoes_ordinarias_tesouraria.append(direita.text)
            
            elif esquerda.text == "Ações Preferenciais em Tesouraria":
                acoes_preferenciais_tesouraria.append(direita.text)
            
            elif esquerda.text == "Total em Tesouraria":
                total_tesouraria.append(direita.text)
            
            elif esquerda.text == "Ações Ordinárias (Exceto Tesouraria)":
                acoes_ordinarias_excecao.append(direita.text)
            
            elif esquerda.text == "Ações Preferenciais (Exceto Tesouraria)":
                acoes_preferenciais_excecao.append(direita.text)
            
            elif esquerda.text == "Total (Exceto Tesouraria)":
                total_excecao.append(direita.text)
        
        
        
    return pd.DataFrame(zip(data,ativo_total,patrimonio_liq,vlr_patrimonial_acao, acoes_ordinarias,
                            acoes_preferenciais,acoes_preferenciais,total,acoes_ordinarias_tesouraria,
                            acoes_preferenciais_tesouraria,acoes_preferenciais_tesouraria,
                            total_tesouraria,acoes_ordinarias_excecao,acoes_preferenciais_excecao,
                            total_excecao),
                 columns=["data","ativo_total","patrimonio_liq","vlr_patrimonial_acao", "acoes_ordinarias",
                                         "acoes_preferenciais","acoes_preferenciais","total","acoes_ordinarias_tesouraria",
                                         "acoes_preferenciais_tesouraria","acoes_preferenciais_tesouraria",
                                         "total_tesouraria","acoes_ordinarias_excecao","acoes_preferenciais_excecao",
                                         "total_excecao"])


def resumoEmpresaFc12Meses(driver):
    
    data = []
    fluxo_caixa_operacional = []
    fluxo_caixa_investimentos = []
    fluxo_caixa_financiamentos = []
    fluxo_caixa_equivalentes = []
    
    tabelaNome = "tabela_resumo_empresa_fc_12meses"
    
    
    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, tabelaNome))
    )
    
    body = tabela.find_element(By.TAG_NAME, "tbody")
    trs = body.find_elements(By.TAG_NAME,"tr")
    
    
    for tr in trs:
        
        esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
        direita = tr.find_element(By.CLASS_NAME,"direita")
        
        if esquerda.text == "Fluxo de Caixa Operacional":
            fluxo_caixa_operacional.append(direita.text)
            
        elif esquerda.text == "Fluxo de Caixa de Investimentos":
            fluxo_caixa_investimentos.append(direita.text)
            
        elif esquerda.text == "Fluxo de Caixa de Financiamentos":
            fluxo_caixa_financiamentos.append(direita.text)
        
        elif esquerda.text == "Aumento (Redução) de Caixa e Equivalentes":
            fluxo_caixa_equivalentes.append(direita.text)
            
    
    
    select_element = tabela.find_element(By.CLASS_NAME, "data_tabela")
    select_object = Select(select_element)
    
    
    all_options = select_object.options
    current_selected = select_object.first_selected_option
    current_index = all_options.index(current_selected)
    
    data.append(all_options[0].text)
    
    
    while current_index < len(all_options) - 1:
        
        print(current_index)
        
        data.append(all_options[current_index + 1].text)
        
        next_option = all_options[current_index + 1]
        next_option.click()
        
        current_index +=1
        
        time.sleep(1)
        
        tabela = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, tabelaNome))
        )
        
        body = tabela.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME,"tr")
        
        
        for tr in trs:
            
            esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
            direita = tr.find_element(By.CLASS_NAME,"direita")
            
            if esquerda.text == "Fluxo de Caixa Operacional":
                fluxo_caixa_operacional.append(direita.text)
                
            elif esquerda.text == "Fluxo de Caixa de Investimentos":
                fluxo_caixa_investimentos.append(direita.text)
                
            elif esquerda.text == "Fluxo de Caixa de Financiamentos":
                fluxo_caixa_financiamentos.append(direita.text)
            
            elif esquerda.text == "Aumento (Redução) de Caixa e Equivalentes":
                fluxo_caixa_equivalentes.append(direita.text)
        
        
        
    return pd.DataFrame(zip(data,fluxo_caixa_operacional,fluxo_caixa_investimentos,
                            fluxo_caixa_financiamentos, fluxo_caixa_equivalentes),
                 columns=["data","fluxo_caixa_operacional","fluxo_caixa_investimentos",
                                         "fluxo_caixa_financiamentos", "fluxo_caixa_equivalentes"])


def resumoEmpresaFc3Meses(driver):
    
    data = []
    fluxo_caixa_operacional = []
    fluxo_caixa_investimentos = []
    fluxo_caixa_financiamentos = []
    fluxo_caixa_equivalentes = []
    
    tabelaNome = "tabela_resumo_empresa_fc_3meses"
    
    
    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, tabelaNome))
    )
    
    body = tabela.find_element(By.TAG_NAME, "tbody")
    trs = body.find_elements(By.TAG_NAME,"tr")
    
    
    for tr in trs:
        
        esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
        direita = tr.find_element(By.CLASS_NAME,"direita")
        
        if esquerda.text == "Fluxo de Caixa Operacional":
            fluxo_caixa_operacional.append(direita.text)
            
        elif esquerda.text == "Fluxo de Caixa de Investimentos":
            fluxo_caixa_investimentos.append(direita.text)
            
        elif esquerda.text == "Fluxo de Caixa de Financiamentos":
            fluxo_caixa_financiamentos.append(direita.text)
        
        elif esquerda.text == "Aumento (Redução) de Caixa e Equivalentes":
            fluxo_caixa_equivalentes.append(direita.text)
            
    
    
    select_element = tabela.find_element(By.CLASS_NAME, "data_tabela")
    select_object = Select(select_element)
    
    
    all_options = select_object.options
    current_selected = select_object.first_selected_option
    current_index = all_options.index(current_selected)
    
    data.append(all_options[0].text)
    
    
    while current_index < len(all_options) - 1:
        
        print(current_index)
        
        data.append(all_options[current_index + 1].text)
        
        next_option = all_options[current_index + 1]
        next_option.click()
        
        current_index +=1
        
        time.sleep(1)
        
        tabela = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, tabelaNome))
        )
        
        body = tabela.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME,"tr")
        
        
        for tr in trs:
            
            esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
            direita = tr.find_element(By.CLASS_NAME,"direita")
            
            if esquerda.text == "Fluxo de Caixa Operacional":
                fluxo_caixa_operacional.append(direita.text)
                
            elif esquerda.text == "Fluxo de Caixa de Investimentos":
                fluxo_caixa_investimentos.append(direita.text)
                
            elif esquerda.text == "Fluxo de Caixa de Financiamentos":
                fluxo_caixa_financiamentos.append(direita.text)
            
            elif esquerda.text == "Aumento (Redução) de Caixa e Equivalentes":
                fluxo_caixa_equivalentes.append(direita.text)
        
        
        
    return pd.DataFrame(zip(data,fluxo_caixa_operacional,fluxo_caixa_investimentos,
                            fluxo_caixa_financiamentos, fluxo_caixa_equivalentes),
                 columns=["data","fluxo_caixa_operacional","fluxo_caixa_investimentos",
                                         "fluxo_caixa_financiamentos", "fluxo_caixa_equivalentes"])


def retornosMargens(driver):
    
    data = []
    retorno_sem_capital_tangivel = []
    retorno_sem_capital_investido = []
    retorno_sem_capital_tangivel_pre_imposto = []
    retorno_sem_capital_investido_pre_imposto = []
    retorno_sem_patrimonio_liq_inicial = []
    retorno_sem_ativo_inicial = []
    margem_bruta = []
    margem_liquida = []
    margem_ebit = []
    margem_ebitda = []
    giro_ativo_inicial = []
    alavancagem_financeira = []
    passivo_patrimonio_liquido = []
    divida_liquida_ebitda = []
    
    tabelaNome = "tabela_resumo_empresa_margens_retornos"
    
    
    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, tabelaNome))
    )
    
    body = tabela.find_element(By.TAG_NAME, "tbody")
    trs = body.find_elements(By.TAG_NAME,"tr")
    
    
    for tr in trs:
        
        esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
        direita = tr.find_element(By.CLASS_NAME,"direita")


        if esquerda.text == "Retorno s/ Capital Tangível Inicial":
            retorno_sem_capital_tangivel.append(direita.text)
            
        elif esquerda.text == "Retorno s/ Capital Investido Inicial":
            retorno_sem_capital_investido.append(direita.text)
            
        elif esquerda.text == "Retorno s/ Capital Tangível Inicial Pré-Impostos":
            retorno_sem_capital_tangivel_pre_imposto.append(direita.text)
        
        elif esquerda.text == "Retorno s/ Capital Investido Inicial Pré-Impostos":
            retorno_sem_capital_investido_pre_imposto.append(direita.text)
            
        elif esquerda.text == "Retorno s/ Patrimônio Líquido Inicial":
            retorno_sem_patrimonio_liq_inicial.append(direita.text)
            
        elif esquerda.text == "Retorno s/ Ativo Inicial":
            retorno_sem_ativo_inicial.append(direita.text)
            
        elif esquerda.text == "Margem Bruta":
            margem_bruta.append(direita.text)
            
        elif esquerda.text == "Margem Líquida":
            margem_liquida.append(direita.text)

        elif esquerda.text == "Margem EBIT":
            margem_ebit.append(direita.text)

        elif esquerda.text == "Margem EBITDA":
            margem_ebitda.append(direita.text)

        elif esquerda.text == "Giro do Ativo Inicial":
            giro_ativo_inicial.append(direita.text)

        elif esquerda.text == "Alavancagem Financeira":
            alavancagem_financeira.append(direita.text)

        elif esquerda.text == "Passivo/Patrimônio Líquido":
            passivo_patrimonio_liquido.append(direita.text)

        elif esquerda.text == "Dívida Líquida/EBITDA":
            divida_liquida_ebitda.append(direita.text)


    
    select_element = tabela.find_element(By.CLASS_NAME, "data_tabela")
    select_object = Select(select_element)
    
    
    all_options = select_object.options
    current_selected = select_object.first_selected_option
    current_index = all_options.index(current_selected)
    
    data.append(all_options[0].text)
    
    
    while current_index < len(all_options) - 1:

        print(current_index)
        
        data.append(all_options[current_index + 1].text)
        
        next_option = all_options[current_index + 1]
        next_option.click()
        
        current_index +=1
        
        time.sleep(1)
        
        tabela = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, tabelaNome))
        )
        
        body = tabela.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME,"tr")
        
        
        for tr in trs:
            
            esquerda = tr.find_element(By.CLASS_NAME,"esquerda")
            direita = tr.find_element(By.CLASS_NAME,"direita")

            if esquerda.text == "Retorno s/ Capital Tangível Inicial":
                retorno_sem_capital_tangivel.append(direita.text)

            elif esquerda.text == "Retorno s/ Capital Investido Inicial":
                retorno_sem_capital_investido.append(direita.text)

            elif esquerda.text == "Retorno s/ Capital Tangível Inicial Pré-Impostos":
                retorno_sem_capital_tangivel_pre_imposto.append(direita.text)

            elif esquerda.text == "Retorno s/ Capital Investido Inicial Pré-Impostos":
                retorno_sem_capital_investido_pre_imposto.append(direita.text)

            elif esquerda.text == "Retorno s/ Patrimônio Líquido Inicial":
                retorno_sem_patrimonio_liq_inicial.append(direita.text)

            elif esquerda.text == "Retorno s/ Ativo Inicial":
                retorno_sem_ativo_inicial.append(direita.text)

            elif esquerda.text == "Margem Bruta":
                margem_bruta.append(direita.text)

            elif esquerda.text == "Margem Líquida":
                margem_liquida.append(direita.text)

            elif esquerda.text == "Margem EBIT":
                margem_ebit.append(direita.text)

            elif esquerda.text == "Margem EBITDA":
                margem_ebitda.append(direita.text)

            elif esquerda.text == "Giro do Ativo Inicial":
                giro_ativo_inicial.append(direita.text)

            elif esquerda.text == "Alavancagem Financeira":
                alavancagem_financeira.append(direita.text)

            elif esquerda.text == "Passivo/Patrimônio Líquido":
                passivo_patrimonio_liquido.append(direita.text)

            elif esquerda.text == "Dívida Líquida/EBITDA":
                divida_liquida_ebitda.append(direita.text)

        
    return pd.DataFrame(zip(data,retorno_sem_capital_tangivel,retorno_sem_capital_investido,retorno_sem_capital_tangivel_pre_imposto,
                            retorno_sem_capital_investido_pre_imposto,retorno_sem_patrimonio_liq_inicial,retorno_sem_ativo_inicial,
                            margem_bruta,margem_liquida,margem_ebit,margem_ebitda,giro_ativo_inicial,alavancagem_financeira,
                            passivo_patrimonio_liquido,divida_liquida_ebitda),
                 columns=["data","retorno_sem_capital_tangivel","retorno_sem_capital_investido","retorno_sem_capital_tangivel_pre_imposto",
                            "retorno_sem_capital_investido_pre_imposto","retorno_sem_patrimonio_liq_inicial","retorno_sem_ativo_inicial",
                            "margem_bruta","margem_liquida","margem_ebit","margem_ebitda","giro_ativo_inicial","alavancagem_financeira",
                            "passivo_patrimonio_liquido","divida_liquida_ebitda"])


acoes = pd.read_csv("acoesListadasB3.csv")
driver = webdriver.Chrome()

continua = True
apartir = ""
for ticker in acoes["Ticker"]:
    
    with open("ultimoAtivo.txt", "w") as arquivo:           
        arquivo.write("Ativo: "+ticker)
    
    if continua:
        try:
            
            
            driver.get("https://www.investsite.com.br/principais_indicadores.php?cod_negociacao="+ticker)
            
            
            tabela = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "tabela_resumo_empresa_dre_12meses"))
            )
            
            if not os.path.exists(ticker):
                os.makedirs(ticker)



            print(f"Começando resumoEmpresaPrecosRelativos {ticker}")
            ret1 = resumoEmpresaPrecosRelativos(driver)
            ret1.to_csv(ticker+"\\resumoEmpresaPrecosRelativos.csv")


            print(f"Começando resumoEmpresaDre12Meses {ticker}")
            ret2 = resumoEmpresaDre12Meses(driver)
            ret2.to_csv(ticker+"\\resumoEmpresaDre12Meses.csv")
            
            print(f"Começando resumoEmpresaDre3Meses {ticker}")
            ret3 = resumoEmpresaDre3Meses(driver)
            ret3.to_csv(ticker+"\\resumoEmpresaDre3Meses.csv")
            
            print(f"Começando resumoEmpresaMargensRetornos {ticker}")
            ret4 = resumoEmpresaMargensRetornos(driver)
            ret4.to_csv(ticker+"\\resumoEmpresaMargensRetornos.csv")
            
            print(f"Começando resumoEmpresaBp {ticker}")
            ret5 = resumoEmpresaBp(driver)
            ret5.to_csv(ticker+"\\resumoEmpresaBp.csv")
            
            print(f"Começando resumoEmpresaFc12Meses {ticker}")
            ret6 = resumoEmpresaFc12Meses(driver)
            ret6.to_csv(ticker+"\\resumoEmpresaFc12Meses.csv")
            
            print(f"Começando resumoEmpresaFc3Meses {ticker}")
            ret7 = resumoEmpresaFc3Meses(driver)
            ret7.to_csv(ticker+"\\resumoEmpresaFc3Meses.csv")


            print(f"Começando retornosMargens {ticker}")
            ret8 = retornosMargens(driver)
            ret8.to_csv(ticker + "\\retornosMargens.csv")

            print(f"Começando resumoEmpresa {ticker}")
            ret9 = resumoEmpresa(driver)
            ret9.to_csv(ticker + "\\resumoEmpresa.csv")

            
            
            
            
        except Exception as e:
            
            with open("arquivoErros.txt", "a") as arquivo:           
                arquivo.write("Ativo: "+ticker+"\nErro: "+str(e)+"\n")
        
    
    if ticker == apartir:
        continua = True