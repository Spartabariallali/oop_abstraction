from operators import division
from operators import multiplication
from operators import subtraction
from operators import addition
from operators import modo

class Calculator_v2:
    number_one = int(input("please enter your first number: "))
    number_two = int(input("please enter your second number: "))

    operator_choice = int(input(" \n enter 1 for + \n enter 2 for - \n enter 3 for * \n enter 4 for / \n enter 5 for % \n"))

    if operator_choice == 1:
        print(addition(number_one,number_two))
    elif operator_choice == 2:
        print(subtraction(number_one,number_two))
    elif operator_choice == 3:
        print(multiplication(number_one,number_two))
    elif operator_choice == 4:
        print(division(number_one,number_two))
    elif operator_choice == 5:
        print(modo(number_one,number_two)) 
    else:
        print("invalid choice")
      
        

