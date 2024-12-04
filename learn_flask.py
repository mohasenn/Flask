from flask import Flask
from markupsafe import escape
from flask import request
import pickle  as pkl

app = Flask(__name__)

# begin
@app.route("/", methods=["GET"])
def hello_world():
     return '''
        <h>Hello, There!</h>
        <br>
        <p>Click any of the buttons below to go to that page:</p>
        <form action="/hello" method="get">
            <button type="submit">Go to Hello Page</button>
        </form>
        <form action="/ping" method="get">
            <button type="submit">Go to JSON Style Page</button>
        </form>
        <form action="/learn" method="get">
            <button type="submit">Go to Learn Page</button>
        </form>
    '''

# HTML escaping
@app.route("/<name>", methods=["GET"])
def hello(name):
    return f"""Hello, {escape(name)}! <br> This is not the correct url. <br> I have this text to avoid 404 error.
    <br>
    <form action="/" method="get">
            <button type="submit">Go to Home Page</button>
        </form>
    """

# routing - 1
@app.route('/hello', methods=["GET"])
def hello_specific():
    return """Hello, there. You have found an easter egg! Ha Ha.
                <br>
                <form action="/" method="get">
                    <button type="submit">Go to Home Page</button>
                </form>
           """

# routing - 2
@app.route('/learn', methods=["GET"])
def learn():
    return """In this page, I am practising Flask. 
                <br>
                <form action="/learn/loantap" method="get">
                    <button type="submit">Go to LoanTap Application Prediction</button>
                </form>
                <br>
                <form action="/" method="get">
                    <button type="submit">Go to Home Page</button>
                </form>
           """

# routing - 3
@app.route('/ping', methods=['GET'])
def ping():
    return {"message": "Why are you pining me?", "reply": "This is for testing purpose."}

# Model
# model_file = open("loan_application_classifier_sk_version_1.5.2.pkl", "rb")
# model = pkl.load(model_file)

@app.route('/learn/loantap', methods=["GET"])
def loan_tap():
    return """ <h1> Loan Approval Application </h1>
                <br>
                <form action="/" method="get">
                    <button type="submit">Go to Home Page</button>
                </form>
           """

# continue building using this: https://github.com/mohit2016/Flask-Dec24/blob/main/loan.py 