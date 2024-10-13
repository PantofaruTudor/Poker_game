from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# --Section1: Initialize the web driver and load the page
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"


WebDriverWait(driver,5).until(
   EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'Consent')]"))
)

# --Section 2: Find the first cookie on the page, select the button and click it
cons = driver.find_element(By.CLASS_NAME,"fc-button-label")
print("Element is visible?" + str(cons.is_displayed()))#CHIAR L AM GASIT........SUNT BUN
time.sleep(5)
cons.click()


# -- Section 3: Find the english language and click it
WebDriverWait(driver,5).until(
   EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'English')]"))
) 
language = driver.find_element(By.XPATH,"//*[contains(text(),'English')]")
print("am gasit")
language.click()

time.sleep(5)

# --Section 4: Find the cookie on the page using it's id and click it
WebDriverWait(driver,5).until(
   EC.presence_of_element_located((By.ID,cookie_id))
) 

cookie = driver.find_element(By.ID, cookie_id)
cookie.click()

time.sleep(2)

# --Section 5: Click the cookie many times until we unlock the rest of options, after that we find and buy them

while True:
   cookie.click()
   cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
   cookies_count = int(cookies_count.replace(",", ""))

   for i in range(4):
      product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

      if not product_price.isdigit():
         continue

      product_price2 = int(product_price)
      
      if cookies_count >= product_price2:
         print("imi permit")
         product = driver.find_element(By.ID, product_prefix + str(i))
         product.click()
         break