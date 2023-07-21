import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main import MainPage

@pytest.mark.parametrize("product_name", ["смартфон", "ліхтарик", "планшет"])
def test_add_to_cart(driver, product_name):
    main_page = MainPage(driver)
    main_page.search_for_product(product_name)

    # Завершити введення в поле пошуку перед перевіркою результатів
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".goods-tile__title")))

    # Клік на перший товар з результатів пошуку
    product_link = driver.find_element(By.CSS_SELECTOR, ".goods-tile__title")
    product_link.click()

    # Дочекатися відображення кнопки додавання до кошика
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.buy-button")))

    # Клік на кнопку додавання товару до кошика
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button.buy-button")
    add_to_cart_button.click()

    # Перевірка успішного додавання до кошика
    success_message = driver.find_element(By.CSS_SELECTOR, ".cart-modal__heading span")
    assert success_message.is_displayed()
