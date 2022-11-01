from flask import Flask


app = Flask(__name__)


@app.route('/')
def Index():
    return "Hello Flask Application"



if __name__=="__main__":
    app.run(debug=True)
