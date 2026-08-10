# 5K PB Predictor 

A Machine Learning project that predicts a runner's 5K Personal Best (PB) time based on their training data.

## My explanation of the code

We first import our models that we will be using to make predictions (LinearRegression + DecisionTreeRegressor). We also import numpy to do calculations in python. We then populate the x-axis of our dataset with runners weekly volume(km), average pace , weekly runs, months of training and their age. These are the variables we will be working with to predict the 5k times of the runners. We also have another dataset for the y-axis with each runner's actual PB. So we will be training these 2 datasets to predict a new 5k PB based on our existing runners. For the tree model we have set a max depth of 3 to prevent the tree model from asking too much questions and having the program become slow because of it. We then use the x_train and y_train as the parameters for training both the Linear and Decision Tree model. We then ask the user for their training data, we take their data and put it into a single element array. We then predict the 5k PB with our linear and Decision tree model with the users training data and use the average of the two predictions as our final prediction. If the final prediction lies too much of an outlier (eg. World record or too slow) the final prediction will be set to a fixed value. The predicted time is then displayed in minutes:seconds.
## Description

This project uses Machine Learning to predict a runner's 5K race time based on:

Weekly training volume (km),
Average pace (min/km),
Runs per week,
Months of training,
Age

## Features

Uses two ML models (Linear Regression & Decision Tree),
Realistic predictions with limits,
Beginner to elite runner classification,
Easy-to-use interface

## 🔧 Installation

1. Clone this repository:
```bash
git clone https://github.com/C7G-Coding/Machine-Learning-Task.git
cd machine-learning-task