from collections import Counter

from PIL import Image

from logger import logging
from url_screenshot import PathConfig


class GetRGBValues:
    def __init__(self) -> None:
        logging.info("GetRGBValues initialized ...")
        self.path = PathConfig

    def get_rgb(self) -> None:
        logging.info("Getting RGB values ...")
        image: Image = Image.open(self.path.image_path)

        # Convert the image to a list of RGB tuples
        pixels = list(image.getdata())

        # Use Counter to count the occurrences of each color
        color_counts = Counter(pixels)

        # Get the 6 most common colors
        top_colors = color_counts.most_common(6)

        with open("RGB_code/values.txt", "w") as f:
            for i, (color, count) in enumerate(top_colors):
                color_block = "\033[48;2;{};{};{}m    \033[0m".format(
                    color[0], color[1], color[2]
                )

                print(
                    f"Color {i + 1}: {color_block} RGB: {color[:-1]} - Count: {count}"
                )

                f.write(f"RGB: {color[:-1]} - Count: {count} \n")
                logging.info(f"RGB: {color[:-1]} - Count: {count}")
