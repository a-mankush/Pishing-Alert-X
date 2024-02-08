import colorgram
import pandas as pd

from color_code import GetRGBValues
from url_screenshot import GetScreenshots, PathConfig

df = pd.read_csv("notebook/data/dataset_B_05_2020.csv")[:500]


class Helpers:
    @staticmethod
    def RGBtoDecimal(rgb) -> int:
        return int("%02x%02x%02x" % (rgb.r, rgb.g, rgb.b), 16)


def getColors(n, i):
    colors = colorgram.extract("Screenshots/url.png", n)
    print(colors)
    return Helpers.RGBtoDecimal(colors[i].rgb)


def get_deci(url, save_screenshot=True):
    ss = GetScreenshots()
    try:
        ss.get_screenshots(url, save_screenshot=True)
        decimal_code = getColors(3, 0)
    except Exception as e:
        print(f"The {url} is not available. The iloc us")
        decimal_code = 0
    return decimal_code


df["color_1"] = df["url"].apply(lambda x: get_deci(x))
# data['color_1'] = data['hash'].apply(lambda x: getColors(x, 3, 0))
print(df[["url", "color_1"]])

df.to_csv("new_df_0_500.csv", index=False)
