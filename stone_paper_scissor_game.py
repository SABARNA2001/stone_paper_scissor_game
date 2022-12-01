import random
def win(comp,player):
    if comp == player:
        return None    
    elif comp=="s":
        if player=="p":
            return True
        elif player=="sc":
            return False
    elif comp=="p":
        if player=="s":
            return False
        elif player=="sc":
            return True
    elif comp=="sc":
        if player=="p":
            return False
        elif player=="s":
            return True        
#computer er khetre
comp=input("comp turn : press enter:")

rando=random.randint(1, 3)

if rando==1:
    comp="s"
elif rando==2:
    comp ="p"
elif rando==3:
    comp="sc"

player=input("your turn : choose any one stone as = (s),paper as = (p),scissor as = (sc) :")

print(f"Computer chose {comp}")
print(f"You chose {player}")

a=win(comp,player)
if a==None:
    print("this game is a tie try again")
elif a:
    print("hurrah you win!")
else:
    print("you lose!")