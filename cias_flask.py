""" cias_flask.py

POC Flask app for crestron control front-end

"""

from flask import Flask, render_template, request
import cias_control

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    args = request.args
    msg = ""

    if not args.get("op"):
        # No operation defined, default do nothing
        msg = "Tap desired input:"
    else:
        # Some kind of operation is defined
        # Squash it to an int, op represents which input to switch to
        op = int(args.get("op"))
        cias = cias_control.CiasControl()
        msg = "Switching input to {}".format(cias.get_input_card_name(op))
        cias.route_av(op, 1)

    return render_template('index.html', msg=msg)
