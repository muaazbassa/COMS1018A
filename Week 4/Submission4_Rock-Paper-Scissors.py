# Mu'aaz Bassa
# Submission 4: Rock-Paper-Scissors

sPlayer1 = str(input())
sPlayer2 = str(input())
iPlayer1=0
iPlayer2=0
if sPlayer1 == 'rock':
    iPlayer1 = 0
elif sPlayer1 == 'paper':
    iPlayer1 = 1
elif sPlayer1 == 'scissors':
    iPlayer1 = 2

if sPlayer2 == 'rock':
    iPlayer2 = 0
elif sPlayer2 == 'paper':
    iPlayer2 = 1
elif sPlayer2 == 'scissors':
    iPlayer2 = 2

if iPlayer1 == 0 and iPlayer2 == 2:
    print("Player 1 wins")
elif iPlayer1 == 1 and iPlayer2 == 0:
    print("Player 1 wins")
elif iPlayer1 == 2 and iPlayer2 == 1:
    print("Player 1 wins")
elif iPlayer1==iPlayer2:
    print("Tie")
else: 
    print("Player 2 wins")
