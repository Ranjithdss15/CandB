#imports
import random

#Public Variables
Bullstr = "The count of Bull is {}"
Cowstr = "The count of Cow is {}"

#Generate a random number
randomnum = random.randrange(1000,9999)
randomnumtest = 5937

#Get a value from user
#uservalue = input("Enter the number")

#convert the int into a list

def convert(num):
    numstr = str(num)
    num1 = list(numstr)
    return(num1)

#Covert a random number into a list

randomList = convert(randomnum)
print(randomList)

#Convert the user number into a list

#UservalueList = convert(uservalue)
#print(UservalueList)


#Matching Function
def search(uservalue,randomList,Bullstr,Cowstr):
    global Bull
    Bull = 0
    global Cow
    Cow = 0
    for u1 in uservalue:
        for r1 in randomList:
            if u1 == r1:
                #print(u1)
                if uservalue.index(u1) == randomList.index(r1):
                    Bull = Bull+1
                else:
                    Cow = Cow + 1
    print(Bullstr.format(Bull))
    print(Cowstr.format(Cow))
    if (Bull == 4):
        return Bull



#CALLING METHODS HERE

def gamefunc(uservalue,randomList,Bullstr,Cowstr):
    while True:
        if (search(uservalue,randomList,Bullstr,Cowstr) == 4):
            print("Hurray!!! You found it..")
            break
        else:
            uservalue = input("Try another number")

def gameMenu():
    print("Welcome to the game")
    print("Cows and Bulls")
    opt = input("To start the game enter Y or to exit enter N")

    if(opt=="Y" or "y"):
        uservalue = input("Enter the number")
        UservalueList = convert(uservalue)
        gamefunc(uservalue,randomList,Bullstr,Cowstr)


gameMenu()

















