nicknames = ["Xilo" , "Nira" , "Faly" , "Zor" , "Kina" , "Jyn" , "Rivo"]
winNick = [8 , 25 , 30 , 60 , 100 , 125 , 150]
loseNick = [0 , 8 , 2 , 3 , 14 , 30 , 10 ]

def rankControl():
    i = 0
    while i < len(nicknames) :
        nick = nicknames[i]
        win = winNick[i]
        lose = loseNick[i]
        classified = ""

        nRank = calculateRank(win , lose)
        classified = classifyRank(nRank)
        print(f"The player {nick} have a {nRank} wins and your level is {classified}!!")
        i += 1

def calculateRank(nWin , nLose):
    sumNivel = nWin - nLose
    return sumNivel

def classifyRank(nivel):
    rank = "" 
    if nivel <= 10:
        rank = "Iron"
    elif nivel > 10 and nivel < 21:
        rank = "Bronze"
    elif nivel > 20 and nivel < 51:
        rank = "Silver"
    elif nivel > 50 and nivel < 81:
        rank = "Gold"
    elif nivel > 80 and nivel < 91:
        rank = "Diamond"
    elif nivel > 90 and nivel < 101:
        rank = "Legendary"
    elif nivel > 100:
        rank = "Imortal"
    return rank

rankControl()