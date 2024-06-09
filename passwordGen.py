#Task3
#TechnoHack Edutech
#PasswordGenerator
#Made by Simal Agrahari

import string
import random
if __name__=="__main__":
    s1 = string.ascii_lowercase
    #print(s1)
    s2 = string.ascii_uppercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4)
   
    lgth = int(input("Enter the password length: ")) 
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)
    random.shuffle(s) #shuffling the list
    #print(s)
    print("Your password is: ")
    print("".join(s[0:lgth]))
