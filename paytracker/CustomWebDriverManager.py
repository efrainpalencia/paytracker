import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class CustomWebDriverManager:
    def __init__(self, driver_path: str = None, download_dir: str = None, browser: str = None):
        self.driver_path = driver_path
        self.download_dir = download_dir or os.getcwd()
        self.browser = browser

    def create_driver(self):
        browser = self.browser.lower()

        if browser == "chrome":
            options = ChromeOptions()
            prefs = {
                "download.default_directory": self.download_dir,
                "download.prompt_for_download": False,
                "profile.default_content_setting_values.automatic_downloads": 1,
                "safebrowsing.enabled": True,
            }
            options.add_experimental_option("prefs", prefs)
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        elif browser == "firefox":
            profile = FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.dir", self.download_dir)
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
            profile.set_preference("pdfjs.disabled", True)
            options = FirefoxOptions()
            options.profile = profile
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        elif browser == "edge":
            options = EdgeOptions()
            options.use_chromium = True
            options.add_argument("--start-maximized")
            prefs = {
                "download.default_directory": self.download_dir,
                "download.prompt_for_download": False,
                "profile.default_content_setting_values.automatic_downloads": 1,
                "safebrowsing.enabled": True,
            }
            options.add_experimental_option("prefs", prefs)
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

        else:
            raise ValueError(f"No driver found for browser: {browser}")

        # Go to URL if driver_path is a URL
        if self.driver_path and self.driver_path.startswith("http"):
            driver.get(self.driver_path)
        time.sleep(10)

        return driver
