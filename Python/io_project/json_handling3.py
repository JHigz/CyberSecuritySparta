import json

trainees = {'fname': "Adam", 'lname': "Smith",'group': "Eng-94",'year': [2020, 2021]}

print("This is the dictionary format")
print(trainees)

print('This is the JSON format')
trainees_json_object = json.dumps(trainees)
print(trainees_json_object)
