
def Addition(x,y):
    return x + y

def Subtraction(x,y):
    return x - y

def Multiplication(x,y):
    return x * y

def Division(x,y):
    try:
        total = x / y
    except ZeroDivisionError:
        print('You cannot complete this task as you have tried to divide by 0')
        return None
    return total

f = open('Results.txt', 'w+')
for i in range (0, 5):
    First_Num = int(input ("Enter your first number : "))
    Second_Num = int(input ("Enter your second number: "))

    add_value = Addition(First_Num,Second_Num)
    print(First_Num, ' + ', Second_Num, '= ', add_value)
    f.write(str(add_value, /n))

    sub_value = Subtraction(First_Num,Second_Num)
    print(First_Num, ' - ', Second_Num, '= ', sub_value)

    mult_value = Multiplication(First_Num,Second_Num)
    print(First_Num, ' * ', Second_Num, '= ', mult_value)

    div_value = Division(First_Num,Second_Num)
    print(First_Num, ' / ', Second_Num, '= ', div_value)
