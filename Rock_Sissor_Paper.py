import random
l=['rock','paper','scissor']
while True :
    ccount=0
    ucount=0  
    uc=int(input('''
    Game Start:
    1 Yes
    2 No | Exit
    
    '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
            1 Rock
            2 Paper
            3 Scissor
            '''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="paper"
            elif userinput==3:
                uchoice="scissor"
            cchoice=random.choice(l)
            if cchoice==uchoice:
                print("computer Value",cchoice)
                print("User Value",uchoice)
                print("Game draw")
            elif (uchoice=="rock" and cchoice=="scissor") or (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="paper"):
                print("computer Value",cchoice)
                print("User Value",uchoice)
                print("You Score")
                ucount=ucount+1
            elif (uchoice=="rock" and cchoice=="paper") or (uchoice=="paper" and cchoice=="scissor") or (uchoice=="scissor" and cchoice=="rock"):
                print("computer Value",cchoice)
                print("User Value",uchoice)
                print("Computer Score")
                ccount=ccount+1
        if ucount==ccount:
            print("Final Game Draw")
            print("User Score",ucount)
            print("Computer Score",ccount)
        elif ucount>ccount:
            print("You Win")
            print("User Score",ucount)
            print("Computer Score",ccount)
        elif ucount<ccount:
            print("You loose")
            print("User Score",ucount)
            print("Computer Score",ccount)           
    else:
        break;