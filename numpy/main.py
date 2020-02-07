
import logging

from flask import Flask
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import requests

app = Flask(__name__)


@app.route('/calculate')
def calculate():
    return_str = ''
    x = np.array([[1, 2],
                  [3, 4]])
    y = np.array([[5, 6], 
                  [7, 8]])
    return_str += 'x dot y : {}'.format(str(np.multiply(x, y)))
    return return_str


def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)
