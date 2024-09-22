# Titanic Survival Prediction App 🚢

This project is a machine learning application that predicts whether a passenger would have survived the Titanic disaster based on several input features. The application is built using Streamlit and containerized with Docker.

## Project Overview

The Titanic Survival Prediction App allows users to input data about a passenger and receive a prediction on whether that passenger would have survived the Titanic disaster. The model was trained on the famous Titanic dataset.

## Features

- Predict survival based on passenger class, gender, age, fare, and port of embarkation.
- User-friendly web interface built with Streamlit.
- Dockerized for easy deployment and consistent environment setup.

## Setup Instructions

### Prerequisites

- Python 3.12
- Poetry
- Docker

### Installation

1. **Clone the Repository**

   Clone the repository from GitHub and navigate to the project directory.

2. **Set Up the Python Environment**

   Install dependencies using Poetry.

3. **Train the Model (Optional)**

   If you want to retrain the model, you can run the training script.

### Running the App Locally

1. **Activate the Poetry Environment**

   Activate the environment created by Poetry.

2. **Run the Streamlit App**

   Run the application with Streamlit.

3. **Access the App**

   Open your browser and go to `http://localhost:8501`.

## Running the App with Docker

1. **Build the Docker Image**

   Build the Docker image using the Dockerfile provided.

2. **Run the Docker Container**

   Run the container and map the ports.

3. **Access the App**

   Open your browser and go to `http://localhost:8501`.

## Authors and Acknowledgments

- **Zakaria Atlassi** - Initial work - [GitHub](https://github.com/zakatlassi)
- Dataset from [Kaggle](https://www.kaggle.com/c/titanic/data)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Project Status

The project is currently complete. Future improvements may include more advanced feature engineering, model tuning, and deployment to a cloud platform.