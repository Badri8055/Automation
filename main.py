from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


username = "BadriNarayanan"
password = "Qwerty@123"

url = "https://demoqa.com/login"
driver = webdriver.Chrome()

driver.get(url)

username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "userName"))
)

username_input.send_keys(username)

password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)


password_input.send_keys(password)


login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login"))
)

driver.execute_script("arguments[0].scrollIntoView(true);", login_button)

sleep(3)

login_button.click()

print("Logged In Successfully\n")

driver.get("https://demoqa.com/books")

sleep(3)

table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "app"))
)

rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")

for row in rows:
    cells = row.find_elements(By.CSS_SELECTOR, ".rt-td")

    if len(cells) >= 3:
        title, author, publisher = [cell.text for cell in cells[1:4]]
        print("Title:", title)
        print("Author:", author)
        print("Publisher:", publisher)
        print("-" * 50)

driver.quit()