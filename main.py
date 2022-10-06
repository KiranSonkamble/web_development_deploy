from flask import Flask
from flask import render_template, request
import pickle


# Load the model
model = pickle.load(
    open('diabetic.pkl', 'rb'))

# initialize the app
app = Flask(__name__)

# tells what to do


@app.route('/')
def hello():
    return render_template('main.html')

# Just for understanding


@app.route('/gallery')
def gallery():
    return 'welome to gallery'


@app.route('/demo')
def demo():
    return render_template('demo.html')


@app.route('/submit', methods=['post'])
def submit():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    # predict the diabetic or not
    pred_list = [preg, plas, pres, skin, test, mass, pedi, age]
    op = model.predict([[float(x) for x in pred_list]])
    # op loop bacause to solve numeric issue
    if op[0] == '1':
        return 'Diabetic'
    else:
        return 'not Diabetic'
    # return 'submitted'


# runt the app
# app.run(debug=True)
app.run(host='0.0.0.0', port=8080)
