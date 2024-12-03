from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get("https://the-internet.herokuapp.com/login")

# Localiza os campos de username e password
campo_usuario = navegador.find_element(By.ID, "username")
campo_senha = navegador.find_element(By.ID, "password")

# Preenche as credenciais
campo_usuario.send_keys("tomsmith")
campo_senha.send_keys("SuperSecretPassword!")

# Clica no botão de login
navegador.find_element(By.XPATH, '//*[@id="login"]/button').click()

mensagem_sucesso = navegador.find_element(By.XPATH, "//div[@class='flash success']")
if "You logged into a secure area!" in mensagem_sucesso.text:
    print("Login bem-sucedido!")
else:
    print("Falha no login ou mensagem incorreta.")   
time.sleep(2)
navegador.quit()