trainees = ("Adam", "Steve", "Eng-94", 2021)

print(trainees)
print(trainees[0])
print(trainees[3])
print("-------------------------")
for i in trainees:
    print(i)

i = 0


print("\nThis is the tuple using while:\n ")
while i < len(trainees):
    print(trainees[i])
    i += 1


Print("\n This is to extract the values"\n)
fname = trainees[0]
sname = trainees[1]
group = trainees[2]
year = trainees[3]

print("fname :", fname)
print("lname :", lname)
print("group :", group)
print("year :", year)



Print("\n This is to extract the values"\n)
fname, lname, group, year = trainees
