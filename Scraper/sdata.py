import os
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.sacred-texts.com/hin/mbs/mbsi01.htm"

driver = webdriver.Firefox()
driver.get(URL)

for i in range(17):
    sections = len(driver.find_elements(
        by=By.XPATH, value="//a[contains(text(), 'Chapter')]"))
    os.mkdir(f"SanskritBooks/Book {i + 1}")
    for j in range(sections):
        section = driver.find_element(
            by=By.XPATH, value=f"//a[contains(text(), 'Chapter')][{j + 1}]")
        section.click()
        section_data = driver.find_element(
            by=By.CSS_SELECTOR, value="td:first-child").text
        with open(f"SanskritBooks/Book {i + 1}/Section {j + 1}.txt", "w", encoding='utf-8') as file:
            file.write(section_data)
        driver.back()
    driver.find_element(
        by=By.XPATH, value=f"//a[text()='Book {i + 2}']").click()
driver.close()
