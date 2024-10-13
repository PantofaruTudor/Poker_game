from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options --> De invatat
import time


# --Section 1: This connects the Chrome browser with selenium using chromeDriver

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://eu.supreme.com/collections/t-shirts")


'''
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.XPATH,"//*[contains(text(),'Tee')]"))
)
'''

# --Section 2:  Finding the first tee on the page, selecting the colour and size
btn_tee = driver.find_element(By.XPATH,"//*[contains(text(),'Tee')]")
print("Element is visible?"+str(btn_tee.is_displayed()))
#btn_tee = driver.find_element(By.CLASS_NAME,"aria-label=Lollipop Tee product link")
btn_tee.click()

time.sleep(1) #Are nevoie de timp pentru a se incarca culoarea

colour = driver.find_element(By.XPATH,"//button[contains(@title,'White')]")
print("Element is visible?"+str(colour.is_displayed()))
colour.click()

time.sleep(1)

size = driver.find_element(By.XPATH,"//select/option[contains(text(),'XLarge')]")
print("Element is visible?"+str(size.is_displayed()))
size.click()

start_time = time.time()
# --Section 3: Finding the checkout and submiting the form
add_bag = driver.find_element(By.XPATH,"//button[contains(text(),'add to cart')]").click()

WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.XPATH,"//span[contains(text(),'checkout')]"))
)

checkout = driver.find_element(By.XPATH,"//span[contains(text(),'checkout')]").click()

WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.ID,"accept-tos"))
)

button = driver.find_element(By.ID,"accept-tos")
button.click()

email = driver.find_element(By.NAME,"email")
email.click()
email.send_keys("tudorpantofaru@gmail.com")


country_code = driver.find_element(By.NAME,"countryCode").click()
country = driver.find_element(By.XPATH,"//select/option[contains(text(),'Romania')]").click()

#full_form = driver.find_element()

end_time = time.time()
print(end_time - start_time)
time.sleep()