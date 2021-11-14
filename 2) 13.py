sub1=int(input("Enter marks of the physics: "))
sub2=int(input("Enter marks of the chemistry: "))
sub3=int(input("Enter marks of the biology: "))
sub4=int(input("Enter marks of the maths: "))
sub5=int(input("Enter marks of the computer: "))
perc=(sub1+sub2+sub3+sub4+sub4)/5*100
if(perc>=90):
    print("Grade: A")
elif(perc>=80%):
    print("Grade: B")
elif(perc>=70%):
    print("Grade: C")
elif(perc>=60%):
    print("Grade: D")
elif(perc>=40%):
    print("Grade: E")
else:
    print("Grade: F")
