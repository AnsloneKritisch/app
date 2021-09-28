"""





def getdate():
    import datetime
    a =  datetime.datetime.now()
    print(a)

print("The Two Candidte here are - Harry and Anshu \n Press 1 for Harry \n Press 2 for Anshu ")
a = int(input("Enter The Name of your Patint"))
print("Press 1 for Exercise \n Press 2 for Diet \n Press 3 for Medicine used by him")
b = int(input("Enter What you Want to Know about Him"))

if a == 1 :
    f = open ("Harry.txt" , "r")
    if b == 1 :
        getdate()
        f2 = f.readline()
        print(f2)
    elif b == 2:
        getdate()
        f2 = f.readline()
        f3 = f.readline()
        print(f3)
    elif b == 3 :
        getdate()
        f2 = f.readline()
        f3 = f.readline()
        f4 = f.readline()
        print(f4)
    else :
        print(" Wrong Choice ")
elif a == 2 :
    f = open("anshu.txt")
    if b == 1 :
        getdate()
        f2 = f.readline()
        print(f2)
    elif b == 2:
        getdate()
        f2 = f.readline()
        f3 = f.readline()
        print(f3)
    elif b == 3:
        getdate()
        f2 = f.readline()
        f3 = f.readline()
        f4 = f.readline()
        print(f4)
    else:
        print(" Wrong Choice ")
else:
    print("You Typed a wrong number")



















"""