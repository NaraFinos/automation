from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime

#automatizar el clic en un elemento web
def click_element_by_xpath(xpath):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.click()

#automatizar la entrada de texto en un campo de formulario web 
def send_keys(xpath,texto):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.click()
    element.send_keys(texto)

#automatizar la interacción con la parte del rango dentro de la parte "input" de la pagina
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

#FECHA mm/yyyy
def ingresar_fecha(driver, fecha): 
    calendario = driver.find_element(By.XPATH, '//input[@id="month"]')
    calendario.click()
    calendario.send_keys(fecha.strftime('%B')) # ingresa el nombre del mes
    calendario.send_keys(Keys.TAB)
    calendario.send_keys(fecha.strftime('%Y')) # ingresa el año en formato YYYY

# FECHA mm/dd/yyyy
def ingresarfecha(driver, fecha):
    calendario = driver.find_element(By.ID, 'date')
    calendario.click()
    calendario.clear()
    
    # Separar la fecha en mes, día y año
    mes, dia, anio = fecha.split('/')
    
    # Hacer clic en el mes y en el año en el calendario
    mes_selector = driver.find_element(By.XPATH, f"//div[@class='calendar']/div[contains(@class, 'months')]/span[contains(text(), '{mes}')]")
    mes_selector.click()
    time.sleep(1) # Esperar un segundo para que se actualice el calendario
    anio_selector = driver.find_element(By.XPATH, f"//div[@class='calendar']/div[contains(@class, 'years')]/span[contains(text(), '{anio}')]")
    anio_selector.click()
    time.sleep(1) # Esperar un segundo para que se actualice el calendario
    
    # Enviar las teclas con la fecha
    calendario.send_keys(fecha)

def send_keys_tab(xpath, text):
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    calendario = driver.find_element('xpath','//input[@id="month"]')
    calendario.click()
    calendario.send_keys(texto)
    calendario.send_keys(Keys.TAB)
    calendario.send_keys(texto)
    time.sleep (5)

#VER ESTE DEF PORQUE NO ANDA
def ingresar_fecha(driver, fecha):
    calendario = driver.find_element(By.ID, 'month')
    calendario.click()
    nombre_mes = fecha.strftime('%B')
    num_mes = datetime.datetime.strptime(nombre_mes, '%B').strftime('%Y-%m')
    anio = str(fecha.year)

    # Enviar el nombre del mes
    for letra in nombre_mes:
        calendario.send_keys(letra)

    # Ir al siguiente campo de entrada
    calendario.send_keys(Keys.TAB)

    # Enviar el año
    for letra in anio:
        calendario.send_keys(letra)

#PRIMERA PARTE DE INPUT
def ingresar_datos(driver, usuario, contrasena, comentario):
    input_usuario = driver.find_element(By.ID, 'InputUserName')
    input_usuario.send_keys(usuario)
    time.sleep(0.5)

    input_contrasena = driver.find_element(By.ID, 'password')
    input_contrasena.send_keys(contrasena)
    time.sleep(0.5)

    textarea_comentario = driver.find_element(By.ID, 'exampleFormControlTextarea1')
    textarea_comentario.send_keys(comentario)
    time.sleep(0.5)

#INGRESAMOS A LA PAGINA
driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.get('https://hakalab.com/hakatools')
time.sleep (0.5)
click_element_by_xpath('//div[@id="cardGoElemets"]')
time.sleep (0.5)
#INSERTAMOS EL NOMBRE, CONTRASEÑA Y TEXTO ok
usuario = 'nara finos'
contrasena = 'lamotomami2023'
comentario = 'si llegaste hasta aquí ya estoy saltando de alegría'
ingresar_datos(driver, usuario, contrasena, comentario)
time.sleep (0.5)
#RANGO ok
uso_de_rango('//input[@id="customRange1"]', 50)
# INGRESAMOS FECHA CON DD/MM/YYY
fecha = '01/10/2009'
ingresarfecha(driver, fecha)

##hay un problema 
#fecha = datetime.date(1992, 1, 1)
#ingresar_fecha(driver, fecha)
#time.sleep (5)

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










