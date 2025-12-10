from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import xlrd
import time

book = xlrd.open_workbook('/home/nprione/Documentos/Meus_Projetos/Meu/Projeto 1 - Modelo do curso OficinaPython/dominios.xls')
planilha = book.sheet_by_name('Plan1')
linhas = planilha.nrows

arquivo = open('Resultado.txt', 'w')

navegador = webdriver.Chrome()
navegador.get('https://registro.br')
time.sleep(2)

for item in range(0, linhas):
    x = planilha.cell_value(item, 0)
    barra_pesquisa = navegador.find_element(By.ID, 'is-avail-field')
    time.sleep(2)
    barra_pesquisa.clear()
    barra_pesquisa.send_keys(x)
    barra_pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    status = navegador.find_element(By.XPATH, '//*[@id="conteudo"]/div/section/div[2]/div/p/span/strong')
    arquivo.write(f'Domínio = ({x}) // Status = {status.text}. \n')
    time.sleep(1)
    
arquivo.close()
navegador.quit()