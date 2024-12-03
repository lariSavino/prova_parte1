from selenium import webdriver 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.alert import Alert

# Inicializa o navegador
navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


    # Acessa o site com alertas
navegador.get("https://www.selenium.dev/selenium/web/alerts.html#")
time.sleep(2)
navegador.find_element(By.ID, "alert").click()
time.sleep(2)
alerta = navegador.switch_to.alert
alerta.accept()

   
