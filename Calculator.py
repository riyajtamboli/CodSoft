while True:
    print("*************************************************************")
    print("Calculator")

    print("Choices are::")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulo")

    choice=int(input("Enter your choice::"))

    print("*************************************************************")

    if (choice == 1):
        number1 = int(input("Enter First Number::"))
        number2 = int(input("Enter second Number::"))
        print("Addition is::", number1 + number2)

    elif (choice == 2):
        number1 = int(input("Enter First Number::"))
        number2 = int(input("Enter second Number::"))
        print("Subtraction is::", number1 - number2)

    elif (choice == 3):
        number1 = int(input("Enter First Number::"))
        number2 = int(input("Enter second Number::"))
        print("Multiplication is::", number1 * number2)

    elif (choice == 4):
        number1 = int(input("Enter First Number::"))
        number2 = int(input("Enter second Number::"))
        print("Division is::", number1 / number2)

    elif (choice == 5):
        number1 = int(input("Enter First Number::"))
        number2 = int(input("Enter second Number::"))
        print("Remainder is::", number1 % number2)

    else:
        print("Enter Valid choice")

    ch  =input("Do you want to Continue?(y/n)")
    if (ch == 'n'):
        print("Exiting")
        break
    elif (ch == 'y'):
        continue
    elif (ch != 'y'):
        print("Invalid Choice")
        break