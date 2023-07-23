""" cias_flask.py

POC Flask app for crestron control front-end

"""

from flask import Flask, render_template, request
import cias_control

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    args = request.args

    if args.get("chassis"):
        chassis = args.get("chassis")
        mode = args.get("mode")

        cias = cias_control.CiasControl(chassis)

        if mode == "lcdtest":
            cias.lcd_test()
            return "Testing LCD"

        if mode == "route":
            if args.get("op"):
                # Some kind of operation is defined
                # Squash it to an int, op represents which input to switch to
                op = int(args.get("op"))

                cias.route_av(op, 1)
                return "Switching input"

    # If no op is specified, render the UI
    return render_template('index.html')
