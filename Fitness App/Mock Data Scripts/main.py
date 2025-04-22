from generate_user_data import generate_user_data, output_path as user_otput_path
from generate_fitness_data import generate_fitness_data, output_path as fitn_output_path

users = generate_user_data(num_users=20)
fitness_data = generate_fitness_data(users=users)

users.to_csv(user_otput_path, index=False)
fitness_data.to_csv(fitn_output_path, index=False)

