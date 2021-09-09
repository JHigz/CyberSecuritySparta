import json

with open('trainees.json', 'r') as file:
    trainees = json.load(file)

print(trainees)

for key, value in trainees.items():
    print(f"{key} = {value}")

    trainees['year'] = [2020, 2021, 2020]

with open('trainees.json', 'w') as file:
    json.dump (trainees, file, indent = 4)
