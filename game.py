import string
import random

# This function generates random card letters ... 
# Return Value: A String 
def id_generator(size=49, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

# This function prints dashes to make the generic grid
def printDashes(N):
    print('     ', end="")
    for x in range(1,5*N-2):
        print('-', end="")

# This function finds the card no. of a specific cell
def findValue(x,y,List,N):
    counter = 0
    counter = N * (x-1) + (y-1)
    return List[counter]

def setValue(x,y,List,N,value):
    counter = 0
    counter = N * (x-1) + (y-1)
    List[counter] = value

def deleteValue(x,y,List,N):
    counter = 0
    counter = N * (x-1) + (y-1)
    List[counter] = ""

def checkPairInList(List):
    for element in List:
        if List.count(element) > 1 and element != "":
            return True
    return False

# This function prints the board ...
def printBoard(List):
    index = 0

    print("\tColumns")
    print("Rows", end = " ")
    for x in range(1,N+1):
        print('|',x, end = " ")
        if(x == N):
            print('|')

    for x in range(1,N+1):
        if(x == 1):
            printDashes(N)
            print(end="\n")

        print('  ',x, end=" ")
        for y in range(1,N+1):
            print('|',List[index],end=" ")
            index += 1
            if(y == N):
                print('|',end="")
        print(end = "\n")
        printDashes(N)
        print(end = "\n")

# taking total players input..
totalPlayers = int(input("Enter total number of players(minimum 2, maximum 4): "))
while(totalPlayers < 2 or totalPlayers > 4):
    totalPlayers = int(input("Please enter valid number: "))

# declaring a list to store player names..
playersList = []
for i in range(totalPlayers):
    player = input("Enter name of player #" + str(i+1) + " : ")
    playersList.append(player)


# -------------------------------------
Level  = int(input("Enter level No <1 or 2>: "))
while(Level < 1 or Level > 2):
    Level = int(input("Please enter correct level(1 or 2 only): "))

if(Level == 1):
    N = 4
else:
    N = int(input("Enter grid size (2-7 only): "))
    while(N < 2 or N > 7):
        N = int(input("Please enter correct grid size(Range: 2-7): "))

# making a list to store the random characters..
myList = list()
myList = id_generator()

charactersList = list()
index = 0

totalCells = N * N
for i in range(0, totalCells):
    charactersList.append(myList[index])
    index += 1


# printing cheat sheet..
print('\n\n\t\t*** Cheat Sheet ***')
printBoard(myList)

# end of printing cheat sheet..
print("\t\t*** End of Cheat Sheet ***")

print("\n \t\t *** Starting Game ***")

# making an empty list for the game..
gameList = list()
totalCells = N * N
for i in range(0,totalCells):
    if(i == totalCells - 1):
        if(N % 2 != 0):
            gameList.append("Nil")
        else:
            gameList.append(" ")
    else:
        gameList.append(" ")


# making a list to store succesful matched up pairs of each player..
scoreList = []
for i in range(len(playersList)):
    scoreList.append(0)

printBoard(gameList)
index = 0
while(checkPairInList(charactersList) == True):
    print("\n-----------------------------------")
    print("Player's turn: ",playersList[index])
    print("Correct pairs: ",str(scoreList[index]))
    print("-----------------------------------")
    print("Enter 1st card row and col, seperated by space: ",end = "")
    inputArray1 = input().split(" ")
    row1 = int(inputArray1[0])
    col1 = int(inputArray1[1])

    # input validations for indexes..
    while(row1 <= 0 or row1 > N or col1 <= 0 or col1 > N):
        print("Please enter correct indexes again!\nEnter 1st card row and col, seperated by space: ",end = "")
        inputArray1 = input().split(" ")
        row1 = int(inputArray1[0])
        col1 = int(inputArray1[1])


    card1 = findValue(row1,col1, charactersList, N)

    print("Card 1 value is: ", str(card1))

    print("Enter 2nd card row and col, seperated by space: ",end = "")
    inputArray2 = input().split(" ")
    row2 = int(inputArray2[0])
    col2 = int(inputArray2[1])

    # input validations for indexes again..
    while(row2 <= 0 or row2 > N or col2 <= 0 or col2 > N):
        print("Please enter correct indexes again!\nEnter 2nd card row and col, seperated by space: ",end = "")
        inputArray2 = input().split(" ")
        row2 = int(inputArray2[0])
        col2 = int(inputArray2[1])

    inputArray1.clear()
    inputArray2.clear()

    card2 = findValue(row2,col2,charactersList,N)
    print("Card 2 value is: ", str(card2))

    if(card1 == card2):
        print("Hurray!! Both cards are matched!! :D")
        setValue(row1,col1,gameList,N,card1)
        setValue(row2,col2,gameList,N,card2)
        deleteValue(row1,col1,charactersList,N)
        deleteValue(row2,col2,charactersList,N)
        scoreList[index] += 1
    else:
        print("Oh no, the cards are not matched! :(")
        index += 1
        if(index == len(playersList)):
            index = 0
    printBoard(gameList)

print("\n\n \t\t*** Game ended, no more pair matches are left!\n")
maximumValue = max(scoreList)
winnersList = []
for i in range(len(scoreList)):
    if scoreList[i] == maximumValue:
        winnersList.append(i)
# Printing the Player(s) with the maximum correct pairs ...    
print("Winner(s) with ", str(maximumValue), " correct pairs are: ")
for i in range(len(winnersList)):
    print(str(i+1), ". ", playersList[i])