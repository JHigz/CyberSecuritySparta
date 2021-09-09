import json

with open('calculator.json') as file:
    data = json.load(file)

print(data)
