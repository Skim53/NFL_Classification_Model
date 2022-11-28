import joblib
#function that takes predict() function model to predict based on new DVOA values 
def predict(data):
    lr = joblib.load("lr_model.sav")
    return lr.predict(data)