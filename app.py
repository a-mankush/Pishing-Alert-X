from color_code import GetRGBValues
from url_screenshot import GetScreenshots


def main():
    ss = GetScreenshots()
    ss.get_screenshots("https://www.python.org/")
    obj = GetRGBValues()
    obj.get_rgb()


if __name__ == "__main__":
    main()
