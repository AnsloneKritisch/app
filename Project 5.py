"""
# Find Your Star Appolostic Star Program
a = int(input("Enter a number "))
if a % 2 == 0 or a == 0 :
    print(" True \n You are positive side of Boolen Algebra \n  You choose " , a , " an Even number ")
    for i in range (1,a+1):
        for j in  range (1,i+1):
            print("*",end=" ")
        print()
else:
    print(" False \n You are negative side of Boolen Algebra \n  You choose " , a , " an odd number ")
    for i in range ( a , 0 , -1):
        for j in range (1 , i+1):
            print("*",end="")
        print()
"""