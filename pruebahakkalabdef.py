from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def escribir_en_input_si_esta_habilitado(input_id, texto):
    # Cargar el controlador del navegador (en este caso, Chrome)
    driver = webdriver.Chrome('./driver/chromedriver.exe')

    # Navegar a la página web que deseas probar
    driver.get("https://ejemplo.com")

    # Buscar el elemento input y verificar si está habilitado
    input_element = driver.find_element_by_id(input_id)
    if input_element.is_enabled():
        # Si está habilitado, escribir en el input
        input_element.send_keys(texto)
    else:
        # Si no está habilitado, mostrar un mensaje
        print("El input está inhabilitado")

    # Cerrar el navegador
    driver.quit()




#########################################

escribir_en_input_si_esta_habilitado("InputUserName", "Nara") #ok
escribir_en_input_si_esta_habilitado("last_name", "Velazquez")