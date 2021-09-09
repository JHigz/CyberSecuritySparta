
# append to file
file = open('readme3.txt', 'a+')

data = file.writelines('This is a new line 07') #writes data on a new line
data = file.read()
print(data)

file.close()
