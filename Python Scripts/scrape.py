from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Setup WebDriver
driver = webdriver.Chrome("/home/chromedriver-linux64/chromedriver")
driver.maximize_window()
driver.get("https://books.toscrape.com")
time.sleep(2)  # Wait for initial page load

# Create CSV file
with open('Scrapes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Availability"])

    while True:
        # Wait until books are present
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_pod"))
        )

        # Scrape all books on the current page
        books = driver.find_elements(By.CLASS_NAME, "product_pod")
        for book in books:
            title = book.find_element(By.TAG_NAME, "h3").text
            price = book.find_element(By.CLASS_NAME, "price_color").text
            availability = book.find_element(By.CLASS_NAME, "availability").text.strip()
            writer.writerow([title, price, availability])

        # Scroll down to load footer
        driver.execute_script("window.scrollBy(0, 2000)")
        time.sleep(1)

        # Check for 'Next' button
        try:
            next_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//li[@class="next"]/a'))
            )
            next_btn.click()
            time.sleep(2)  # Let next page load
        except:
            print("Scraping complete.")
            break

# Close browser
driver.quit()
