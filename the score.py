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
question_1 = input("enter the word blue: ").lower()
if question_1 == "blue":
    Score = Score+1

question_1 = input("enter the word red: ").lower()
if question_1 == "red":
    Score = Score+1

question_1 = input("enter the word green: ").lower()
if question_1 == "green":
    Score = Score+1

print(f"{Score}")