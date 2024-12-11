from flask import Flask, request
from markupsafe import escape
from flask import request
import pickle  as pkl
import numpy as np

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
                <form action="/learn/jamboree" method="get">
                    <button type="submit">Go to Jamboree Admission Chance Prediction</button>
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

@app.route('/learn/jamboree', methods=["GET", "POST"])
def jamboree():
    if request.method == "GET":
        return """ <h1> Jamboree Admission Chance Prediction </h1>
                <br>
                <form action="/" method="get">
                    <button type="submit">Go to Home Page</button>
                </form>
                """
    else:
        """
        An example post JSON:
        {
            "CGPA": 9.24,
            "GRE": 330,
            "TOEFL": 114,
            "University_Rating": 3,
            "Research": 1,
            "LOR": 4.5
        }
        """
        post_req = request.get_json()

        input_data = np.array([[post_req["GRE"], post_req["TOEFL"], post_req["University_Rating"], 5, post_req["LOR"], post_req["CGPA"],post_req["Research"]]]) # my scaler() needs Statement of proposal rating for transforming, so added 5.

        with open('scale_jamboree.pkl', 'rb') as scale_file:
            scaler = pkl.load(scale_file)
        scaled_input = scaler.transform(input_data)
        scaled_input = scaled_input.reshape(-1,1)
        scaled_input = np.append(scaled_input[:3], scaled_input[4:]).reshape(1,-1) # My model doesn't need Statement of Proposal rating, hence removing.

        with open('sk_model_jamboree.pkl', 'rb') as file:
            sk_model = pkl.load(file)
        pred = sk_model.predict(scaled_input)
        if pred<0:
            pred = [0]
        elif pred > 1.00:
            pred = [1.00]
        return f"Your Admission chance is: {pred[0]*100:.3f} %"