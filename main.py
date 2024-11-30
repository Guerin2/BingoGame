from datetime import datetime
import math

def createBingoCard(userID, totalPlayers): #Returns a list
    cardList = []
    freqList= []
    maxNo = math.ceil(10*math.log(totalPlayers)+30) # Creates highest number in the game for bingo card basd on total players. Must change to parameter later

    while len(freqList)<58:
        freqList.append(0)

    for i in range(0,10000000):
        rand = makeRandomNumber((userID+i), maxNo)
        freqList[rand]= freqList[rand]+1

    for i in range(0,58):
        freqList[i] = freqList[i]/100000

    
    while len(cardList) <25: #Adds list while list isnt finished
        rand = makeRandomNumber(userID+len(cardList), maxNo) #Gets a random number to add to the lis
        if ((rand in cardList) == False) and (rand !=0): #Makes sure number isnt already in the list or 0
            cardList.append(rand) #Adds number to the list
    cardList.sort()
    print(freqList)
    return cardList

def getTimeStamp(): #Returns current timestamp
    return datetime.timestamp(datetime.now())

def makeRandomNumber(seed, maxNo):
    finished =False
    while finished == False:
        randNumber = (math.ceil(getTimeStamp() * seed)+1+(seed%2)) % maxNo #Generates random number by mutiplying seed and timestamp while allowing for odd values
        if randNumber != 0:
            return randNumber

print(createBingoCard(7584365934, 15))