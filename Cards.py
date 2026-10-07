import random

def splashScreen():
    print("Welcome to Higher Or Lower!")
    menu()

def menu():
    #The user picks a number, corresponding to an option on the menu.
    print("---------------------------")
    print("1. Single Player")
    print("---------------------------")
    print("2. Endless Mode")
    print("---------------------------")
    print("3. Exit Game")
    print("---------------------------")
    option = input("Please enter your chosen option number: ")
    if option == "1":
        singlePlayer()
    elif option == "2":
        endlessMode()
    elif option =="3":
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
    player1game = Row(Deck(), 5)
    player2game = Row(Deck(), 5)
    p1points = 0
    p2points = 0

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








