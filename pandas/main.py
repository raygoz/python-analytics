
import logging

from flask import Flask
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import requests

app = Flask(__name__)


@app.route('/reglineal')
def reglineal():
    return_str = ''
    data=pd.read_csv("day.csv")
    import statsmodels.formula.api as smf

    lm= smf.ols(formula= "cnt~weathersit", data=data).fit()
    lm.params
    print(lm.summary())
    return_str += str (lm.summary())
    #str(lm.rsquared) + ' , ' + str(lm.rsquared_adj)
    return return_str


@app.errorhandler(500)
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
