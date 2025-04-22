import pandas as pd
import random
from faker import Faker
from pathlib import Path

output_path = Path(__file__).resolve().parent.parent / "Mock Data" / "dimUser.csv"

fake = Faker()
Faker.seed(0)
random.seed(0)

random_male_image_urls = [
    "https://avatar.iran.liara.run/public/40",
    "https://avatar.iran.liara.run/public/45",
    "https://avatar.iran.liara.run/public/1",
    "https://avatar.iran.liara.run/public/20",
    "https://avatar.iran.liara.run/public/27",
    "https://avatar.iran.liara.run/public/37",
    "https://avatar.iran.liara.run/public/22",
    "https://avatar.iran.liara.run/public/19",
    "https://avatar.iran.liara.run/public/42",
    "https://avatar.iran.liara.run/public/23",
    "https://avatar.iran.liara.run/public/36"
]
random_female_image_urls = [
    "https://avatar.iran.liara.run/public/64",
    "https://avatar.iran.liara.run/public/59",
    "https://avatar.iran.liara.run/public/71",
    "https://avatar.iran.liara.run/public/100",
    "https://avatar.iran.liara.run/public/72",
    "https://avatar.iran.liara.run/public/81",
    "https://avatar.iran.liara.run/public/53",
    "https://avatar.iran.liara.run/public/68",
    "https://avatar.iran.liara.run/public/77",
    "https://avatar.iran.liara.run/public/91",
    "https://avatar.iran.liara.run/public/58"
]

def generate_user_data(num_users=20):
    data = []
    for user_id in range(1, num_users + 1):
        gender = random.choice(['Male', 'Female'])
        first_name = fake.first_name_male() if gender == "Male" else fake.first_name_female()
        last_name = fake.last_name()
        
        name = f"{first_name} {last_name}"
        
        calories_min = random.randint(1500, 2000)
        calories_max = random.randint(2001, 3000)

        steps_min = random.randint(3000, 6000)
        steps_max = random.randint(6001, 12000)

        hr_min = random.randint(60, 70)
        hr_max = random.randint(100, 130)

        sessions_min = random.randint(4, 8)
        sessions_max = random.randint(9, 20)

        image_list = random_male_image_urls if gender == "Male" else random_female_image_urls
        photo_img = image_list[user_id % len(image_list)]

        data.append({
            "User ID": user_id,
            "First Name": first_name,
            "Last Name": last_name,
            "Name": name,
            "Gender": gender,
            "Calories Target Min": calories_min,
            "Calories Target Max": calories_max,
            "Steps Target Min": steps_min,
            "Steps Target Max": steps_max,
            "Heart Rate Target Min": hr_min,
            "Heart Rate Target Max": hr_max,
            "Exercise Sessions (monthly) Target Min": sessions_min,
            "Exercise Sessions (monthly) Target Max": sessions_max,
            "Photo Img": photo_img
        })

    df = pd.DataFrame(data)
    return df