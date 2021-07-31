"""f = open("anshu.txt" , "w") # When we use write mode than the old content files are deleted
f.write("Anshu is a prime .") # write function is mainly use to add text to a file
f.close()
"""
"""f = open("anshu.txt" , "a")# append function is mainly use to  add data and no old data is removed ....
# f.write("Anshu is going to be leader of autobots ")
#f.write("\n Anshu is going to be leader of autobots \n")
a = f.write(" \n Anshu is going to be leader of autobots \n  ")
print(a) # This command is mainly used to know the no of characters are added to the file .
f.close()"""
"""f = open("anshu.txt" , "r+") # r+ mode is mixture of read and write mode , the main thing we can add sentences without deleting the old document and here the write function work same as it worked in append mode ....
f1 = f.read()
print(f1)
f2 = f.write(" The world is very big but below my feet ")
print("The no  of characters you added in you file is = " , f2 )
f3 = f.read()
print(" The new lines added are : \n " )
print(f3)
f.close()"""