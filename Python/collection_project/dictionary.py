trainees = {'fname': "Adam", 'lname': "Steve",'group': "Eng-94",'year': [2020, 2021]}


trainees = dict(fname = "Adam", lname = "Steve", group = "Eng-94", year = [2020, 2021])

print('fname :', trainees['fname'])
print('lname :', trainees['lname'])
print('group :', trainees['group'])
print('year :', trainees['year'])

trainees['fname'] = 'Mark'
print('fname :', trainees['fname'])


print('printing using a loop')
for i in trainees:
    print (i)
print('printing keys using a loop with .keys()')
for i in trainees.keys():
    print(i)
print('printing values using a loop with .valules()')
for i in trainees.values():
    print(i)
print('printing keys and values using a loop with')
for key, value in trainees.items():
    print(key, ' : ', value)

for key in trainees:
    print(key, ' : ', trainees[key])
