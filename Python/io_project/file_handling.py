
# read file
file = open('readme.txt', 'r')

data1 = file.read(10) # reads only 10 bytes of the file
print (data1)


"""
this will continue with the NEXT 10 bytes
as the cursor has already moved 10 bytes down
"""
data2 = file.read(10)
print (data2)


file.close()
