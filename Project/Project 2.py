"""#Faulty Calculator
# 45 * 3 = 555 , 56+9 = 77, 56/6 = 4
x = int(input("Enter a Number"))
y = int(input("Enter a Number"))
print(" Press \n 1.For Division \n 2.For Muntiplication \n 3.For Addition ")
z = int(input("Enter Your Choice"))
if z == 1 :
    print("You Choose Division")
    if x == 56 or x== 6 and y == 56 or y == 6 :
        print("The Divison of " , x , " and " , y , "is = 4 ")
    else:
        print("The  Divison of " , x , " and " , y , "is = " , x/y )
elif z == 2 :
    print("You Choose Muntiplication ")
    if x == 45 or x== 3 and y == 45 or y == 3 :
        print("The Muntiplication of " , x , " and " , y , "is = 555 ")
    else:
        print("The Muntiplication of " , x , " and " , y , "is = " , x*y )
elif z == 3 :
    print("You Choose Addition")
    if x == 56 or x== 9 and y == 56 or y == 9 :
        print("The Addition  of " , x , " and " , y , "is = 77 ")
    else:
        print(("The Addition  of " , x , " and " , y , "is = " , x+y ))
else:
    print(" Wrong Instruction ")
"""