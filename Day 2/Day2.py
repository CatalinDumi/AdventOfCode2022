import os

def get_input_data():
    project_root = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(project_root, 'input_day_2.txt'), 'r') as f:
        list = f.read().split("\n")
    
    return list

""""
Opponent ; Me
A ; X = Rock
B ; Y = Paper
C ; Z = Scissors

A beats Z
B beats X
C beats Y

X beats C
Y beats A
Z beats B

"""

rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
loss = 0

#part_1
scoring = {
    "A X": rock + draw,
    "A Y": paper + win,
    "A Z": scissors + loss,
    "B X": rock + loss,
    "B Y": paper + draw,
    "B Z": scissors + win,
    "C X": rock + win,
    "C Y": paper + loss,
    "C Z": scissors + draw
 }

input_data = get_input_data()
total_score = 0

for x in input_data:
    total_score += scoring[x]

print(total_score)


#part_2
scoring = {
    "A X": scissors + loss,
    "A Y": rock + draw,
    "A Z": paper + win,
    "B X": rock + loss,
    "B Y": paper + draw,
    "B Z": scissors + win,
    "C X": paper + loss,
    "C Y": scissors + draw,
    "C Z": rock + win
 }

input_data = get_input_data()
total_score = 0

for x in input_data:
    total_score += scoring[x]

print(total_score)

