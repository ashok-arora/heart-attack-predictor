from flask import Flask
from flask import request
from flask import jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import RobustScaler

with open("final_model_lr.bin", "rb") as f_in:
    model = pickle.load(f_in)


app = Flask("Heart Attack Prediction")
df = pd.read_csv('./heart.csv')
@app.route("/", methods=["GET"])
def greet():
    return "Welcome to Heart Attack Prediction API. \nPOST patient data to /predict endpoint to get prediction stats. \nGET sample patient data at /sample endpoint."


@app.route("/sample", methods=["GET"])
def sample_data():
    return df.iloc[[0]].reset_index().to_dict()

@app.route("/predict", methods=["POST"])
def predict():
    global df
    cat_cols = ['sex', 'cp', 'fbs', 'restecg', 'exng', 'slp', 'caa', 'thall']
    num_cols = ['age', 'trtbps', 'chol', 'thalachh', 'oldpeak']
    print(request.get_json())
    # return(request)
    patient_data = pd.DataFrame.from_dict(request.get_json(), orient="index").T
    patient_data['output'] = 1
    print(patient_data)
    # return "OK"
    patients = df.append(patient_data).reset_index(drop=True)

    print(patients.iloc[303])
    # return "OK"

    X = patients.drop(['output'],axis=1)
    y = patients[['output']]

    X = pd.get_dummies(X, columns = cat_cols, drop_first = True)
    print(X.iloc[302])
    # return "OK"
    scaler = RobustScaler()

    X[num_cols] = scaler.fit_transform(X[num_cols])

    # print(X.iloc[303])
    # return "OK"

    y_pred = model.predict_proba(X.iloc[[303]])[:, 1]
    prediction = y_pred[0]
    print(prediction)
    if prediction >= 0.5:
        verdict = "High Risk"
    else:
        verdict = "Low Risk"

    result = {"hit_probability": float(prediction), "verdict": verdict}
    df.drop(df.tail(0).index,inplace=True)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)
