from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
website = f"C:\\Users\\ADMIN\\Desktop\\FRIDAY\Body\\voice.html"

driver.get(website)


def Listen():
    print()
    print(Fore.MAGENTA + "LISTENING ... ")
    print()
    driver.get(website)
    driver.find_element(By.ID, 'start').click()
    while True:  # Changed from while 1 to while True
        text = driver.find_element(By.ID, 'output').text
        if text != "":
            print(Fore.YELLOW + "YOU SAID : " + text)
            print()
            driver.find_element(By.ID, 'end').click()
            return text


if __name__ == "__main__":  # Corrected the if __name__ line
    while True:  # Changed from while 1 to while True
        Listen()
