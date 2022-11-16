import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



ACCOUNT_EMAIL = "Email"
ACCOUNT_PASSWORD = "Password"



## chrome_driver_path
chrome_driver_path = "C:\Development\chromedriver"
serv = Service(chrome_driver_path)

driver = webdriver.Chrome(service=serv)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3198960669&geoId=101620260&keywords=software%20engineer%20junior")

time.sleep(1)
sign_in = driver.find_element(By.CSS_SELECTOR,
                              "body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in.click()

# Sign in user with password and email.
emailEntry = driver.find_element(By.ID, "username")
emailEntry.send_keys(ACCOUNT_EMAIL)
passEntry = driver.find_element(By.ID, "password")
passEntry.send_keys(ACCOUNT_PASSWORD)
sign_in = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
sign_in.click()

# Selecting the pages that we want to get the links of jobs in linkedin website.
print(f'Collecting the links in the page: {0}')
for page in range(2, 14):
    time.sleep(2)
    jobs_block = driver.find_elements(By.CSS_SELECTOR, "#main > div > section.scaffold-layout__list > div > ul")
    links = []
    for job in jobs_block:
        all_links = job.find_elements(By.TAG_NAME, 'a')
        for a in all_links:
            if str(a.get_attribute('href')).startswith("https://www.linkedin.com/jobs/view") and a.get_attribute(
                    'href') not in links:
                links.append(a.get_attribute('href'))
                print(a.get_attribute('href'))
            else:
                pass
        driver.execute_script("arguments[0].scrollIntoView();", job)

    print(f'Collecting the links in the page: {page - 1}')
    # go to next page:
    driver.find_element(By.XPATH, f"//button[@aria-label='Page {page}']").click()
    time.sleep(3)

driver.quit()
