# Mtcars Flask API

This project is a Flask-based machine learning API that predicts the fuel efficiency (MPG) of a car using the mtcars dataset. The model is trained using a linear regression algorithm and is deployed as a RESTful API.

### Key Components:

- `main.py`: Flask application exposing the `/predict` endpoint
- `model.pkl`: Serialized regression model trained on `mtcars.csv`
- `Dockerfile`: Docker setup for containerization
- `requirements.txt`: Python dependencies
