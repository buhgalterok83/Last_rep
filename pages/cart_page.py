from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def is_product_in_cart(self):
        cart_remove_button = self.driver.find_element(By.CSS_SELECTOR, ".cart-product__delete")
        return EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-product__delete"))

    def remove_product_from_cart(self):
        cart_remove_button = self.driver.find_element(By.CSS_SELECTOR, ".cart-product__delete")
        cart_remove_button.click()

    def get_cart_total_price(self):
        cart_total_price = self.driver.find_element(By.CSS_SELECTOR, ".cart-modal__total-price .cart-modal__total-price-value")
        total_price_value = float(cart_total_price.text.replace(" ", "").replace(",", "."))
        return total_price_value
