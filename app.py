from flask import flask
from flask import jsonify

app = flask(__name__)

@app.route("/")
def hello():
    return jsonify({
    'message':'mahesh',
    'flag':true})

if__name__ =="__main__":
    app.run(debug=true)
