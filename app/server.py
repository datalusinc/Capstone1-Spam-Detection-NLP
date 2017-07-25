from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import sb_cl_nlp_for_app as spam

app = Flask(__name__)
CORS(app)

app.debug = True

@app.route('/', methods=['POST'])
def hello_world():
    msg = request.form['msg']
    res = spam.checkSpam(msg)
    return jsonify(result=int(res))

if __name__ == '__main__':
    app.run()