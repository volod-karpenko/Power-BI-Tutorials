from faker import Faker
import random
import pandas as pd
from pathlib import Path
import numpy as np

output_path = Path(__file__).resolve().parent.parent / "Mock Data" / "fctFitnessStats.csv"

fake = Faker()

def generate_fitness_data(users):    
    data = []
    activty_dates = pd.date_range(start = "2022-01-01", end = "2025-06-30", freq = "1D")
    dates_sample_size = 950

    for index, user in users.iterrows():
        user_id = user["User ID"]
        user_dates = np.random.choice(activty_dates, size = dates_sample_size, replace = False)
        user_min_steps = user["Steps Target Min"] - 1500
        user_max_steps = user["Steps Target Max"] - 250
        user_min_heart_rate = user["Heart Rate Target Min"] - 10
        user_max_heart_rate = user["Heart Rate Target Max"] - 10
        user_min_calories = user["Calories Target Min"] - 500
        user_max_calories = user["Calories Target Max"] - 250
        
        for date in user_dates:
            # Generate realistic fitness data with some randomness
            steps = random.randint(user_min_steps, user_max_steps)
            heart_rate = random.randint(user_min_heart_rate, user_max_heart_rate)
            calories = random.randint(user_min_calories, user_max_calories)
            
            
            # Number of exercise sessions (0-3, with 0 being most common)
            exercise_session = 0
            if random.random() < 0.3:  # 30% chance of having at least one session
                exercise_session = random.randint(1, 3)
                
            # Exercise time correlates with number of sessions
            exercise_time = exercise_session * random.randint(15, 60)
            
            data.append({
                "UserID": user_id,
                "Date": date,
                "Steps": steps,
                "Heart Rate": heart_rate,
                "Exercise Session": exercise_session,
                "Exercise Time (in Min)": exercise_time,
                "Calories": calories
            })
    
    df = pd.DataFrame(data)
    return df