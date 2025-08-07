import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductCartTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialize the Chrome browser"""
        chrome_path = "/home/chromedriver-linux64/chromedriver"
        service = Service(executable_path=chrome_path)
        options = Options()
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.maximize_window()
        cls.driver.get("https://automationexercise.com")

    def test_01_search_product(self):
        """Search for a product after navigating to the 'Products' section"""
        driver = self.driver

        # Wait and click 'Products'
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "card_travel"))
        ).click()

        # Wait for the search input, enter keyword, and search
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search_product"))
        ).send_keys("T-Shirt")

        driver.find_element(By.ID, "submit_search").click()
        driver.execute_script("window.scrollTo(0, 500);")

    def test_02_add_to_cart_and_verify_price(self):
        """Add a product to the cart and compare the price"""
        driver = self.driver

        # Wait for product and capture price
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "add-to-cart"))
        )
        product_price = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/h2')
        price1 = product_price.text.strip()
        print("Product Price:", price1)

        # Hover and click 'Add to cart'
        action = ActionChains(driver)
        product = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a')
        action.move_to_element(product).perform()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/a').click()

        # Screenshot after adding to cart
        time.sleep(2)
        driver.save_screenshot('screenshots/add_to_cart_success.png')

        # View cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[1]/div/div/div[2]/p[2]/a/u'))
        ).click()

        # Get price from cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "check_out"))
        )
        cart_price = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/table/tbody/tr/td[3]/p')
        price2 = cart_price.text.strip()
        print("Cart Price:", price2)

        time.sleep(2)

        # Assertion with better error message
        self.assertEqual(price1, price2, f"Mismatch in price: Expected {price1}, but got {price2}")

    @classmethod
    def tearDownClass(cls):
        """Close the browser"""
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='reports/Selenium'),
        verbosity=2
    )
