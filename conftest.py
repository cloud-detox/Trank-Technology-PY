import pytest
from config import base_url
from selenium import webdriver

@pytest.fixture
def driver():
    # service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()