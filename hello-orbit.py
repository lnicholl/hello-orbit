print("Let's play a game of two truths and a lie! Although this is slightly different...\nThere are three rounds each with a couple of intro questions about me as a warm up.\nYou will then be presented with one ***TRUTH OR LIE*** question at the end of each round.\nGood luck!\n")

correct_answers = 0

# check answer to question is either Y or N, capitalise if in lower case
def askQuestion(question):
    while True:
        answer = input(question).upper()
        if answer == "Y" or answer == "N":
            return answer
        else:
            print('Please enter a valid response!')

# loop through each round until all intro answers are correct
while True:
    # if intro answer is correct, move on to next question
    try:
        music_1 = askQuestion("Is Laurie a classically trained singer? Y/N ")
        if music_1 == "N":
            print("Correct!\n")
        # if intro answer is incorrect, go straight to except block and restart the round
        else:
            raise Exception

        music_2 = askQuestion("Can Laurie rap the whole of 'The Eminem Show?' Y/N ")
        if music_2 == "Y":
            print("Correct!\n")
        else:
            raise Exception

        music_3 = askQuestion("***TRUTH OR LIE!*** Laurie's uncle won Eurovision in 1997 with Katrina and the Waves. Y/N ")
        if music_3 == "Y":
            print("We'll see! Moving onto the next round...\n")
            # if ***TRUTH OR LIE*** question answered correctly, one point is added to correct_answers
            correct_answers += 1
        # if ***TRUTH OR LIE*** answered incorrectly, we still move onto the next round and skip Exception
        else:
            print("We'll see! Moving onto the next round...\n")

    # we print a message if Exception is raised and loop restarts
    except:
        print("Incorrect! Back to the start\n")

    # once all questions are answered correctly, break from the loop
    else:
        break

while True:
    try:
        sport_1 = askQuestion("Was Laurie was the only girl on her football team as a child? Y/N ")
        if sport_1 == "Y":
            print("Correct!\n")
        else:
            raise Exception

        sport_2 = askQuestion("Did Laurie break her leg doing a horrendous sliding tackle? Y/N ")
        if sport_2 == "N":
            print("Correct!\n")
        else:
            raise Exception

        sport_3 = askQuestion("***TRUTH OR LIE!*** Laurie once played for England girls U14's. Y/N ")
        if sport_3 == "N":
            print("We'll see! Moving onto the next round...\n")
            correct_answers += 1
        else:
            print("We'll see! Moving onto the next round...\n")

    except:
        print("Incorrect! Back to the start\n")

    else:
        break

while True:
    try:
        food_1 = askQuestion("Has Laurie eaten snake? Y/N ")
        if food_1 == "N":
            print("Correct!\n")
        else:
            raise Exception

        food_2 = askQuestion("Has Laurie eaten a 100-year-old EGG? Y/N ")
        if food_2 == "Y":
            print("Correct!\n")
        else:
            raise Exception

        food_3 = askQuestion("Has Laurie eaten raw horse? Y/N ")
        if food_3 == "Y":
            print("Correct!\n")
        else:
            raise Exception

        food_4 = askQuestion("Has Laurie eaten kangaroo? Y/N ")
        if food_4 == "N":
            print("Correct!\n")
        else:
            raise Exception

        food_5 = askQuestion("Has Laurie eaten cow brain? Y/N ")
        if food_5 == "Y":
            print("Correct!\n")
        else:
            raise Exception

        food_6 = askQuestion("***TRUTH OR LIE!*** Laurie is now a vegetarian! Y/N ")
        if food_6 == "Y":
            correct_answers += 1

    except:
        print("Incorrect! Back to the start\n")

    else:
        break

# find out how you did!
if correct_answers == 3:
    print("\nYou got all three ***TRUTH OR LIE*** correct! You must have cheated ;)")
elif correct_answers >= 1:
    print("\nYou got " + str(correct_answers) + " out of 3 ***TRUTH OR LIE*** correct! Can you guess which ones? ;)")
else:
    print("\nYou got 0 **+TRUTH OR LIE*** correct... Try again?")