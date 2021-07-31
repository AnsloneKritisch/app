#file handeling
"""
"r" open file for reading
"w" open file for writing and even creates a file which don't exsisits . When we use this mode then all the data of the file gets deleted and new data are input
"x" creates files if not exsists
"a" add more content to a file
"t" text mode
"p" mode
"+" read and write



f = open ("anshu.txt" , "r")
f1 = f.read(10)
f2 = f.readline(1)
f3 = f.readlins(1)
print(f1)
print(f2)
print(f3)
for i in f :
    print( i , end = "" )
print (f.readline())
f.close()"""