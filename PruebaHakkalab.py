from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#automatizar el clic en un elemento web
def click_element_by_xpath(xpath):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.click()

#automatizar la entrada de texto en un campo de formulario web 
def send_keys(xpath,texto):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.click()
    element.send_keys(texto)

#automatizar la interacción con un elemento de la página web 
def uso_de_rango(xpath, range):
    #elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))): busca el elemento web que corresponde al XPath proporcionado y espera hasta que esté presente 
        #driver: es el controlador de Selenium que se utiliza para interactuar con el navegador web
        #10: es el tiempo máximo que se espera para que aparezca el elemento
        # "presence_of_element_located": es una función de espera explícita de Selenium que verifica que el elemento esté presente en el DOM
    #acciones = ActionChains(driver):esta línea crea una nueva instancia de la clase ActionChains de Selenium que se utiliza para realizar acciones complejas con el mouse y el teclado.
    #acciones.click_and_hold(elemento): hace clic en el elemento y lo mantiene presionado.
    #acciones.move_by_offset(range, 0):mueve el mouse una cantidad especificada de píxeles a la derecha (en el eje X) 
    #acciones.release(): suelta el elemento.
    #acciones.perform():  ejecuta todas las acciones en secuencia.
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    acciones = ActionChains(driver)
    acciones.click_and_hold(elemento).move_by_offset(range, 0).release().perform()
    time.sleep (5)


def send_keys_tab(xpath, text):
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    calendario = driver.find_element('xpath','//input[@id="month"]')
    calendario.click()
    calendario.send_keys(texto)
    calendario.send_keys(Keys.TAB)
    calendario.send_keys(texto)
    time.sleep (5)

def seleccionar_fecha_y_anio(date,value):
    fecha_input = driver.find_element_by_id('date')
    fecha_actual = fecha_input.get_attribute('value')
    dia, mes, anio = fecha_actual.split('-')
    print("Fecha actual:", fecha_actual)
    print("Día:", dia)
    print("Mes:", mes)
    print("Año:", anio)

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.get('https://hakalab.com/hakatools')
time.sleep (0.5)
click_element_by_xpath('//div[@id="cardGoElemets"]')
time.sleep (0.5)
send_keys('//input[@id="InputUserName"]', "nara finos")
time.sleep (0.5)
time.sleep (0.5)
send_keys('//input[@id="password"]', "lamotomami2023")
time.sleep (0.5)
send_keys('//textarea[@id="exampleFormControlTextarea1"]', "si llegaste hasta aquí ya estoy saltando de alegría")
time.sleep (0.5)
uso_de_rango('//input[@id="customRange1"]', 50)
calendario = driver.find_element(By.XPATH,'//input[@id="date"]')
calendario.click()
calendario.send_keys("10/01/2009")
time.sleep (0.5)
calendario = driver.find_element(By.XPATH,'//input[@id="month"]')
calendario.click()
calendario.send_keys("july")
calendario.send_keys(Keys.TAB)
calendario.send_keys("2023")

##hay un problema 
calendario = driver.find_element(By.XPATH,'//input[@id="month"]')
calendario.click()
calendario.send_keys("july")
calendario.send_keys(Keys.TAB)
calendario.send_keys("2023")
time.sleep (2)

#cal_semana = driver.find_element(By.XPATH,'//input[@id="datetime-local"]')
#cal_semana.click()
#cal_semana.send_keys("12")
#cal_semana.send_keys("12")
#cal_semana.send_keys("2023")
#cal_semana.send_keys(Keys.TAB)
#cal_semana.send_keys("12")
#cal_semana.send_keys("12")
#cal_semana.send_keys("a")
#time.sleep (5)
#color_palette = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "color")))
#ActionChains(driver).move_to_element(color_palette).move_by_offset(2, 0).click().perform()
time.sleep (0.5)
# ACA ABRE UNA NUEVA PESTAÑA
#driver.execute_script("window.open('');")
#driver.switch_to.window(driver.window_handles[1])
#driver.get('https://hakalab.com/hakatools')
#utilizacion de selector
#selector = driver.find_element('id',"list-selects-list")
##selector.click()
#time.sleep (1)
#opcion = driver.find_element(By.XPATH,'//select[@id="selectorLenguaje"]')
#opcion.click()
#opcion = driver.find_element(By.XPATH,'//option[text()="Phyton"]')
#opcion.click()
time.sleep (0.5)
#opcion = driver.find_element(By.XPATH,'//option[text()="Manzana"]')
#opcion.click()
#time.sleep (2)
##SELECTORES DE FECHA
#selector = driver.find_element('id',"list-pickers-list")
#selector.click()
##time.sleep (1)
#selector_dia = driver.find_element(By.XPATH,'(//option[@aria-label="Ene"])[1]')
#selector_dia.click()
#selector_mes = driver.find_element(By.XPATH,'(//div[@aria-label="5-1-2023"])[1]')
#selector_mes.click()
#time.sleep (2)
#selector_dia = driver.find_element(By.XPATH,'(//option[@aria-label="Ene"])[2]')
#selector_dia.click()
#selector_mes = driver.find_element (By.XPATH ,'(//div[@aria-label="5-1-2023"])[2]')
#selector_dia.click()
#time.sleep (2)
##CHECKBOX
checkbox = driver.find_element(By.XPATH, '//a[@id="list-checkbox-list"]')
checkbox.click()
time.sleep (0.5)
seleccionbox = driver.find_element(By.XPATH,'//input[@id="simpleCheckbox"]')
seleccionbox.click()
seleccionbox = driver.find_element(By.XPATH, '//input[@id="defaultCheckbox"]')
seleccionbox.click()
time.sleep (0.5)
## SELECTOR DE GRUPO DE BOTONES
selectbuttongroup = driver.find_element(By.XPATH, '//a[@id="list-groupButtons-list"]')
selectbuttongroup.click()
time.sleep (0.5)
buttom = driver.find_element('id',"SegundaOpcionGroupButton")
buttom.click()
time.sleep (0.5)
##SELECTOR DE CLICK DE BOTONES
selectbutton = driver.find_element(By.XPATH, '//a[@id="list-buttons-list"]')
selectbutton.click()
#LOGRA HACER CLICK PERO USANDO OTRO METODO. ¿por que?
buttonone = driver.find_element('xpath','//button[@id="singleClickButton"]')
driver.execute_script("arguments[0].click();", buttonone)
# LOGRA HACER DOBLE CLICK PERO ¿POR QUE?
button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "DoubleClickButton")))
actions = ActionChains(driver)
actions.double_click(button).perform()
time.sleep (0.5)
#Este código utiliza WebDriverWait para esperar hasta que el botón con el ID "ClickDerechoButton" esté presente y visible en la página web. Una vez que el botón está disponible, se utiliza la clase ActionChains para hacer doble clic en el botón con context_click(boton) y perform()
wait = WebDriverWait(driver, 10)
boton = wait.until(EC.visibility_of_element_located((By.ID, "ClickDerechoButton")))
accion = ActionChains(driver)
accion.context_click(boton).perform()
time.sleep (0.5)
#CARGA DE ARCHIVO
archivo = driver.find_element(By.XPATH, '//a[@id="list-upload-list"]')
archivo.click()
ruta_archivo = "C:\\Users\\naraf\\Downloads\\luna.jpeg"
input_archivo = driver.find_element(By.ID, "uploadFileInput")
input_archivo.send_keys(ruta_archivo)
driver.implicitly_wait(10)
boton_descarga = driver.find_element(By.ID, "downloadButton")
boton_descarga.click()
time.sleep (2)










