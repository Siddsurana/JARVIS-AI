#pip install selenium
from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from as import getcwd
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset.true)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-u1-for-media-stream")
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
website = f"C:\\Users\\factw\\Desktop\\JARVIS\Body\\voice.html"

driver.get(website)

def listen():
	print()
	print(Fore.GREEN + "LISTENING . . .")
	print()
	driver.get(website)
	driver.find_element(by-By.ID, value='start').click()
	while 1
		text=driver.find_element(by-By.ID, value='output').text()
		if text != ''
			print(Fore.BLUE+"YOU SAID : " + text)
			print()
			driver.find_element(by-By.ID, value 'end').click()
			return text
if _name=="main_"
	while 1
		listen()