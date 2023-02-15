import os
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.sacred-texts.com/hin/m01/index.htm"

driver = webdriver.Firefox()
driver.get(URL)

for i in range(17):
    sections = len(driver.find_elements(
        by=By.XPATH, value="//a[contains(text(), 'Section')]"))
    os.mkdir(f"Books/Book {i + 1}")
    for j in range(sections):
        section = driver.find_element(
            by=By.XPATH, value=f"//a[contains(text(), 'Section')][{j + 1}]")
        section.click()
        section_data = ""
        for para in driver.find_elements(by=By.XPATH, value="//p[position() > 1]"):
            if para.text.startswith("p."):
                continue
            section_data += para.text + "\n"
        with open(f"Books/Book {i + 1}/Section {j + 1}.txt", "w") as file:
            file.write(section_data)
        driver.back()
    driver.find_element(
        by=By.XPATH, value=f"//a[text()='Book {i + 2}']").click()
driver.close()
