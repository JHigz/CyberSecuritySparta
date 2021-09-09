def welcome (id):
    print('Welcome to cyber course')
    print('This is the beginning of the course, Week :', id)
    return True

for i in range(0, 10):
    return_value = welcome(i)
    print(return_value)
