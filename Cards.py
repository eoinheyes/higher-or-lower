import random

def splashScreen():
    print("Welcome to Higher Or Lower!")
    menu()

def menu():
    print("---------------------------")
    print("1. Single Player")
    print("---------------------------")
    print("2. Exit Game")
    print("---------------------------")
    option = input("Please enter your chosen option number: ")
    if option == "1":
        singlePlayer()
    elif option == "2":
        print("Exiting game...")

    else:
        print("Invalid option. Please select one of the numbered options listed.")
        menu()


#Sets up the deck of cards, utilising a loop to combine 2 arrays into one 3-dimensional array representing each card and its value
def Deck():
    suits = ["Hearts","Diamonds","Spades","Clubs"]
    ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    array3d = []
    for s in suits:
        for i, r in enumerate(ranks):
            card = [r,s, values[i]]
            array3d.append(card)
    return array3d

#Sets up the random cards selected in the game.
def Row(deck):
    rowLength = 5
    return random.sample(deck, rowLength)

def singlePlayer():
    points = 0
    game = Row(Deck())
    for i in range(len(game)-1):
        higher = True
        if i == 0:
            print("Your first card is... the " + game[i][0] + " of "+ game[i][1] +".")
        answer = input("Is the next card higher (H) or Lower? (L)")
        print("Your next card is... the " + game[i+1][0] + " of "+ game[i+1][1] +".")
        if game[i][2] < game[i+1][2]:
            print("The card is higher!")
            if answer.upper() == "H":
                points=points+1
                print("You earn a point")
            else:
                points=points-1
                print("You lose a point")
        elif game[i][2] > game[i+1][2]:
            print("The card is lower!")
            higher = False
            if answer.upper() == "L":
                points=points+1
                print("You earn a point.")
            else:
                points=points-1
                print("You lose a point.")
        elif game[i][2] == game[i+1][2]:
            print("It's a pair, you don't get anything for a pair, not in this game!")
            points=points-1
            print("You lose a point.")
    print("Your final score is "+ str(points))
    menu()


splashScreen()








