## Wonsuk Lee
## Assignment for 

import random

def weightedDM(rock, paper, scissor):
    total = rock + paper + scissor
    ## Prob is probability
    rockProb = int(float(scissor) / float(total) * 100) ## More Scissor, Throw Rock
    paperProb = int(float(rock) / float(total) * 100) + rockProb ## More Rock, Throw Paper
    
    ## All probs start at 33%. If we play twice, doing paper and rock.
    ## Prob of scissor will be 20%. Difference of paper and rock must be within
    ## 10% for this to trigger. By game theory, Paper is a smarter move to make
    ## since the worst result by game theory can only be a draw here.
    rockStat = float(rock) / total
    paperStat = float(paper) / total
    scissorStat = float(scissor) / total
    
    dice = random.randint(1, 100)
    
    if (abs(float(rockStat) - float(paperStat))) <= .1 and (scissorStat <= .2):
        compThrow = 2
    elif dice <= rockProb:
        compThrow = 1
    elif dice >= rockProb and dice <= paperProb:
        compThrow = 2
    else:
        compThrow = 3
    # print str(rockStat), str(paperStat), str(scissorStat)
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
    print "1 for Rock.\n2 for Paper.\n3 for Scissor.\nAny other key to Quit!"
    
    playerThrow = raw_input("What will you throw out?: ")
    
    if playerThrow == "1":
        playerThrow = int(playerThrow)
        rockCounter += 1
        playCounter += 1
        winCounter += outcome(playerThrow, compThrow)
        print "You have played", playCounter, "times this session."
    elif playerThrow == "2":
        playerThrow = int(playerThrow)
        paperCounter += 1
        playCounter += 1
        winCounter += outcome(playerThrow, compThrow)
        print "You have played", playCounter, "times this session."
    elif playerThrow == "3":
        playerThrow = int(playerThrow)
        scissorCounter += 1
        playCounter += 1
        winCounter += outcome(playerThrow, compThrow)
        print "You have played", playCounter, "times this session."
    else:
        print "You played", playCounter, "times.", "You win", winCounter, "times!"
        print "Invalid input. Did you want to quit?"
        invalidChecker = raw_input("Enter 1 to continue. Anything else to quit: ")
        if invalidChecker == "1":
            print "Restarting Game!"
        else:
            break
