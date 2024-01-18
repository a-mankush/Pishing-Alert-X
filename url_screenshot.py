import sys
from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from exception import CustomException
from logger import logging


@dataclass
class PathConfig:
    image_path: str = "static/screenshot.png"
    # Give you own path
    chrome_driver_path: str = "C:/Users/aman kushwaha/Desktop/The/Web Development/chromedriver-win64/chromedriver.exe"


class GetScreenshots:
    def __init__(self) -> None:
        logging.info("GetScreenshots initialized ...")
        self.paths = PathConfig()
        self.s = Service(self.paths.chrome_driver_path)

    def get_screenshots(self, url: str) -> None:
        try:
            option = Options()
            option.add_argument("--headless")
            driver = webdriver.Chrome(service=self.s)

            driver.set_page_load_timeout(30)

            driver.get(url)
            driver.save_screenshot(self.paths.image_path)
            driver.quit()
            logging.info("Get the screenshot Successfully...")

        except Exception as e:
            raise CustomException(e, sys) from e
