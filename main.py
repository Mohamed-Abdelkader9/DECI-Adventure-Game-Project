#import time library
import time

#import random library
import random

def print_pause(text):
    #prints the given text and pauses for a short period of time.
    print(text)
    time.sleep(.1)

score = 0
monsters = ["monster1", "monster2"]

def game():
    #initializes the game by setting the score to 0.
    global score
    #introduces the player to the story.
    print_pause("You stand opposite a house with a death body.")
    print_pause("And behind the house stand two police officers.")

    #asks the player to make a choice: enter the house or escape.
    print_pause("to enter the house, enter 1")
    print_pause("to escape from this place, enter 2")

    def option1():
        #asks the player to make a choice.
        player_choice = input("Enter 1 or 2: ")

        #handles the player's choice.
        if player_choice == "1":
            #enters the house and nighttime falls.
            print_pause("You enter the house and nighttime falls.")
            print_pause("You left the house and officers disappeared.")

            #increments the score.
            global score
            score += 1
            print_pause(f"Your current score: {score}")

            print_pause("To discover the forest, enter 1")
            print_pause("To hide in the house, enter 2")

            #presents the player with another choice.
            def option2():
                #asks the player to choose
                player_choice2 = input("Please enter 1 or 2:")

                #handles the player's choice.
                if player_choice2 == "1":
                    #enters the forest and finds a strange monster.
                    print_pause("You entered the forest")
                    print_pause("You find a strange monster")
                    global score
                    score += 1
                    print_pause(f"Your current score: {score}")

                    print_pause("to give him your back and go, enter 1")
                    print_pause("to go but while you look at him, enter 2")

                    #presents the player with another choice.
                    def option3():
                        global score
                        #asks the player to choose
                        player_choice3 = input("Enter 1 or 2:")

                        #handles the player's choice.
                        if player_choice3 == "1":
                            #the monster kills the player.
                            print_pause("the monster started to ran after you")
                            print_pause("the monster killed you")
                            print_pause(f"Your current score: {score}")
                            print_pause("you lost")
                            play_again()

                        elif player_choice3 == "2":
                            #the player escapes.
                            print_pause("you finally escaped")
                            score += 1
                            print_pause(f"Your current score: {score}")
                            play_again()

                        else:
                            #invalid choice, prompts the player to try again.
                            print_pause("Invalid choice, please enter 1 or 2.")
                            option3()
                    option3()

                elif player_choice2 == "2":
                    #a lot of monsters appear and kill the player.
                    print_pause("A lot of monsters appear and kill you")
                    print_pause(f"Your current score: {score}")
                    play_again()

                else:
                    #invalid choice, prompts the player to try again.
                    print_pause("Invalid choice, please enter 1 or 2.")
                    option2()

            def option4():
                #asks the player to choose
                player_choice4 = input("Please enter 1 or 2:")
                #handles the player's choice.
                if player_choice4 == "1":
                    #enters the forest and finds a strange monster.
                    print_pause("You entered the forest")
                    print_pause("You find a strange monster")
                    global score
                    score += 1
                    print_pause(f"Your current score: {score}")
                    print_pause("to continue looking at it, enter 1")
                    print_pause("to go and escape, enter 2")

                    def option5():
                        #asks the player to make a choice:
                        player_choice5 = input("Enter 1 or 2:")
                        if player_choice5 == "1":
                            print_pause("it attacked you and kill you")
                            global score
                            print_pause(f"Your current score: {score}")
                            play_again()
                        elif player_choice5 == "2":
                            print_pause("you finally escaped")
                            score += 1
                            print_pause(f"Your current score: {score}")
                            play_again()
                        else:
                            print_pause("Invalid choice, enter 1 or 2")
                            option5()
                    option5()


                elif player_choice4 == "2":
                    #a lot of monsters appear and kill the player.
                    print_pause("A lot of monsters appear and kill you")
                    print_pause(f"Your current score: {score}")
                    play_again()

                else:
                    #invalid choice, prompts the player to try again.
                    print_pause("Invalid choice, please enter 1 or 2.")
                    option4()
            if random.choice(monsters) == "monster1":
                option2()
            elif random.choice(monsters) == "monster2":
                option4()


        elif player_choice == "2":
            #the player escapes, but nighttime falls and a monster appears.
            print_pause("Nighttime falls and atmosphere darkens.")
            print_pause("A monster appears and kills you.")
            print_pause(f"Your current score: {score}")
            play_again()

        else:
            #invalid choice, prompts the player to try again.
            print_pause("Invalid choice, please enter 1 or 2.")
            option1()

    option1()

def play_again():
    #make the player choose to play again or no
    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() == "yes":
        global score
        score = 0
        game()
    elif choice.lower() == "no":
        print_pause("Goodbye!")
    else:
        print_pause("Invalid choice, please enter yes or no.")
        play_again()

game()