import random
import Player

def splashScreen():
    print("Welcome to Higher Or Lower!")
    login()

def login():
    username = input("Enter your username: ")
    player1 = Player.Player(username, 0)
    print("Welcome "+ player1.username +"!")
    menu()

def menu():
    #The user picks a number, corresponding to an option on the menu.
    print("---------------------------")
    print("1. Single Player")
    print("---------------------------")
    print("2. Multiplayer Mode")
    print("---------------------------")
    print("3. Endless Mode")
    print("---------------------------")
    print("4. Exit Game")
    print("---------------------------")
    option = input("Please enter your chosen option number: ")
    if option == "1":
        singlePlayer()
    elif option == "2":
        multiPlayer()
    elif option =="3":
        endlessMode()
    elif option =="4":
        print("Exiting game...")
    else:
        print("Invalid option. Please select one of the numbered options listed.")
        menu()


#Sets up the deck of cards, utilising a loop to combine 3 arrays into one 2-dimensional array representing each card and its value
def Deck():
    suits = ["Hearts","Diamonds","Spades","Clubs"]
    ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    array2d = []
    for s in suits:
        for i, r in enumerate(ranks):
            card = [r,s, values[i]]
            array2d.append(card)
    return array2d

#Sets up the random cards selected in the game.
def Row(deck, rowLength):
    return random.sample(deck, rowLength)

def singlePlayer():
    #The user always starts with 0 points.
    points = 0
    game = Row(Deck(), 5)
    #One game is equal to the number of cards -1 iteration.
    for i in range(len(game)-1):
        if i == 0:
            print("Your first card is... the " + game[i][0] + " of "+ game[i][1] +".")
        answer = input("Is the next card higher (H) or Lower? (L)")
        print("Your next card is... the " + game[i+1][0] + " of "+ game[i+1][1] +".")
        #If the consecutive card is higher
        if game[i][2] < game[i+1][2]:
            print("The card is higher!")
            if answer.upper() == "H":
                points=points+1
                print("You earn a point")
            else:
                points=points-1
                print("You lose a point")
        #If the consecutive card is lower
        elif game[i][2] > game[i+1][2]:
            print("The card is lower!")
            if answer.upper() == "L":
                points=points+1
                print("You earn a point.")
            else:
                points=points-1
                print("You lose a point.")
        #If the cards are of equal value
        elif game[i][2] == game[i+1][2]:
            print("It's a pair, you don't get anything for a pair, not in this game!")
            points=points-1
            print("You lose a point.")
    #The user's final score is outputted here.
    print("Your final score is "+ str(points))
    menu()

def multiPlayer():
    game = Row(Deck(), 10)
    #Splits the deck for the two players using array slicing
    p1game = game[:len(game)//2]
    p2game = game[len(game)//2:]
    p1p = 0
    p2p = 0
    p1seq = 0
    p2seq = 0
    running = True

    while running:
        while p1seq < len(p1game):
            print("Player 1's turn...")
            print("")
            if p1seq == 0:
                print("Your first card is... the " + p1game[p1seq][0] + " of "+ p1game[p1seq][1] +".")
            answer = input("Is the next card higher (H) or Lower? (L)")
            print("Your next card is... the " + p1game[p1seq+1][0] + " of "+ p1game[p1seq+1][1] +".")

            #If the consecutive card is higher
            if p1game[p1seq][2] < p1game[p1seq+1][2]:
                print("The card is higher!")
                if answer.upper() == "H":
                    p1p=p1p+1
                    print("You earn a point")
                else:
                    p1p=p1p-1
                    print("You lose a point")
                    p1seq=p1seq+1
                    break
            
            #If the consecutive card is lower
            elif p1game[p1seq][2] > p1game[p1seq+1][2]:
                print("The card is lower!")
                if answer.upper() == "L":
                    p1p=p1p+1
                    print("You earn a point.")
                else:
                    p1p=p1p-1
                    print("You lose a point.")
                    p1seq=p1seq+1
                    break
            #If the cards are of equal value
            elif p1game[p1seq][2] == p1game[p1seq+1][2]:
                print("It's a pair, you don't get anything for a pair, not in this game!")
                p1p=p1p-1
                print("You lose a point.")
            p1seq=p1seq+1

        #Player 2 game
        while p2seq < len(p2game):
            print("Player 2's turn...")
            print("")
            if p2seq == 0:
                print("Your first card is... the " + p2game[p2seq][0] + " of "+ p2game[p2seq][1] +".")
            answer = input("Is the next card higher (H) or Lower? (L)")
            print("Your next card is... the " + p1game[p2seq+1][0] + " of "+ p2game[p2seq+1][1] +".")

            #If the consecutive card is higher
            if p1game[p2seq][2] < game[p2seq+1][2]:
                print("The card is higher!")
                if answer.upper() == "H":
                    p2p=p2p+1
                    print("You earn a point")
                else:
                    p2p=p2p-1
                    print("You lose a point")
                    p2seq=p2seq+1
                    break
            
            #If the consecutive card is lower
            elif p2game[p2seq][2] > p2game[p2seq+1][2]:
                print("The card is lower!")
                if answer.upper() == "L":
                    p2p=p2p+1
                    print("You earn a point.")
                else:
                    p2p=p2p-1
                    print("You lose a point.")
                    p2seq=p2seq+1
                    break
            #If the cards are of equal value
            elif p2game[p2seq][2] == p2game[p2seq+1][2]:
                print("It's a pair, you don't get anything for a pair, not in this game!")
                points=points-1
                print("You lose a point.")
            p2seq=p2seq+1

    #The users' final scores are outputted here.
    print("Player 1's final score is "+ str(p1p) +" points.")
    print("Player 2's final score is "+ str(p2p) +" points.")
    menu()


def endlessMode():
    streak = True
    game = Row(Deck(), 52)
    points = 0
    while streak:
        for i in range(len(game)-1):
            if i == 0:
                print("Your first card is... the " + game[i][0] + " of "+ game[i][1] +".")
            answer = input("Is the next card higher (H) or Lower? (L)")
            print("Your next card is... the " + game[i+1][0] + " of "+ game[i+1][1] +".")
            #If the consecutive card is higher
            if game[i][2] < game[i+1][2]:
                print("The card is higher!")
                if answer.upper() == "H":
                    points=points+1
                    print("You earn a point")
                else:
                    print("You lose.")
                    streak = False
                    break
                #If the consecutive card is lower
            elif game[i][2] > game[i+1][2]:
                print("The card is lower!")
                if answer.upper() == "L":
                    points=points+1
                    print("You earn a point.")
                else:
                    print("You lose.")
                    streak = False
                    break
            #If the cards are of equal value
            elif game[i][2] == game[i+1][2]:
                print("It's a pair, you don't get anything for a pair, not in this game!")
                print("You lose.")
                streak = False
                break
    #The user's final score is outputted here.
    print("Your final score is "+ str(points))
    menu()        


#The splashscreen is called, which sets the whole program in motion.
splashScreen()








