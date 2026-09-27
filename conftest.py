import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выбор браузера для тестов: chrome или firefox"
    )


@pytest.fixture(scope="session")
def target_url():
    return "https://practice-automation.com/iframes/"


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser").lower()

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # options.add_argument("--headless=new")
        driver_instance = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        driver_instance = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
        driver_instance.maximize_window()
    else:
        raise pytest.UsageError(f"--browser={browser_name} не поддерживается. Доступны: chrome, firefox")

    driver_instance.implicitly_wait(0)

    yield driver_instance

    driver_instance.quit()
