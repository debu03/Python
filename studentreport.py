print("      Student Report Card System")
print("-------------Input Section--------------")
total=0
name=input("Name: ")
school=input("School Name: ")
n=int(input("Enter number of subjects: "))
for i in range(n):
    subject=input("Enter subject: ")
    marks=int(input(f'Enter {subject} marks: '))
    if  marks>=90:
        print(f'{subject}={marks}/100-Grade S')
    elif marks>=80:
        print(f'{subject}={marks}/100-Grade A')
    elif marks>=70:
        print(f'{subject}={marks}/100-Grade B')
    elif marks>=60:
        print(f'{subject}={marks}/100-Grade C')
    elif marks>=50:
        print(f'{subject}={marks}/100-Grade D')
    elif marks>=40:
        print(f'{subject}={marks}/100-Grade E')
    else:
        print(f'{subject}={marks}/100-Grade F')
    total=total+marks

print("--------------Output Section---------------")
print("School:"+school)
print("Student Name----"+name)
print("\n")
print(f'Total={total}')
print(f'Percentage={total/(n)}%')
grade=int(total/n)
if  grade>=90:
    print(f'Overall Grade S')
elif grade>=80:
    print(f'Overall Grade A')
elif grade>=70:
    print(f'Overall Grade B')
elif grade>=60:
    print(f'Overall Grade C')
elif grade>=50:
    print(f'Overall Grade D')
elif grade>=40:
    print(f'Overall Grade E')
else:
    print(f'Overall Grade F')
