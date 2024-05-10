import uvicorn   # For ASGI
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
from BankNote import BankNote


my_app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


@my_app.get('/')
def index():
    return {'message':'Hello from root API'}


@my_app.get('/welcome')
def get_name(name:str):
    return {'Thank you for checking out my app': f'{name}'}


@my_app.post('/predict')
def predict_note(data: BankNote):
    data = data.dict()
    print(data)
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    prediction = (classifier.predict(
        [[variance,skewness,curtosis,entropy]]
    ))

    if prediction[0]> 0.5:
        prediction = "Fake note"
    else:
        prediction = "Real note"
    return {
        'result':prediction
    }


if __name__ == '__main__':
    uvicorn.run(my_app,host='127.0.0.1',port=8080)


