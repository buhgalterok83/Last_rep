# main.py
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


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        product_link = self.driver.find_element(By.CSS_SELECTOR, ".goods-tile__heading a")
        product_link.click()

        add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, "button.buy-button")
        add_to_cart_button.click()


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
