#importação das bibliotecas do Selenium e Tempo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Instanciar objeto que representará o Chrome
chrome = webdriver.Chrome()



#Chama a URL do Google
chrome.get('https://www.google.com.br')

#Conta 5 segundos
#time.sleep(10)

#Captura a caixa de busca do Google e digita python
searchBox = chrome.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
searchBox.send_keys('Python')
#Simula botão Enter teclado
searchBox.send_keys(Keys.RETURN)

# Captura o link do primeiro resultado de busca
link = chrome.find_element(By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div > div > div > div > div > div > div.yuRUbf > a > h3')
link.click()
time.sleep(10)
# Fecha o navegador
chrome.close()



