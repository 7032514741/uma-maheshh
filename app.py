from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
    'message':'mahesh',
    'flag':true})

if __name__ =="__main__":
    app.run(debug=true)
