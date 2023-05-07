Score = 0

#main script

#Welcome

Rules = input("Welcome To the Te Reo Maori Quiz\n"
      "would you like the rules?:").lower()
if Rules == "y" or Rules == "yes":

#rules

    print ("x"*40)
    print ("These are the rules.\n"
           "You will be asked 10 questions,\n"
           "some will be mutli-choice and some will be written.\n"
           "for multi-choice aswers, you will be given 4 options,\n"
           "'A','B','C', and 'D'.\n"
           "enter the letter as an answer not the word.\n"
           "for the written questions you will be asked a question.\n"
           "the answer will be a single word.\n"
           "(pls note that if you spell the word wrong it will be marked as inccorect)\n"
           "at the end of the game you will get a score out of ten.\n\n"
           "HAVE FUN")
    print ("x"*40)

#start game

print ("THE GAME HAS BEGUN!!!")
question_1 = input("Question 1:\n"
                   "Kikorangi means what in maori?;\n"
                   "A Red\n"
                   "B Blue\n"
                   "C March\n"
                   "D Seven\n"
                   "> ").lower()
if question_1 == "b":
    Score = Score+1

question_2 = input("Question 2:\n"
                   "what does 'Whero' mean?").lower()
if question_2 == "red":
    Score = Score+1

question_3 = input("Question 3:\n"
                   "which of these numbers is the greatest;\n"
                   "A Tahi\n"
                   "B Wha\n"
                   "C Whitu\n"
                   "D toru\n"
                   "> ").lower()
if question_3 == "c":
    Score = Score+1

question_4 = input("Question 4;\n"
                   "kakariki means what?\n"
                   "A) Red\n"
                   "B) Black\n"
                   "C) Yellow\n"
                   "D) Green\n"
                   ">").lower()
if question_4 == "d":
    Score = Score+1

question_5 = input("Question 5;\n"
                   "What does karaka mean?\n"
                   ">").lower()
if question_5 == "orange":
    Score = Score+1

question_6 = input("Question 6;\n"
                   "what does Tekau mean?\n"
                   ">").lower()
if question_6 == "ten":
    Score = Score+1

question_7 = input("Question 7;\n"
                   "which one of the following means One:\n"
                   "A) Ono\n"
                   "B) Wha\n"
                   "C) Tahi\n"
                   "D) Iwa\n"
                   ">").lower()
if question_7 == "c":
    Score = Score+1

question_8 = input("Question 8\n"
                   "enter the word for red in Maori\n"
                   ">").lower()
if question_8 == "whero":
    Score = Score+1

question_9 = input("Question 9\n"
                   "what does Pipiri mean\n"
                   ">").lower()
if question_9 == "green":
    Score = Score+1

question_10 = input("Question 10\n"
                    "which of these is not a colour;\n"
                    "A) ma\n"
                    "b) whero\n"
                    "C) Kakariki\n"
                    "D) Karaka\n"
                    ">").lower()
if question_10 == "a":
    Score = Score+1

print(f"{Score}")