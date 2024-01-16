from flask import Flask, render_template

from color_code import GetRGBValues
from url_screenshot import GetScreenshots

app = Flask(__name__)


@app.route("/")
def index():
    # ss = GetScreenshots()
    # ss.get_screenshots("https://www.python.org/")
    val = GetRGBValues()
    colors_info = val.get_rgb()
    return render_template("index.html", colors_info=colors_info)


if __name__ == "__main__":
    app.run(debug=True)
