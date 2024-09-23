import random
import os 
players = []
playername = []
pl = int(input("Enter Total No of players: "))
for i in range(1,pl+1,1):
    print("\nEnter the name ",i," of Player: ")
    en = input("Enter Here: ")
    playername.append(en)
    players.append(0)

print("\n\nLocation of Snakes:")
print("1. 33 to 5")
print("2. 43 to 24")
print("3. 56 to 20")
print("4. 66 to 12")
print("5. 78 to 59")
print("6. 96 to 72")
print("7. 98 to 4")

print("\nLocation of Ladders:")
print("1. 7 to 36")
print("2. 21 to 58")
print("3. 31 to 51")
print("4. 34 to 84")
print("5. 54 to 89")
print("6. 63 to 82")
print("7. 69 to 91")

pos = 0
con =1
while con == 1:
    os.system('cls')
    print("\n\nPosition are: ")
    for i in range(0,pl,1):
        print(playername[i],": ",players[i])
    
    if pos == pl:
        pos = 0
    
    
    for pos in range(0,pl,1):
    
        print("Player ",pos+1," Press Enter to roll the dice: ")
        a = input("")
        die = random.randint(1,6)
        print("Dice value: ",die)
        if players[pos]<100:
            players[pos]+= die
        if players[pos]>100:
            players[pos]-=die

        if players[pos]==33:
            print("oh no!! you have been bitten by Snake!!")
            print("You have been sent to tile 5")
            players[pos]=5
        elif players[pos]==43:
            print("sheesh You have been bitten by sanke!!")
            print("You been sent to tile 24")
            players[pos]=24
        elif players[pos]==56:
            print("oh no!! you have been bitten by Snake!!")
            print("You have been sent to tile 20")
            players[pos]=20
        elif players[pos]==66:
            print("sheesh You have been bitten by sanke!!")
            print("You been sent to tile 12")
            players[pos]=12
        elif players[pos]== 78:
            print("oh no!! you have been bitten by Snake!!")
            print("You have been sent to tile 59")
            players[pos]=59
        elif players[pos]==96:
            print("sheesh You have been bitten by sanke!!")
            print("You been sent to tile 72")
            players[pos]=72
        elif players[pos]==98:
            print("oh no!! you have been bitten by Snake!!")
            print("You have been sent to tile 4")
            players[pos]=4

        elif players[pos]==7:
            print("YAY!! You found a Ladder!!")
            print("Promoted to 36")
            players[pos]=36
        elif players[pos]==21:
            print("YAY!! You found a Ladder!!")
            print("Promoted to 58")
            players[pos]=58
        elif players[pos]==31:
            print("YAY!! You found a Ladder!!")
            print("Promoted to 51")
            
            players[pos]=51

        elif players[pos]==34:
            print("YAY!! You found a Ladder!!")
            print("Promoted to 84")
            players[pos]=84
        elif players[pos]==54:
            print("YAY!! You found a Ladder!!")
            print("Promoted to 89")
            players[pos]=89
        elif players[pos]==63:
            print("YAY!! You found a Ladder!!")
            print("Promoted to 82")
            players[pos]=82
        elif players[pos]==69:
            print("YAY!! You found a Ladder!!")
            print("Promoted to 91")
            players[pos]=91
        if players[pos]==100:
            print("YAY YAY YAY ",playername[pos]," has WON the Game!!")
            con =0 
        else:
            continue 

print("Game Ended")   
    
    
    
    
    