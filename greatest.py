while True:
    num1, num2, num3 = input("Enter three numbers separated by spaces: ").split()

    # Convert input strings to integers
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)

    print("First number is {}, second number is {}, third number is {}".format(num1, num2, num3))

    if num1 > num2 and num1 > num3:
        print(str(num1) + ' is greatest')
    elif num2 > num1 and num2 > num3:
        print(str(num2) + ' is greatest')
    elif num3 > num1 and num3 > num2:
        print(str(num3) + ' is greatest')
    else:
        print('All three are equal')

    choice = input("Do you want to continue (y/n): ")

    if choice != 'y':
        break
