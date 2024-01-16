from dataclasses import dataclass

from logger import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@dataclass
class PathConfig:
    image_path: str = "Screenshots/screenshot.png"
    chrome_driver_path: str = "C:/Users/aman kushwaha/Desktop/The/Web Development/chromedriver-win64/chromedriver.exe"


class GetScreenshots:
    def __init__(self) -> None:
        logging.info("GetScreenshots initialized ...")
        self.paths = PathConfig()
        self.s = Service(self.paths.chrome_driver_path)

    def get_screenshots(self, url: str) -> None:
        driver = webdriver.Chrome(service=self.s)
        driver.get(url)
        driver.save_screenshot(self.paths.image_path)
        driver.quit()
        logging.info("Get the screenshot Successfully...")
