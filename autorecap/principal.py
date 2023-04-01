##objetivo levantar un browser, navegar y tirar el browser
#traemos selenium
from selenium import webdriver
# traemos time 
import time
#instanciamos variable con lo que queremos usar  y llamamos al archivo
driver = webdriver.Chrome('chromedriver.exe')
#navegar a algun sitio
driver.get('http://mercadolibre.com.ar')
title = driver.title
assert title == "Mercado Libre Argentina - Envíos Gratis en el día"
#logramos que se loguee
link = driver.find_element('xpath',"//*[@id='nav-header-menu']/a[2]")
link.click()
driver.implicitly_wait (3)
# link = driver.find_element('xpath',"//input[@name='user_id']")
# link.send_keys('naara.finos@gmail.com')
# link = driver.find_element('xpath',"//button[@type='submit']")
# link.click()
# driver.implicitly_wait (0.9)
# 
