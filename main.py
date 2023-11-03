import random as Rand
"""
simple PassGen

Created by Kevin Wahome, 
Computer Science Student
University of Massachusetts - Lowell

Task
    - Allow for password generation containing number of num, upper, lower, special char
"""

def numberGen(password): # a helper function to return a number
    numberCase = "0123456789"
    index = Rand.randint(0, 9)
    password.append(numberCase[index])
    return password

def upperCaseGen(password): # a helper function to return a upperCase letter
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = Rand.randint(0, 25)
    password.append(upperCase[index])
    return password

def lowerCaseGen(password): # a helper function to return a uppercase letter
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    index = Rand.randint(0, 25)
    password.append(lowerCase[index])
    return password

def specialCaseGen(password): # a helper function to return a specialCaseGen
    specialCase = "!@#$%^&*"
    index = Rand.randint(0, 7)
    password.append(specialCase[index])
    return password

def preDefined(password):
    i = 16 # preDefined password length iterator | only works with even numbers, does not handle odd numberCase well
    while i > 0:
        numberGen(password)
        upperCaseGen(password)
        lowerCaseGen(password)
        specialCaseGen(password)
        i-=4 # iterates by 4 to account for the 4 insert

def driver(): # the brains of our program
    password = [] # our initial password generator
    print("Hello user, would you like a generated password? choose (y/n) ")
    choice = (input())
    if choice.lower() == 'y': # handles our upper case in one step
       preDefined(password)
       unindexedPassword = "".join(password) # joins our comma seperated list into one string
       print('\n' + "Password: " + unindexedPassword)
       print("Would you like to generate another one? (y/n)")
       choice = (input())
       if choice.lower() == 'y': # handles our upper case in one step
           driver()
       else:
        return 0
    else:
        print("Come back again when your ready to generate a password :)")
        return 0


driver()

