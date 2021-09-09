
# create a file
try:
    file = open('readme3.txt', 'x')
except FileExistsError as file_exists_error:
    print(file_exists_error)
except Exception as exception_msg:
    print(exception_msg)
finally:
    file.close()

#data = file.write('This is a new line 07\n')
#data = file.read()
#print(data)

#file.close()
