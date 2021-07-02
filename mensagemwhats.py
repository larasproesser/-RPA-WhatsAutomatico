import pandas as pd

contatos_df = pd.read_excel("EnviarWhats.xlsx")
display(contatos_df)

# Essa planilha precisa estar na mesma pasta que o código!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import pyautogui

pyautogui.alert('Automação irá inicar!')

navegador = webdriver.Chrome()
navegador.get("http://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) <1:
    time.sleep(1)

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
   # link = "http://web.whatsapp.com/send?phone={numero}&text={texto}"
    texto = urllib.parse.quote(f"Oi, {pessoa}! {mensagem}")
    link = f"http://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) <1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)    
    time.sleep(10)
       
pyautogui.alert('Pronto, computador voltou a ser seu!')