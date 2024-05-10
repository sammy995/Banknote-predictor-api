The Bank Note Predictor App is a machine learning application that predicts whether a bank note is real or fake based on its characteristics. 
The application uses a Random Forest Classifier trained on specific features of bank notes, and it exposes an API for making predictions via FastAPI.

### Technologies Used
Python: The primary programming language used for developing this application.
Pydantic: Utilized for data validation and settings management using Python type annotations.
Pandas: A library for data manipulation and analysis. Used here to read and process the dataset.
NumPy: Essential for numerical operations on arrays.
Scikit-learn: Machine learning library used to train the Random Forest Classifier and split the dataset.
FastAPI: A modern, fast web framework for building APIs. Used to create endpoints for the application.
Pickle: Used to serialize and deserialize the trained model for use in the API.
Uvicorn: An ASGI server for FastAPI that allows the app to run and handle requests.


### Application Structure
BankNote.py: Defines a BankNote class using Pydantic's BaseModel. This class models the data structure for a bank note with attributes:
variance: Float
skewness: Float
curtosis: Float
entropy: Float

### banknote_classifier.py: 
Contains the code to load the dataset (BankNote_Authentication.csv), preprocess it, and train a Random Forest Classifier. The model is then serialized using pickle for later use in predictions.
### main.py: 
The core of the web application, built with FastAPI. This file includes:

### Endpoint /: A simple root API that returns a welcome message.
### Endpoint /welcome: Returns a personalized message for the user.
### Endpoint /predict: Takes a BankNote object as input, validates and transforms it into a dictionary, uses the pre-trained classifier to predict the authenticity of the note, and returns whether the note is real or fake.


Running the Application
To run this application, ensure you have all the dependencies installed, then execute the following command in the terminal:

```bash
uvicorn main:my_app --host=127.0.0.1 --port=8080
```
This starts the FastAPI app on localhost at port 8080.

Conclusion
The Bank Note Predictor App is a straightforward demonstration of integrating machine learning with a web API. It showcases the use of several Python libraries to build a functional and interactive application that can predict the authenticity of bank notes based on their features. ​

### Additional Resources:
[Project details & screenshots](https://www.notion.so/Portfolio-Projects-SRL-83d36d9c198b409b8ec6a798b2df68d4?p=6dabb81aef3543d98779b30797c406f9&pm=c)
