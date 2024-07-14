import random

def game(Machine, you):

    if Machine == you:
        return None
    
    elif Machine == "S":
        if you == "W":
            return False
        elif you == "G":
            return True
        
    elif Machine == "W":
        if you == "G":
            return False
        elif you == "S":
            return True
        
    elif Machine == "G":
        if you  == "S":
            return False
        elif you == "W":
            return False
        

print("Machine Turn : Snake(S), Water(W), Gun(G)? ")        
rando = random.randint(1,3)
if rando == 1:
    Machine = "S"
elif rando == 2 :
    Machine = "W"
elif rando == 3:
    Machine = "G"

you = input("Yours Turn : Snake(S), Water(W), Gun(G)? ")
a = game(Machine,you)

print(f"Machine Choose: {Machine} ")
print(f"You Choose: {you} ")

if a == None:
    print("The game is tie!")
elif a:
    print("you Win")
else:
    print("You Loose!")
    