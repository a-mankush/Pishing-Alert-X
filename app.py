from flask import Flask, render_template, request

from color_code import GetRGBValues
from url_screenshot import GetScreenshots

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("form.html")
    url: str | None = request.form.get("url")
    ss = GetScreenshots()
    ss.get_screenshots(url, save_screenshot=True)
    val = GetRGBValues(6)
    colors_info: list[dict] = val.get_rgb()
    return render_template("index.html", colors_info=colors_info)


if __name__ == "__main__":
    app.run(debug=True)
