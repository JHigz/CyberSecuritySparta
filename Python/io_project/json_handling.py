import json

trainees = {'fname': "Adam", 'lname': "Smith",'group': "Eng-94",'year': [2020, 2021]}

print(trainees)

with open('trainees.json', 'w') as file:
    json.dump(trainees,file, indent = 4)
