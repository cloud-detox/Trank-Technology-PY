import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.kamera-express.nl/")
    wait = WebDriverWait(driver, 20)

    request.cls.driver = driver
    request.cls.wait = wait

    yield
    driver.quit()
