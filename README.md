# Overview
This is a Metabolic Syndrome Prediction Flask app trained with Random forest, KNN, Logistic regression models and stacking ensemble technique with deployment done in Heroku. The model with the best evaluation metric is the hyperparameter tunned Random Forest model with ROC curve of 94%.

Metabolic syndrome is the medical term for a combination of diabetes, high blood pressure (hypertension) and obesity. It puts you at greater risk of getting coronary heart disease, stroke and other conditions that affect the blood vessels.
On their own, diabetes, high blood pressure and obesity can damage your blood vessels, but having all 3 together is particularly dangerous. They're very common conditions that are linked, which explains why metabolic syndrome affects an estimated 1 in 3 older adults aged 50 or over in the UK.

The aim of this project is to identify patients at risk of developing Metabolic Syndrome and also to assist front-line staff in identification and detection of Metabolic Syndrome.

App link: https://metabolicsyndrome.herokuapp.com

## Dataset
The dataset "Metabolic Sydrome data" contains records of 10,046 respondents. For each respondent, 5 attributes are known: Diastolic blood pressure (DSP), Systolic blood pressure (SBP), Fasting blood sugar, Triglycerides, HDL Cholesterol and LDL Cholesterol. and a binary classification response column IDFMetsynd (International Diabetes Federation Metabolic syndrome).

Diastolic blood pressure (DSP): Normal blood pressure range 60-90 *mm/HG*  <br />
Systolic blood pressure (SBP): Normal blood pressure range 95-145 *mm/HG* <br />
Fasting blood sugar: Normal blood glucose level (tested while fasting) for non-diabetics is 70-130 *mg/dL* <br />
Triglycerides: Healthy range is <150 *mg/dL* <br />
HDL Cholesterol: Normal findings for HDL-C are as follows : Male: >45 *mg/dL*, Female: >55 *mg/dL* <br />
LDL Cholesterol: Normal findings for LDL-C are as follows : Male: <100 *mg/dL*, Female: <100 *mg/dL* <br />
## Algorithms
The algorithms leveraged in this project are Random Forest, KNN, Logistic Regression and Stacking ensemble and the AUC-ROC Curve is the metric used for model evaluation.

The **Receiver Operator Characteristic (ROC)** curve is an evaluation metric for binary classification problems. The **Area Under the Curve (AUC)** is the measure of the ability of a classifier to distinguish between classes and is used as a summary of the ROC curve. **The higher the AUC, the better the performance of the model at distinguishing between the positive and negative classes**.

### Hyperparameter Tunning
Hyperparameter tuning is an essential aspect of machine learning process. A good choice of hyperparameters can really make a model succeed in meeting desired metric value or on the contrary it can lead to a unending cycle of continuous training and optimization. 

### Model Evaluation
The table below shows the evaluation of each model before and after hyperparameter tuning.

| Models | Base Model (%) | Tunned Model (%) |
| :----: | :------------: | :--------------: |
|   RF   |       93       |        94        |
|  KNN   |       89       |        92        |
|   LR   |       89       |        -         |
|   ES   |       93       |        93        |