from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import sb_cl_nlp_for_app as spam

app = Flask(__name__)
CORS(app)

app.debug = True

@app.route('/', methods=['GET'])
def healthcheck():
    return 'It works!'

@app.route('/', methods=['POST'])
def checkSpam():
    if request.form["msg"]:
        msg = request.form['msg']
        res = spam.checkSpam(msg)
        return jsonify(result=int(res))
    return ''
if __name__ == '__main__':
    app.run()