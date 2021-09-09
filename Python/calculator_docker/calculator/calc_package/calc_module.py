
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
