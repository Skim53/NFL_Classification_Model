import joblib
#function that takes predict() function model to predict based on new DVOA values 
def predict(data):
    lr = joblib.load(r"C:/Users/17036/Documents/School/Fall_2022/CDS_303/Code/Streamlit/lr_model.sav")
    return lr.predict(data)