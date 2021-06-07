import json
import os

import allure
import pytest
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

from constants.general_constants import *


@pytest.fixture(scope="class")
def get_driver(request):
    driver = None
    browser = os.environ[BROWSER]
    run_type = os.environ[TYPE]
    headless = False
    if run_type == Types.DESKTOP.value:

        if browser == Browsers.CHROME.value:
            chrome_options = ChromeOptions()
            if os.environ[HEADLESS] == "True":
                chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

            if THROUGHPUT in os.environ.copy():
                driver.set_network_conditions(
                    offline=False,
                    latency=5,
                    throughput=int(os.environ[THROUGHPUT]) * 1024,
                )
        elif browser == Browsers.FIREFOX.value:
            firefox_options = FirefoxOptions()
            if os.environ[HEADLESS] == "True":
                firefox_options.headless = True
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
        elif browser == Browsers.IE.value:
            ie_options = IeOptions()
            if os.environ[HEADLESS] == "True":
                ie_options.set_capability("headless", True)
            driver = webdriver.Ie(IEDriverManager().install())
        elif browser == Browsers.EDGE.value:
            edge_options = EdgeOptions()
            if os.environ[HEADLESS] == "True":
                edge_options.set_capability("headless", True)
            driver = webdriver.Edge(EdgeChromiumDriverManager().install(), edge_options=edge_options)
        elif browser == Browsers.SAFARI.value:
            driver = webdriver.Safari()
        driver.maximize_window()
    elif run_type == Types.MOBILE.value:
        with open(Files.DEVICE_CONFIG.value) as f:
            desired_caps = json.load(f)
        driver = webdriver.Remote(Urls.APPIUM_URL.value, desired_caps)
    elif run_type == Types.BS_DESKTOP.value:
        with open(Files.BS_CONFIG.value) as f:
            desired_caps = json.load(f)
        desired_cap_web = desired_caps.get('web').get(browser)
        driver = webdriver.Remote(
            command_executor=Urls.BS_URl.value.format(
                desired_caps['username'], desired_caps['key']),
            desired_capabilities=desired_cap_web)
    elif run_type == Types.BS_MOBILE.value:
        with open(Files.BS_CONFIG.value) as f:
            desired_caps = json.load(f)
        desired_cap_mobile = desired_caps['mobile'][browser]
        driver = webdriver.Remote(
            command_executor=Urls.BS_URl.value.format(
                desired_caps['username'], desired_caps['key']),
            desired_capabilities=desired_cap_mobile)

    request.cls.driver = driver
    yield
    driver.close()
    if headless:
        display.stop()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def py_test_run_test_make_report(item):
    outcome = yield
    rep = outcome.get_result()

    if (rep.when == "call" or rep.when == "setup") and rep.failed:
        try:
            allure.attach(item.instance.driver.get_screenshot_as_png(),
                          name=item.name,
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(e)
