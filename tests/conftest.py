import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    """Функция-фикстура для инициализации браузера"""
    driver = webdriver.Chrome(executable_path='../chromedriver_win/chromedriver.exe')
    driver.maximize_window()

    yield driver
    driver.quit()

