import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chromium.service import ChromiumService as ChromiumService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager



# This creates my setup and tear-down approach
# This approach is for multi-browser testing

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="browser type")
    parser.addoption("--platform",action="store_true",default="windows",help="platform type")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options=FirefoxOptions()
        service=FirefoxService(GeckoDriverManager().install())
        driver=webdriver.Firefox(service=service, options=options)
    elif browser == "edge":
        options=EdgeOptions()
        service=EdgeService(EdgeChromiumDriverManager().install())
        driver=webdriver.Edge(service=service, options=options)
    elif browser == "ie":
        options=IeOptions()
        service= IeService(IEDriverManager().install())
        driver=webdriver.Ie(service=service, options=options)
    elif browser == "chromium":
        options=ChromiumOptions()
        service=ChromiumService(EdgeChromiumDriverManager().install())
        driver=webdriver.Chrome(service=service, options=options)
    else:
        raise Exception(f'Broswer {browser} not supported.')

    wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()