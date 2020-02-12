

from flask import Flask, send_from_directory, render_template, request, abort
import time 
from src.inference import *
from src.map_selector import *

app = Flask(__name__, static_url_path="/static")
app.config.from_object("default_settings")



@app.route("/")
def index():
    """Return the main page."""
    return send_from_directory("static", "index.html")

@app.route("/get_results", methods=["POST"])
def get_results():
    """ Mask the buildings on the input image """
    img_path = request.form['img_path']
    print(img_path)

    predicted_mask = make_prediction(img_path)

    
    return render_template("results.html", timestamp=str(time.time()))


@app.route("/get_map_results", methods=["POST"])
def get_map_results():
    """ Mask the buildings from the folium live map """
    lat = float(request.form["lat"])
    lng = float(request.form["lng"])
    location = [lat, lng]
    

    print(location)
    m = render_map(location= location, aerial = True)
    capture_map()
    img_path = "../seg_build_flask/static/images/screenshot.png"
    predicted_mask = make_prediction(img_path)

    return render_template("results.html", timestamp = str(time.time()))
    


# if __name__ == "__main__":
#     serve(app, host='0.0.0.0', port=5000)

