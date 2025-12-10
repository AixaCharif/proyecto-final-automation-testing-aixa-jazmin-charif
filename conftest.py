import os
import pytest
import logging
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    os.makedirs("reports/logs", exist_ok=True)

    logging.basicConfig(
        filename="reports/logs/execution.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("==== INICIO DE LA EJECUCIÓN ====")


@pytest.fixture
def driver():
    logging.info("Inicializando navegador Chrome")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "profile.managed_default_content_settings.popups": 0
    }

    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    logging.info("Cerrando navegador")
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            filename = f"{item.name}_{timestamp}.png"
            filepath = os.path.join(screenshot_dir, filename)

            driver.save_screenshot(filepath)
            logging.error(f"Test fallido: {filepath}")

        if item.config.pluginmanager.hasplugin("html"):
            extra = getattr(report, "extra", [])
            report.extra = extra
