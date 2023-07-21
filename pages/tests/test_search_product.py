import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main import MainPage

@pytest.mark.parametrize("product_name", ["смартфон", "ліхтарик", "планшет"])
def test_search_product(driver, product_name):
    main_page = MainPage(driver)
    main_page.search_for_product(product_name)

    # Завершити введення в поле пошуку перед перевіркою результатів
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".goods-tile__title")))

    product_listings = driver.find_elements(By.CLASS_NAME, "goods-tile__title")
    assert len(product_listings) > 0
