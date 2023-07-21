from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        product_link = self.driver.find_element(By.CSS_SELECTOR, ".goods-tile__heading a")
        product_link.click()

        add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, "button.buy-button")
        add_to_cart_button.click()
