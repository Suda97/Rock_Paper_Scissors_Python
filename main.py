def game():
    p1 = input("Player One! Type rock/paper/scissors: ")
    p2 = input("Player Two! Type rock/paper/scissors: ")
    if p1 == p2:
        print("Tie")
    elif p1 == 'rock':
        if p2 == 'scissors':
            print("Player One WINS!")
        else:
            print("Player Two WINS!")
    elif p1 == 'paper':
        if p2 == 'rock':
            print("Player One WINS!")
        else:
            print("Player Two WINS!")
    elif p1 == 'scissors':
        if p2 == 'paper':
            print("Player One WINS!")
        else:
            print("Player Two WINS!")
    elif (p1 != 'scissors' and p1 != 'paper' and p1 != 'rock') or \
            (p2 != 'scissors' and p2 != 'paper' and p2 != 'rock'):
        print("Bad input!")


# Game of rock, paper, scissors
while True:
    game()
    uCom = input("If You want to quit type 'quit': ")
    if uCom == 'quit':
        break
