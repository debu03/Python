while(True):
    num=int(input("Enter a number to check: "))

    if(num==0):
        print("You have entered a zero number")
    elif(num<0):
        print("You have entered a negative number")
    else:
        print("You have entered a positive number")
    choice=input("Do you want to continue(y/n):")
    if (choice=='n'):
        break
    elif(choice=='y'):
        continue
    else:
        break