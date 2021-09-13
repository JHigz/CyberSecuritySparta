import calculator
import sqlite3
from contextlib import closing

def create_table():
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("CREATE TABLE operations_table (id INTEGER PRIMARY KEY, fnum INTEGER, snum INTEGER, sum INTEGER, sub INTEGER);")
            connection.commit()
def insert():
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(f"INSERT INTO operations_table (fnum, snum, sum, sub) VALUES ('{number1}', '{number2}', '{sum}', '{sub}');")
            connection.commit()

def show():
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * from operations_table;")
            records = cursor.fetchall()
            print(records)

create_table()

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

    insert()

show()
