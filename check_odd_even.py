while(True):
    num=int(input("Enter a number to check: "))

    if(num%2==0):
        print("number is even")
    else:
        print("number in odd")
    choice=input("Do you want to continue(y/n):")
    if (choice=='n'):
        break
    elif(choice=='y'):
        continue
    else:
        break