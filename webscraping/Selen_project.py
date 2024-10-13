from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

time.sleep(3) #sa trec de cookies

#WebDriverWait(driver,5).until(
#EC.presence_of_element_located((By.CLASS_NAME, "gLFyF")))  #-> ASA ASTEPTI SA APARA UN ELEMENT PE PAGINA


input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
#input_element.clear() -> DACA VREI SA STERGI CEVA DE PE PAGINA DEJA SCRIS INTR O CASUTA
input_element.send_keys("tech with tim" + Keys.ENTER)

WebDriverWait(driver,5).until(
   EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))) 

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim") #DACA PE PAGINA APARE CEVA CU NUMELE ACELA, IL VA SELECTA
link.click()

time.sleep(10)

driver.quit()
 