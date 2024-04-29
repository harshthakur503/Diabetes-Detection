# Diabetes Detection Using Deep Neural Network

This project implements a simple Deep Neural Network to perform binary classification, determining whether a given patient is diabetic or not based on various factors. It utilizes the Keras library and a sequential neural network architecture with four layers.

## Project Overview

The dataset used in this project contains information on various factors such as glucose concentration, blood pressure, BMI, etc., which are used to predict the likelihood of a person having diabetes. The dataset is split into input variables (X) and output variable (y), with 80% used for training and 20% for testing.

## Model Architecture

The model consists of four layers, with 64, 32, 16, and 1 neurons in each layer, respectively. The activation function used is ReLU for hidden layers and Sigmoid for the output layer. The model is compiled using binary cross-entropy as the loss function and RMSprop as the optimizer.

## Training and Evaluation

The model is trained for 100 epochs on the training data and evaluated on the testing set. After training, the model achieves an accuracy of approximately 71.4%. The test loss decreases as the number of epochs increases, indicating the model's improving performance.

## Results

The results for the test set are displayed below, showing whether each patient is diabetic or not based on the model's predictions. Additionally, a graphical representation of the training process is provided in the image below.

## Project Structure

- `diabetes_detection.ipynb`: Jupyter Notebook containing the code for the project.
- `pima-indians-diabetes.data.csv`: Dataset used for training and testing.

## Requirements

- Python 3.x
- Jupyter Notebook
- NumPy
- Pandas
- Keras
- scikit-learn

## Results Visualization

![Training Process](/Users/harshthakur/Documents/VSC/Deep Learning Project/epochs.png)

