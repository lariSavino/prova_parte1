from selenium import webdriver 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.firefox import GeckoDriverManager


navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get("https://www.selenium.dev/")
navegador.find_element(By.XPATH, '/html/body/header/nav/div/ul/li[2]/a/span').click()
time.sleep(2)

header = navegador.find_element(By.TAG_NAME, "h2")  # Busca pelo cabeçalho principal (h1)
print("Texto do h2:", header.text)
navegador.quit()