import json

with open('trainees.json', 'r') as file:
    trainees = json.load(file)

print(trainees)

for key, value in trainees.items():
    print(f"{key} = {value}")
