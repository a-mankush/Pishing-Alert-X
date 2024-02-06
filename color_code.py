import sys
from collections import Counter
from typing import Any

import colorgram
from PIL import Image

from exception import CustomException
from logger import logging
from url_screenshot import PathConfig

TARGET_PATH = "Screenshots"


class Helpers:
    @staticmethod
    def RGBtoDecimal(rgb) -> int:
        return int("%02x%02x%02x" % (rgb.r, rgb.g, rgb.b), 16)


class GetRGBValues:
    def __init__(self, number_of_colors: int) -> None:
        logging.info("GetRGBValues initialized ...")
        self.path = PathConfig
        self.number_of_colors: int = number_of_colors

    def get_rgb(self):
        try:
            logging.info("Getting RGB values ...")
            image: Image = Image.open(self.path.image_path)

            # Convert the image to a list of RGB tuples
            pixels = list(image.getdata())

            # Use Counter to count the occurrences of each color
            color_counts = Counter(pixels)

            # Get the 6 most common colors
            top_colors = color_counts.most_common(self.number_of_colors)

            colors_info: list = []

            with open("RGB_code/values.txt", "w") as f:
                for i, (color, count) in enumerate(top_colors):
                    color_block = "\033[48;2;{};{};{}m    \033[0m".format(
                        color[0], color[1], color[2]
                    )
                    hex_color = "#{:02x}{:02x}{:02x}".format(
                        color[0], color[1], color[2]
                    )

                    color_info: dict[str, Any] = {
                        "hex_color": hex_color,
                        "rgb": color[:-1],
                        "count": count,
                    }
                    colors_info.append(color_info)

                    print(
                        f"Color {i + 1}: {color_block} RGB: {color[:-1]} - Count: {count}"
                    )

                    f.write(
                        f"Color {i + 1}: {hex_color} RGB: {color[:-1]} - Count: {count} \n"
                    )

            return colors_info

        except Exception as e:
            raise CustomException(e, sys) from e


def getColors(image, n, i):
    try:
        colors = colorgram.extract(f"{TARGET_PATH}/images/{image}.png", n)
        return Helpers.RGBtoDecimal(colors[i].rgb)
    except Exception as e:
        raise CustomException(e, sys) from e
