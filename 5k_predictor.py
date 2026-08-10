#!/usr/bin/env python3

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import numpy as np

def prediction_5k_pb():
    print("="*50)
    print("5k Personal Best (PB) Predictor")
    print("="*50)

    #Training Data set: [weekly_km, avg_pace, runs_per_week, months_training, age]
    # x-axis 
    x_train = [
        [0, 10.0, 0, 0, 22],   
        [5, 9.0, 1, 1, 30],    
        [8, 8.5, 2, 2, 35],    
        [10, 8.0, 2, 3, 28],   
        [12, 7.5, 3, 4, 40],   
        [15, 7.0, 3, 6, 25], 
        [30, 6.0, 3, 6, 25],
        [45, 5.5, 4, 12, 28],
        [60, 5.0, 5, 18, 22],
        [20, 7.0, 2, 3, 30],
        [50, 5.2, 4, 15, 26],
        [80, 4.5, 6, 24, 20],
        [35, 6.5, 3, 8, 35],
        [55, 4.8, 5, 20, 27],
        [25, 6.8, 2, 4, 22],
        [70, 4.6, 6, 22, 24],
        [40, 5.8, 4, 10, 29],
        [90, 4.2, 7, 30, 19],
        [120, 3.8, 8, 48, 23],
        [110, 4.0, 7, 40, 22],
        [140, 3.6, 9, 60, 20]
    ]

    # Their Current 5k PB times (in minutes)
    # y-axis 
    y_train = [
        35.0, 33.0, 31.0, 29.0, 27.5, 26.0,
        24.5, 23.5, 22.5, 21.5, 20.5, 20.0,
        19.5, 19.0, 18.5, 18.0, 17.5, 17.0,
        16.5, 16.0, 15.0
    ]

    
    print(f"Training the ML model with data from {len(x_train)} runners...")

    #Creating 2 different models that we will be using (Linear Regression + Decision Tree Regressor)
    linear_model = LinearRegression()
    tree_model = DecisionTreeRegressor(max_depth=3)

    # Train both models
    linear_model.fit(x_train,y_train)
    tree_model.fit(x_train,y_train)

    print("Models trained successfully!")

    # Getting user's running stats
    print("\n" + "-"*50)
    print("Enter your running stats")
    print("-"*50)

    # Get weekly volume (km)
    while True:
        try:
            weekly_km = float(input("Weekly km: "))
            break
        except:
            print("Please enter a number")

    # Get Average pace (min/km)
    while True:
        try: 
            avg_pace = float(input("Average pace (min/km): "))
            break
        except:
            print("Please enter a number")

    # Get number of runs per week -> (int)
    while True:
        try:
            runs_per_week = int(input("Runs per week: "))
            break
        except:
            print("Please enter a number")

    # Get months running -> (int)
    while True:
        try:
            months_training = int(input("Months training: "))
            break
        except:
            print("Please enter a number")

    # Get age -> (int)
    while True:
        try:
            age = int(input("Your Age: "))
            break
        except:
            print("Please enter a number")


    # Making a prediction
    your_stats = [[weekly_km, avg_pace, runs_per_week, months_training, age]]

    linear_prediction = linear_model.predict(your_stats)[0]
    tree_prediction = tree_model.predict(your_stats)[0]
    final_prediction = (linear_prediction + tree_prediction) / 2



    MIN_REALISTIC_5K = 12.5   # Just slower than world record
    MAX_REALISTIC_5K = 35.0   # Recreational 
    
    
    if final_prediction < MIN_REALISTIC_5K:     #Quicker than WR Pace
        final_prediction = MIN_REALISTIC_5K

    elif final_prediction > MAX_REALISTIC_5K:   #Slower than Recreational
        final_prediction = MAX_REALISTIC_5K

    # Displaying the results
    print("\n" + "-"*50)
    print("Your 5K PB Prediction")
    print("="*50)
    print("\nBased on your training:")
    print(f"Weekly volume (km): {weekly_km}")
    print(f"Pace (min/km): {avg_pace}")
    print(f"Runs per week: {runs_per_week}")
    print(f"Months training: {months_training}")
    print(f"Age: {age}")

    print("\n" + "-"*50)
    print("Predicted 5k PB:")

    minutes = int(final_prediction)
    seconds = int((final_prediction - minutes) * 60)

    print(f"{minutes}:{seconds:02d} minutes")
    print("-"*50)

def main():
    prediction_5k_pb()
    

if __name__ == "__main__":
    prediction_5k_pb()  








    