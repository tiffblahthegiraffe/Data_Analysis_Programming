##Wonsuk Lee

import random

def weightedDM(rock, paper, scissor):
    total = rock + paper + scissor
    rockProb = int(float(scissor) / float(total) * 100) ## More Scissor, Throw Rock
    paperProb = int(float(rock) / float(total) * 100) + rockProb ## More Rock, Throw Paper
    
    dice = random.randint(1, 100)
    if dice <= rockProb:
        compThrow = 1
    elif dice >= rockProb and dice <= paperProb:
        compThrow = 2
    else:
        compThrow = 3

    return compThrow

def outcome(playerThrow, compThrow):
    print ""
    if playerThrow == 1:
        print "Player threw ROCK!"
        playerValue = 3
    elif playerThrow == 2:
        print "Player threw PAPER!"
        playerValue = 1
    else:
        print "Player threw SCISSORS!"
        playerValue = 2
        
    if compThrow == 1:
        print "Computer threw ROCK!"
        compValue = 3
    elif compThrow == 2:
        print "Computer threw PAPER!"
        compValue = 1
    else:
        print "Computer threw SCISSOR!"
        compValue = 2
        
    print ""
        
    if playerValue == 1 and compValue == 3:
        compValue = compValue - 3
    elif playerValue == 3 and compValue == 1:
        playerValue = playerValue - 3
        
    if playerValue == compValue:
        print "Draw!"
        return 0
    elif playerValue > compValue:
        print "Player Wins!"
        return 1
    elif playerValue < compValue:
        print "Player Loses!"
        return 0
            

winCounter = 0
playCounter = 0

rockCounter = 1
paperCounter = 1
scissorCounter = 1

rock = 1
paper = 2
scissor = 3

while True:
    compThrow = weightedDM(rockCounter, paperCounter, scissorCounter)
    
    print ""
    print "Time to play Rock, Paper, Scissors!"
    print "1 for Rock.\n2 for Paper.\n3 for Scissor.\n4 to quit!"
    
    playerThrow = int(raw_input("What will you throw out? "))
    
    if playerThrow == 1:
        rockCounter += 1
        playCounter += 1
        winCounter += outcome(playerThrow, compThrow)
        print "You have played", playCounter, "times this session."
    elif playerThrow == 2:
        paperCounter += 1
        playCounter += 1
        winCounter += outcome(playerThrow, compThrow)
        print "You have played", playCounter, "times this session."
    elif playerThrow == 3:
        scissorCounter += 1
        playCounter += 1
        winCounter += outcome(playerThrow, compThrow)
        print "You have played", playCounter, "times this session."
    else:
        print "You played", playCounter, "times.", "You win", winCounter, "times!"
        break

