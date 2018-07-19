import random
hands = ["Rock","Paper","Scissors"]

#This is the function showing the win lose between three hands
def win_or_lose(h,c):
    points = 0
    if h == hands[0]:
        if c == hands[0]:
            points = 0
        elif c == hands[1]:
            points = 0
        elif c == hands[2]:
            points = 1
    if h == hands[1]:
        if c == hands[0]:
            points = 1
        elif c == hands[1]:
            points = 0
        elif c == hands[2]:
            points = 0
    if h == hands[2]:
        if c == hands[0]:
            points = 0
        elif c == hands[1]:
            points = 1
        elif c == hands[2]:
            points = 0
    return points

#This function is used to predict what human will play by the most frequent hands he plays         
def com_brain(h):
    human_brain = max(h, key = h.count)
    if human_brain == hands[0]:
        return hands[1]
    elif human_brain == hands[1]:
        return hands[2]
    elif human_brain == hands[2]:
        return hands[0]
#h=["Rock","Paper","Scissors","Rock","Paper","Scissors","Scissors","Scissors","Scissors","Paper","Paper","Paper"]
#print com_brain(h)
#print type(com_brain(h))   

def game():
    
    human_decision = []
    computer_decision = []
    game_played = 0
    human_win = 0
    
    while True:
    
        print "1. Rock\n2. Paper\n3. Scissors\n4.Quit"
        human = input("It's your turn to choose: ")
        
        if human_decision == []:
            computer = random.choice(hands)
        else:
            computer = com_brain(human_decision)
    
        if human == 1:
            human_decision.append(hands[0])
            computer_decision.append(computer)
            human_win = human_win + win_or_lose(hands[0],computer)
            game_played += 1
            
        elif human == 2:
            human_decision.append(hands[1])
            computer_decision.append(computer)
            human_win = human_win + win_or_lose(hands[1],computer)
            game_played += 1
            
        elif human == 3:
            human_decision.append(hands[2])
            computer_decision.append(computer)
            human_win = human_win + win_or_lose(hands[2],computer)
            game_played += 1
            
        elif human == 4:
            print "You are out of the game!"
            break
        else:
            print "Please re-enter your choice: " 
            continue 
    
    print "human:" , human_decision
    print "computer:" , computer_decision
    print "human has won:", human_win
    print "total game played:", game_played   
          
    
game()

