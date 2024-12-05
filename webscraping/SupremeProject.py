from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options #--> De invatat
import time
import sys
import os


def restart_program():
    time.sleep(3)
    print("Restarting the program")
    os.execv(sys.executable,['python'] + sys.argv)


def checkOut():
    try:
        WebDriverWait(driver,120).until(
            EC.presence_of_all_elements_located((By.ID,"accept-tos"))
        )
        print("found")
    except:
        driver.execute_script("window.history.go(-2)")
        checkout = driver.find_element(By.XPATH,"//span[contains(text(),'checkout')]").click()
        checkOut()

    tos = driver.find_element(By.ID,"accept-tos")

    if  tos.is_displayed() == True:
        print("Am ajuns la tos")
    tos.click()

    email = driver.find_element(By.NAME,"email")
    email.click()
    email.send_keys("tudorpantofaru@gmail.com")

    country_code = driver.find_element(By.NAME,"countryCode").click()
    country = driver.find_element(By.XPATH,"//select/option[contains(text(),'Romania')]").click()

    time.sleep(1)

    #-- This is another faster method to complete the form, but it is not good enough to replicate human behaviour
    '''
    driver.execute_script("document.getElementsByName('firstName')[0].value='Pantofaru';")
    driver.execute_script("document.getElementsByName('lastName')[0].value='Tudor';")
    driver.execute_script("document.getElementsByName('address1')[0].value='Strada 1 Decembrie 1918, nr 61';")
    driver.execute_script("document.getElementsByName('postalCode')[0].value='610219';")
    driver.execute_script("document.getElementsByName('city')[0].value='Piatra Neamt';")
    driver.execute_script("document.getElementsByName('phone')[0].value='0771052736';")
    time.sleep(2)
    '''
    #-- Section 3: Filling the form with the user's data
    first_name = driver.find_element(By.NAME,"firstName")
    first_name.click()
    first_name.send_keys("Pantofaru")

    last_name = driver.find_element(By.NAME,"lastName")
    last_name.click()
    last_name.send_keys("Tudor")

    address = driver.find_element(By.NAME,"address1")
    address.click()
    address.send_keys("Strada 1 Decembrie 1918, nr 61")

    postal_code = driver.find_element(By.NAME,"postalCode")
    postal_code.click()
    postal_code.send_keys("610219")

    city = driver.find_element(By.NAME,"city")
    city.click()
    city.send_keys("Piatra Neamt")

    phone = driver.find_element(By.NAME,"phone")
    phone.click()
    phone.send_keys("0771052736")


    county = driver.find_element(By.XPATH,"//select/option[contains(text(),'Neam')]").click()
    
    
    # --Section 4: Submitting card data and finishing the payment
    
    iframe_sec = driver.find_element(By.XPATH,"//iframe[contains(@title,'Field container for: Security code')]")
    driver.switch_to.frame(iframe_sec)
    sec_cod = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Security code']")
    print(sec_cod.is_displayed())
    sec_cod.send_keys("772")
    driver.switch_to.default_content()

    iframe_card = driver.find_element(By.XPATH,"//iframe[contains(@title,'Field container for: Card number')]")
    driver.switch_to.frame(iframe_card)
    card_number = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Card number']")
    print(card_number.is_displayed())
    card_number.send_keys("0000000")
    
    driver.switch_to.default_content()

    iframe_exp = driver.find_element(By.XPATH,"//iframe[contains(@title,'Field container for: Expiration date')]")
    driver.switch_to.frame(iframe_exp)
    exp_date = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Expiration date (MM/YY)']")
    print(exp_date.is_displayed())
    exp_date.send_keys("9")
    time.sleep(0.5)
    exp_date.send_keys("26")
    driver.switch_to.default_content()

    iframe_name = driver.find_element(By.XPATH,"//iframe[contains(@title,'Field container for: Name on card')]")
    driver.switch_to.frame(iframe_name)
    name = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Name on card']")
    print(name.is_displayed())
    name.send_keys("Pantofaru Tudor Mihai")
    driver.switch_to.default_content()

    #payment = driver.find_element(By.ID,"checkout-pay-button").click()



def b_checkout(url):
    driver.get(url)
    

    # --Section 2:  Finding the first tee on the page, selecting the colour and size
    WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.XPATH,"//*[contains(text(),'Tee')]")))
    btn_tee = driver.find_element(By.XPATH,"//*[contains(text(),'Tee')]")
    time.sleep(1)
    btn_tee.click()

    time.sleep(1)

    colour = driver.find_element(By.XPATH,"//button[contains(@title,'White')]")
    colour.click()

    time.sleep(0.3)

    size = driver.find_element(By.XPATH,"//select/option[contains(text(),'Large')]")
    if size.is_displayed() == True:
        size.click()
    else:
        size = driver.find_element(By.XPATH,"//select/option[contains(text(),'Medium')]")
        if size.is_displayed() == False:
            size = driver.find_element(By.XPATH,"//select/option[contains(text(),'Small')]")
            size.click()
        else:
            return restart_program() #nu stiu daca merge sigur
    
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
chrome_options = webdriver.ChromeOptions()

proxy_address = "brd.superproxy.io:22225"
chrome_options = Options()
#chrome_options.add_argument(f'--proxy-server={proxy_address}')
# Initialize the driver with the options
#driver = webdriver.Chrome(options = chrome_options)

url = "https://eu.supreme.com/collections/t-shirts"

start_time = time.time()
b_checkout(url)
end_time = time.time()
print(end_time - start_time)
time.sleep(600)  