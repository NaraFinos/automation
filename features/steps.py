from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest



@given('que el usuario ha ingresado a la página de Hakatools')
def step_impl(context):
    context.driver = webdriver.Chrome('./driver/chromedriver.exe')
    context.driver.get('https://hakalab.com/hakatools')
    time.sleep(0.5)
    context.driver.find_element_by_xpath('//div[@id="cardGoElemets"]')

@when('el usuario completa los campos del formulario')
def step_impl(context):
    
    context.driver.find_element(By.ID, "InputUserName").send_keys("nara finos")
    context.driver.find_element(By.ID, "password").send_keys("lamotomami2023")
    context.driver.find_element(By.ID, "exampleFormControlTextarea1").send_keys("si llegaste hasta aquí ya estoy saltando de alegría")
    
@when('selecciona una fecha en el calendario')
def step_impl(context):
    calendario = context.driver.find_element(By.ID, "date")
    calendario.click()
    calendario.send_keys("10/01/2009")
    time.sleep(0.5)
    calendario = context.driver.find_element(By.ID, "month")
    calendario.click()
    calendario.send_keys("july")
    calendario.send_keys(Keys.TAB)
    calendario.send_keys("2023")

@then('el mensaje se envía correctamente')
def step_impl(context):
    uso_de_rango = context.driver.find_element(By.ID, "customRange1")
    uso_de_rango.send_keys(Keys.ARROW_RIGHT * 50)
    retorna_Input = return context.driver.find_element(By.ID, "InputUserName").text
    context.assertTrue("nara finos" in retorna_Input)
    context.driver.quit()