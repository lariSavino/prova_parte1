from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome() 

    # Abre o navegador e acessa o site do Google
driver.get("https://www.google.com")

    # Procura pela barra de pesquisa
search_bar = driver.find_element(By.NAME, "q")

    # Digita "Python Selenium" na barra de pesquisa e pressionar Enter
search_bar.send_keys("Python Selenium")
search_bar.send_keys(Keys.ENTER)
time.sleep(2)

    # captura de tela
driver.save_screenshot("resultado.png")
print("Captura de tela salva como 'resultado.png'")
    
driver.quit()