

from flask import Flask, send_from_directory, render_template, request, abort
import time 
# from src.models.inference import *



app = Flask(__name__, static_url_path="/static")
app.config.from_object("default_settings")

from src.inference import *
from src.inference_classes import *

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

    # # test_value, errors = validate_input(data)

    # if not errors:
    #     predicted_class = predict_wine(test_value)
    #     return render_template("results.html", predicted_mask=predicted_mask)
    # else:
    #     return abort(400, errors)

    
    return render_template("results.html",timestamp=str(time.time()))





# if __name__ == "__main__":
#     serve(app, host='0.0.0.0', port=5000)

