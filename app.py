from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('rf_classification_model.pkl', 'rb')) 
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        DBP = float(request.form['DBP'])
        SBP = float(request.form['SBP'])
        FastingBloodSugar = float(request.form['FastingBloodSugar'])
        Triglycerides = float(request.form['Triglycerides'])
        HDLcholestrol = float(request.form['HDLcholestrol'])
        LDLcholestrol = float(request.form['LDLcholestrol'])

        prediction=model.predict([[DBP,SBP,FastingBloodSugar,Triglycerides,HDLcholestrol,LDLcholestrol]])
        output=prediction
        if output < 1:
            return render_template('index.html',prediction_texts="Unlikely to suffer from Metabolic Syndrome")
        else:
            return render_template('index.html',prediction_text="Likely to suffer from Metabolic Syndrome")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
