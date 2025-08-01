import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from page_scrapper import scrap

def setup_driver():

    '''Setting up the chrome driver'''

    options = Options()
    options.add_argument("--window-size=1024,720")
    options.add_argument("--incognito")
    options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service , options = options)

    return driver

def close(driver):

    '''Closing the chrome driver'''
    driver.quit()

def main():

    print("Welcome to NEWS FETCH AI")
    print("="*20)


    choice = input("""Which newspaper do u want to read?
1. Bhaskar
2. Amarujala
Hit 1 for Bhaskar and 2 for Amarujala
""").strip()

    choice2 = input("""Do you want to read news about:
1.state 
2.city
Hit 1 for state and 2 for city
""").strip()
    

    
    if choice == "1" and choice2 == "1":
        state = input("Enter the state name:").strip()

        url = f"https://www.bhaskar.com/local/{state}"

    elif choice == "1" and choice2 == "2":
        city = input("Enter the city name:").strip()

        state = input("Enter the state the city belongs to:").strip()

        url = f"https://www.bhaskar.com/local/{state}/{city}"

    elif choice == "2" and choice2 == "1":
        state = input("Enter the state name:").strip()

        url = f"https://www.amarujala.com/{state}"

    elif choice == "2" and choice2 == "2":
        city = input("Enter the city name:").strip()

        state = input("Enter the state the city belongs to:").strip()    

        url = f"https://www.amarujala.com/{state}/{city}"

    else:
        print("Invalid choice")
        exit()

    print(f"url is {url}")

    print("Setting up the driver")
    
    driver = setup_driver()

    print("driver setup complete")
    
    driver.get(url)

    time.sleep(5)

    print("scraping the page")

    try:
        scrap(driver , city)

    except Exception as e:
        print("Error occured while scraping the page , Check your internet connection and try again")

    time.sleep(5)

    close(driver)

if __name__ == "__main__":
    main()