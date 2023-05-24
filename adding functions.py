
# define quiz; i only made this a fuction for the sake of passing, it is called at the end of rules
def quiz():
    score = 0
    play_again = "yes"
    # loop of game starts here, top of while loop, asks all the questions
    while play_again == "yes" or play_again == "y":
        print("THE GAME HAS BEGUN!!!")
        question_1 = input("Question 1:\n"
                           "Kikorangi means what in maori?;\n"
                           "A) Red\n"
                           "B) Blue\n"
                           "C) March\n"
                           "D) Seven\n"
                           "> ").lower()

        question_2 = input("Question 2:\n"
                           "what does 'Whero' mean?\n"
                           ">").lower()

        question_3 = input("Question 3:\n"
                           "which of these numbers is the greatest;\n"
                           "A) Tahi\n"
                           "B) Wha\n"
                           "C) Whitu\n"
                           "D) toru\n"
                           "> ").lower()

        question_4 = input("Question 4;\n"
                           "kakariki means what?\n"
                           "A) Red\n"
                           "B) Black\n"
                           "C) Yellow\n"
                           "D) Green\n"
                           "> ").lower()

        question_5 = input("Question 5;\n"
                           "What does karaka mean?\n"
                           "> ").lower()

        question_6 = input("Question 6;\n"
                           "what does Tekau mean?\n"
                           "> ").lower()

        question_7 = input("Question 7;\n"
                           "which one of the following means One:\n"
                           "A) Ono\n"
                           "B) Wha\n"
                           "C) Tahi\n"
                           "D) Iwa\n"
                           "> ").lower()

        question_8 = input("Question 8\n"
                           "enter the word for red in Maori\n"
                           "> ").lower()

        question_9 = input("Question 9\n"
                           "what does Pipiri mean\n"
                           "> ").lower()

        question_10 = input("Question 10\n"
                            "which of these is not a colour;\n"
                            "A) ma\n"
                            "b) whero\n"
                            "C) Kakariki\n"
                            "D) Karaka\n"
                            "> ").lower()

        # the final result; the score is checked and they player is given a witty remark on hwo well they did.

        print("Final Result.\n")

        if question_1 == "b":
            print("Q1 correct")
            score = score + 1

        if question_2 == "red":
            print("Q2 correct")
            score = score + 1

        if question_3 == "c":
            print("Q3 correct")
            score = score + 1

        if question_4 == "d":
            print("Q4 correct")
            score = score + 1

        if question_5 == "orange":
            print("Q5 correct")
            score = score + 1

        if question_6 == "ten":
            print("Q6 correct")
            score = score + 1

        if question_7 == "c":
            print("Q7 correct")
            score = score + 1

        if question_8 == "whero":
            print("Q8 correct")
            score = score + 1

        if question_9 == "green":
            print("Q9 correct")
            score = score + 1

        if question_10 == "a":
            print("Q10 correct")
            score = score + 1

        print(f"you got a Score of {score}/10")
        # witty remark on skill level

        if score <= 5:
            print("bro, you gotta work on your stuff.")
        elif score == 5:
            print("congrats, you are exactly average")
        elif score <= 10:
            print("nice, not entirely useless")
        else:
            print("wow, you can use a serch bar, good one, you almost got away with it too.")

        # play again2; this is the choice to play again or not. if not the game ends, if so it loops.

        print("#" * 40)
        play_again = input("Play again?: ")


# Welcome; this is the start of the main script, it welcomes players to the game

def game():
    rules = input("Welcome To the Te Reo Maori Quiz\n"
                  "would you like the rules?:").lower()
    if rules == "y" or rules == "yes":

        # rules; this is where players can have the choice to see the rules or not.
        # if they do not it starts game right away

        print("x"*40)
        the_rules = input("These are the rules.\n"
                          "You will be asked 10 questions,\n"
                          "some will be mutli-choice and some will be written.\n"
                          "for multi-choice aswers, you will be given 4 options,\n"
                          "'A','B','C', and 'D'.\n"
                          "enter the letter as an answer not the word.\n"
                          "for the written questions you will be asked a question.\n"
                          "the answer will be a single word.\n"
                          "(pls note that if you spell the word wrong it will be marked as inccorect)\n"
                          "at the end of the game you will get a score out of ten.\n\n"
                          "HAVE FUN\n"
                          "Enter anything to start: ")

        print("x"*40)
        if the_rules == "asdfghjkl":
            print("EASTER EGG")

    quiz()


game()

print("THX FOR PLAYING")
