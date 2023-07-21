
import pytest
from selenium import webdriver

# Фікстура для ініціалізації та закриття драйвера браузера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
