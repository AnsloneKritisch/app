# Create a Dictonary and take input from the user and return the meaning of the Word .
d1 = {"English" : "It is a language" , "english" : "It is a language" ,
      "Elephant" : "It is an name of an animal " ,"elephant" : "It is an name of an animal " ,
      "Bat" : { 1 : "It is an instrument used for playing games " , 2 :"It is a type of animal" } ,
      "bat" : { 1 : "It is an instrument used for playing games" , 2 :"It is a type of animal" } ,
      "Hindi" : "It is a language" ,"hindi" : "It is a language" }
print("The meaning of the given Words are present \n 1.English \n 2.Elephant \n 3.Hindi \n 4.Bat")
x = input("Enter The Name Of The Word You Want To Find")
l = d1[x]
print("The Meaning Of the word IS " , l )