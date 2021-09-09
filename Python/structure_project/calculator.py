from calc_package import calc_module
import json

f = open('results.txt', 'a+' )


data_list = []
for i in range (0, 3):
    First_Num = int(input ("Enter your first number : "))
    Second_Num = int(input ("Enter your second number: "))

    add_value = calc_module.Addition(First_Num,Second_Num)
    print(First_Num, ' + ', Second_Num, '= ', add_value)

    sub_value = calc_module.Subtraction(First_Num,Second_Num)
    print(First_Num, ' - ', Second_Num, '= ', sub_value)

    mult_value = calc_module.Multiplication(First_Num,Second_Num)
    print(First_Num, ' * ', Second_Num, '= ', mult_value)

    div_value = calc_module.Division(First_Num,Second_Num)
    print(First_Num, ' / ', Second_Num, '= ', div_value)

    f.write('---------------------------')
    f.write('\n')
    f.write(str(add_value))
    f.write('\n')
    f.write(str(sub_value))
    f.write('\n')
    f.write(str(mult_value))
    f.write('\n')
    f.write(str(div_value))
    f.write('\n')

    data_dict = {'Addition':add_value, 'Subtraction':sub_value, 'Multiplication':mult_value, 'Division':div_value}


    with open('calculator.json', 'a+') as file:
        json.dump(data_dict,file, indent = 4)
f.close()
