
file = open('readme.txt', 'r')

data = file.readline()

while data != '':
    print(data)
    data = file.readline()

file.close()
