import os

def get_input_data():
    project_root = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(project_root, 'input_day_1.txt'), 'r') as f:
        list = f.readlines()
    
    return list

input_data = get_input_data()
initial_calories = 0
calories = []
    
for x in input_data:
        if x != '\n':
            initial_calories += int(x)
        else:
            calories.append(initial_calories)
            initial_calories = 0

calories = sorted(calories)


print((calories[-1])) 
print(calories[-1]+calories[-2]+calories[-3])
