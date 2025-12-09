from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

arquivo = open('Resultado', 'w')

navegador = webdriver.Chrome()
navegador.get('https://registro.br')

dominio = 'testesite'
barra_pesquisa = navegador.find_element(By.ID, 'is-avail-field')
barra_pesquisa.clear()
barra_pesquisa.send_keys(dominio)
barra_pesquisa.send_keys(Keys.RETURN)
time.sleep(2)

status = navegador.find_element(By.XPATH, '//*[@id="conteudo"]/div/section/div[2]/div/p/span/strong')

arquivo.write(f'Domínio = ({dominio}) // Status = {status.text}')
arquivo.close()

time.sleep(2)
navegador.quit()