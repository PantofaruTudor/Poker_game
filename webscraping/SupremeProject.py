from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options --> De invatat
import time
import sys
import os


def restart_program():
    time.sleep(3)
    print("Restarting the program")
    os.execv(sys.executable,['python'] + sys.argv)


def checkOut():
    try:
        WebDriverWait(driver,5).until(
            EC.presence_of_all_elements_located((By.ID,"accept-tos"))
        )
        print("found")
    except:
        restart_program()

    tos = driver.find_element(By.ID,"accept-tos")

    if  tos.is_displayed() == True:
        print("Am ajuns la tos")
        #supreme()   incerc sa fac programul un subprogram
    tos.click()

    email = driver.find_element(By.NAME,"email")
    email.click()
    email.send_keys("tudorpantofaru@gmail.com")

    country_code = driver.find_element(By.NAME,"countryCode").click()
    country = driver.find_element(By.XPATH,"//select/option[contains(text(),'Romania')]").click()

    random_button = driver.find_element(By.ID,"shipping-methods")
    random_button.click()

    time.sleep(1)

    county = driver.find_element(By.XPATH,"//select/option[contains(text(),'Neam')]").click()

    time.sleep(2)

    driver.execute_script("document.getElementsByName('firstName')[0].value='Pantofaru';")
    driver.execute_script("document.getElementsByName('lastName')[0].value='Tudor';")
    driver.execute_script("document.getElementsByName('address1')[0].value='Strada 1 Decembrie 1918, nr 61';")
    driver.execute_script("document.getElementsByName('postalCode')[0].value='610219';")
    driver.execute_script("document.getElementsByName('city')[0].value='Piatra Neamt';")
    driver.execute_script("document.getElementsByName('phone')[0].value='0771052736';")

    # --Section 4: Submitting card data and finishing the payment
    time.sleep(2)

    driver.execute_script("document.getElementsByName('number')[0].value = '4689180012300190';")
    driver.execute_script("document.getElementsByName('verification_value')[0].value = '772';")
    driver.execute_script("document.getElementsByName('expiry')[0].value = '09/26';")
    driver.execute_script("document.getElementsByName('name')[0].value = 'Pantofaru Tudor Mihai';")





def b_checkout(url):
    driver.get(url)
    
    # --Section 2:  Finding the first tee on the page, selecting the colour and size
    btn_tee = driver.find_element(By.XPATH,"//*[contains(text(),'Tee')]")
    print("Element is visible?"+str(btn_tee.is_displayed()))
    time.sleep(1)
    #btn_tee = driver.find_element(By.CLASS_NAME,"aria-label=Lollipop Tee product link")
    btn_tee.click()

    time.sleep(0.5) #Are nevoie de timp pentru a se incarca culoarea

    colour = driver.find_element(By.XPATH,"//button[contains(@title,'White')]")
    print("Element is visible?"+str(colour.is_displayed()))
    colour.click()

    time.sleep(0.3)

    size = driver.find_element(By.XPATH,"//select/option[contains(text(),'Large')]")
    print("Element is visible?"+str(size.is_displayed()))
    size.click()

    
    # --Section 3: Finding the checkout and submiting the form
    add_bag = driver.find_element(By.XPATH,"//button[contains(text(),'add to cart')]").click()
    WebDriverWait(driver,5).until(
        EC.presence_of_all_elements_located((By.XPATH,"//span[contains(text(),'checkout')]"))
    )

    checkout = driver.find_element(By.XPATH,"//span[contains(text(),'checkout')]").click()
    checkOut()



# --Section 1: This connects the Chrome browser with selenium using chromeDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)
url = "https://eu.supreme.com/collections/t-shirts"
#driver.get("https://eu.supreme.com/collections/t-shirts")

b_checkout(url)

start_time = time.time()
end_time = time.time()
print(end_time - start_time)
time.sleep()