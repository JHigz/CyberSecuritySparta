import calculator

for index in range (0, 3):
    number1 = int(input("please enter your first number :"))
    number2 = int(input("Please enter your second number :"))

    CalculatorObject = calculator.CalculatorClass (number1, number2)

    sum = CalculatorObject.add ()
    print (sum)
    print (f"Total Operations : {CalculatorObject.op_count}")


    sub = CalculatorObject.sub ()
    print (sub)
    print (f"Total Operations : {CalculatorObject.op_count}")
