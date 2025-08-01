import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from write_to_csv import write_to_csv
def scrap(driver , city):

    """Scraps the page and extracts the leads

    Args:
        driver (webdriver): Webdriver object
        city (str): Name of the city to scrap

    Returns:
        None

    functionality: Scraps the page and extracts the leads, Thrn calls write_to_csv to write the leads to the csv file
    """

    time.sleep(5)

    leads = []

    items = driver.find_elements(By.CSS_SELECTOR , ".c7ff6507.db9a2680")

    print(f"len of item {len(items)}")

    for i , lead in enumerate(items , start=1):

        print(f"processing {i}")

        container1 = lead.find_element(By.CSS_SELECTOR , ".ad3ccf1a")

        load_dict = {}

        if ':' in container1.text:

            headline , summary = container1.text.strip().split(":" , 1)

            load_dict['headline'] = headline

            load_dict['summary'] = summary

        container2 = lead.find_element(By.CSS_SELECTOR , "span.fd4e34d0 a") 

        load_dict['Area'] = container2.text.strip()

        leads.append(load_dict)

    output_filename = f"{city}_new_leads.csv"

    write_to_csv(leads , output_filename)
