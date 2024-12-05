import requests 
"""
username = "wwgjmpze"
port = "6540"
address = "198.23.239.134"
password = "2gvl01sl64ce"
proxies = {f"http": "http://{username}:{password}@{address}:{port}"}

r = requests.get("http://httpbin.org/ip", proxies=proxies)

print(r.content)
"""

import time  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
proxy = "115.72.46.111:49000"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)

chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

chrome_options.add_argument("--disable-webrtc")
chrome = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=chrome_options)
chrome.get("http://whatismyipaddress.com") 
time.sleep(1000)