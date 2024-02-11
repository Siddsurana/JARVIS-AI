

from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pathlib
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings

warnings.simplefilter('ignore')
Scriptdir=pathlib.Path().absolute()
url="https://chat.openai.com/c/1a33b37e-4b11-4b88-89ae-c952ffeba00f"
options=uc.ChromeOptions()
options.add_argument('--profile-directory=Default')
options.add_argument(f'--user-data-dir={Scriptdir}\\chromedata')
driver=uc.Chrome(options=options)
driver.maximize_window()
driver.get(url=url)

def Chapgpt(query):
    prompt_element=driver.find_element(By.ID,"prompt-textarea")
    prompt_element.clear()
    prompt_element.send_keys(query)
    prompt_element.send_keys(keys.ENTER)
    sleep(1)
    while 1:
        try:
            sleep(0.1)
            driver.find_element(By.XPATH,'//*[@id="_next"]/div[1]/div[2]/main/div[2]/div[2]/form/div/div/div/button').click(
            )
        except:
               pass
    driver.find_elements(By.CLASS_NAME,"markdown")[-1].click()  
    A=driver.find_elements(By.CLASS_NAME,"markdown")[-1].text
    while 1:
        
            sleep(1)
            if driver.find_elements(By.CLASS_NAME,"markdown")[-1].text==A:
                 break
            else:
                 A=driver.find_elements(By.CLASS_NAME,"markdown")[-1].text
                 
            
            return A
            
            if __name__ == "__main__":
                 while 1:
                    ChapGpt("reply in less words")
                    A=input(">>> ")+""
                    C=t()
                 
                 
                    print(Chapgpt(A))
                    print(t()-C)


'''from time import sleep, time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pathlib
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings

warnings.simplefilter('ignore')
Scriptdir = pathlib.Path().absolute()
url = "https://chat.openai.com/c/1a33b37e-4b11-4b88-89ae-c952ffeba00f"
options = uc.ChromeOptions()
options.add_argument('--profile-directory=Default')
options.add_argument(f'--user-data-dir={Scriptdir}\\chromedata')
driver = uc.Chrome(options=options)
driver.maximize_window()
driver.get(url=url)


def Chapgpt(query):
    prompt_element = driver.find_element(By.ID, "prompt-textarea")
    prompt_element.clear()
    prompt_element.send_keys(query)
    prompt_element.send_keys(Keys.ENTER)
    sleep(1)
    while True:
        try:
            sleep(0.1)
            driver.find_element(By.XPATH, '//*[@id="_next"]/div[1]/div[2]/main/div[2]/div[2]/form/div/div/div/button').click()
        except NoSuchElementException:
            break

    driver.find_elements(By.CLASS_NAME, "markdown")[-1].click()
    A = driver.find_elements(By.CLASS_NAME, "markdown")[-1].text
    while True:
        sleep(1)
        if driver.find_elements(By.CLASS_NAME, "markdown")[-1].text == A:
            break
        else:
            A = driver.find_elements(By.CLASS_NAME, "markdown")[-1].text

    return A


def main():
    while True:
        query = input(">>> ") + ""
        start_time = time()
        result = Chapgpt(query)
        print(result)
        print("Execution time:", time() - start_time)


if __name__ == "__main__":
    main()
'''
            

       



