import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.set_window_size(1920, 1080) 
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()
