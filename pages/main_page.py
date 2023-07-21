from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def search_for_product(self, product_name):
        self.driver.get("https://rozetka.com.ua/ua/")
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='search']")
        search_input.send_keys(product_name)

        search_button = self.driver.find_element(By.CSS_SELECTOR, "button.button_color_green")
        search_button.click()
