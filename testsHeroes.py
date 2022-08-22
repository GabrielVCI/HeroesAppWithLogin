# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLoginTest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginTest(self):
    # Test name: Login Test
    # Step # | name | target | value
    # 1 | open | /login | 
    self.driver.get("http://localhost:9000/login")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


##Registro de usuarios
class TestRegistroTest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_registroTest(self):
    # Test name: Registro Test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:9000/")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | linkText=Signup | 
    self.driver.find_element(By.LINK_TEXT, "Signup").click()
    # 4 | click | id=name-input | 
    self.driver.find_element(By.ID, "name-input").click()
    # 5 | type | id=name-input | Alejandro
    self.driver.find_element(By.ID, "name-input").send_keys("Alejandro")
    # 6 | click | id=email-input | 
    self.driver.find_element(By.ID, "email-input").click()
    # 7 | type | id=email-input | gabrielva72@gmail.com
    self.driver.find_element(By.ID, "email-input").send_keys("ejemplo72@gmail.com")
    # 8 | click | id=password-input | 
    self.driver.find_element(By.ID, "password-input").click()
    # 9 | type | id=password-input | 1234
    self.driver.find_element(By.ID, "password-input").send_keys("1234")
    # 10 | click | id=confirm-password-input | 
    self.driver.find_element(By.ID, "confirm-password-input").click()
    # 11 | type | id=confirm-password-input | 1234
    self.driver.find_element(By.ID, "confirm-password-input").send_keys("1234")
    # 12 | click | css=.btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # 13 | type | id=floatingInput | gabrielva72@gmail.com
    self.driver.find_element(By.ID, "floatingInput").send_keys("ejemplo@gmail.com")
    # 14 | type | id=floatingPassword | 1234
    self.driver.find_element(By.ID, "floatingPassword").send_keys("1234")

###Logout
class TestLogoutTest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_logoutTest(self):
    # Test name: Logout Test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:9000/")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | css=.btn-danger:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-danger:nth-child(2)").click()

###Crear heroe
class TestCrearheroetest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_crearhroetest(self):
    # Test name: Crear héroe test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:9000/")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # 4 | click | id=name | 
    self.driver.find_element(By.ID, "name").click()
    # 5 | type | id=name | Hombre Araña
    self.driver.find_element(By.ID, "name").send_keys("Hombre Araña")
    # 6 | click | id=description | 
    self.driver.find_element(By.ID, "description").click()
    # 7 | type | id=description | Es un hombre con los poderes de una araña.
    self.driver.find_element(By.ID, "description").send_keys("Es un hombre con los poderes de una araña.")
    # 8 | click | css=.mb-3:nth-child(4) | 
    self.driver.find_element(By.CSS_SELECTOR, ".mb-3:nth-child(4)").click()
    # 9 | click | id=races | 
    self.driver.find_element(By.ID, "races").click()
    # 10 | select | id=races | label=Humano
    dropdown = self.driver.find_element(By.ID, "races")
    dropdown.find_element(By.XPATH, "//option[. = 'Humano']").click()
    # 11 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
  
###Crear raza
class TestCreateracestest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createracestest(self):
    # Test name: Create races test
    # Step # | name | target | value
    # 1 | open | /races | 
    self.driver.get("http://localhost:9000/races")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | linkText=Crear nueva raza | 
    self.driver.find_element(By.LINK_TEXT, "Crear nueva raza").click()
    # 4 | click | id=name | 
    self.driver.find_element(By.ID, "name").click()
    # 5 | type | id=name | Asgardiano
    self.driver.find_element(By.ID, "name").send_keys("Asgardiano")
    # 6 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
  
###Edit heroes
class TestEditHeroetest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_editHeroetest(self):
    # Test name: EditHeroe test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:9000/")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | css=.card:nth-child(5) > .card-body > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(5) > .card-body > .btn").click()
    # 4 | click | id=description | 
    self.driver.find_element(By.ID, "description").click()
    # 5 | click | css=.row | 
    self.driver.find_element(By.CSS_SELECTOR, ".row").click()
    # 6 | type | id=name | Flash
    self.driver.find_element(By.ID, "name").send_keys("Flash")
    # 7 | click | id=description | 
    self.driver.find_element(By.ID, "description").click()
    # 8 | click | css=.row | 
    self.driver.find_element(By.CSS_SELECTOR, ".row").click()
    # 9 | click | id=description | 
    self.driver.find_element(By.ID, "description").click()
    # 10 | type | id=description | El hombre más rápido que existe.
    self.driver.find_element(By.ID, "description").send_keys("El hombre más rápido que existe.")
    # 11 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

###Edit races
class TestEditracestest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_editracestest(self):
    # Test name: Edit races test
    # Step # | name | target | value
    # 1 | open | /races | 
    self.driver.get("http://localhost:9000/races")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | css=.card:nth-child(2) > .card-body > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) > .card-body > .btn").click()
    # 4 | click | id=name | 
    self.driver.find_element(By.ID, "name").click()
    # 5 | click | css=.row | 
    self.driver.find_element(By.CSS_SELECTOR, ".row").click()
    # 6 | type | id=name | Felino
    self.driver.find_element(By.ID, "name").send_keys("Felino")
    # 7 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
  
###Delete heroes
class TestDeleteheroetest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_deleteheroetest(self):
    # Test name: Delete heroe test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:9000/")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 4 | click | css=.card:nth-child(3) .form-inline > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) .form-inline > .btn").click()
    # 5 | webdriverChooseOkOnVisibleConfirmation |  | 
    self.driver.switch_to.alert.accept()

###Delete races
class TestDeleteracestest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_deleteracestest(self):
    # Test name: Delete races test
    # Step # | name | target | value
    # 1 | open | /races | 
    self.driver.get("http://localhost:9000/races")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | css=.card:nth-child(2) .form-inline > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) .form-inline > .btn").click()

###Cancel create hero
class TestCancelcreateheroetest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cancelcreateheroetest(self):
    # Test name: cancel_create_heroe test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:9000/")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # 4 | click | linkText=volver atras | 
    self.driver.find_element(By.LINK_TEXT, "volver atras").click()
  

###Cancel create race
class TestCancelcreateracetest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cancelcreateracetest(self):
    # Test name: cancel_create_race test
    # Step # | name | target | value
    # 1 | open | /races | 
    self.driver.get("http://localhost:9000/races")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | linkText=Crear nueva raza | 
    self.driver.find_element(By.LINK_TEXT, "Crear nueva raza").click()
    # 4 | click | linkText=volver atras | 
    self.driver.find_element(By.LINK_TEXT, "volver atras").click()
  
###Cancel edit hero
class TestCanceleditheroetest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_canceleditheroetest(self):
    # Test name: cancel_edit_heroe test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:9000/")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | linkText=Editar | 
    self.driver.find_element(By.LINK_TEXT, "Editar").click()
    # 4 | click | linkText=volver atras | 
    self.driver.find_element(By.LINK_TEXT, "volver atras").click()

###Cancel edit race
class TestCanceleditracetest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_canceleditracetest(self):
    # Test name: cancel_edit_race test
    # Step # | name | target | value
    # 1 | open | /races | 
    self.driver.get("http://localhost:9000/races")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | linkText=Editar | 
    self.driver.find_element(By.LINK_TEXT, "Editar").click()
    # 4 | click | linkText=volver atras | 
    self.driver.find_element(By.LINK_TEXT, "volver atras").click()
  
###Return home from login
class TestReturnhomefromlogintest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_returnhomefromlogintest(self):
    # Test name: Return_home_from_login test
    # Step # | name | target | value
    # 1 | open | /login | 
    self.driver.get("http://localhost:9000/login")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | linkText=Atras | 
    self.driver.find_element(By.LINK_TEXT, "Atras").click()
  
###Go from home to register
class TestReturnregisterfromhometest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_returnregisterfromhometest(self):
    # Test name: Return_register_from_home test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:9000/")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | linkText=Signup | 
    self.driver.find_element(By.LINK_TEXT, "Signup").click()

###Go home from races
class TestReturnhomefromracestest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_returnhomefromracestest(self):
    # Test name: Return_home_from_races test
    # Step # | name | target | value
    # 1 | open | /races | 
    self.driver.get("http://localhost:9000/races")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | linkText=Home | 
    self.driver.find_element(By.LINK_TEXT, "Home").click()
  
###Delete all races
class TestDeleteallracestest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_deleteallracestest(self):
    # Test name: Delete_all_races test
    # Step # | name | target | value
    # 1 | open | /races | 
    self.driver.get("http://localhost:9000/races")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | css=.card:nth-child(2) .form-inline > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(2) .form-inline > .btn").click()
    # 4 | click | css=.btn:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
  

###Go from home to login
class TestGofromhometologintest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_gofromhometologintest(self):
    # Test name: Go_from_home_to_login test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:9000/")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | linkText=Login | 
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    # 4 | type | id=floatingInput | gabrielva72@gmail.com
    self.driver.find_element(By.ID, "floatingInput").send_keys("ejemplo@gmail.com")
    # 5 | type | id=floatingPassword | 1234
    self.driver.find_element(By.ID, "floatingPassword").send_keys("1234")

###Go from home to races
class TestGofromhometoracestest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_gofromhometoracestest(self):
    # Test name: Go_from_home_to_races test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:9000/")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | linkText=Races | 
    self.driver.find_element(By.LINK_TEXT, "Races").click()
  

