def main():

    #I wrote my own code just so I don't have to try to deduce the professor's code she gave us.
    #Step 0: Have answer, ask guess, put all letters into upper case. Make sure guesses are valid.
    #Note: I made my answer pretty funny by choosing one of the letters and making it the entire answer :)
    answer = ["W", "W", "W", "W"]
    choices = ["R", "G", "Y", "P", "B", "O", "W", " "]
    feedback = []
    guess = input("Guess: ")
    guess = guess.upper()
    guess = list(guess)
    #Step 1: make sure user's guess is appropriate length. ask until len = 4
    while len(guess) > 4 or len(guess) < 4 :
        print("Error")
        guess = input("Guess: ")
        guess = guess.upper()
        guess = list(guess)
    #Step 2: Create a feedback form for guess to answer
    if answer[0] == guess[0]:
        feedback.append("W")
    else:
        feedback.append("_")
    if answer[1] == guess[1]:
        feedback.append("W")
    else:
        feedback.append("_")
    if answer[2] == guess[2]:
        feedback.append("W")
    else:
        feedback.append("_")
    if answer[3] == guess[3]:
        feedback.append("W")
    else:
        feedback.append("_")
    print("Feedback: ", end="")
    for letter in feedback:
        print(letter, end="")
    print("")
    #Step 3: Print out score. If error is given, doesn't count to score, just like the sample on the instructions.
    score = 1
    if answer[0] == guess[0] and answer[1] == guess[1] and answer[2] == guess[2] and answer[3] == guess[3]:
        print("Score: -" + str(int(score)))
    feedback.clear()

    #Step 4: If first proper guess is not correct, create loop until correct guess is performed.
    while answer[0] != guess[0] or answer[1] != guess[1] or answer[2] != guess[2] or answer[3] != guess[3]:
        guess = input("Guess: ")
        guess = guess.upper()
        guess = list(guess)
        while len(guess) > 4 or len(guess) < 4 :
            print("Error")
            guess = input("Guess: ")
            guess = guess.upper()
            guess = list(guess)
        if answer[0] == guess[0]:
            feedback.append("W")
        else:
            feedback.append("_")
        if answer[1] == guess[1]:
            feedback.append("W")
        else:
            feedback.append("_")
        if answer[2] == guess[2]:
             feedback.append("W")
        else:
            feedback.append("_")
        if answer[3] == guess[3]:
            feedback.append("W")
        else:
            feedback.append("_")
        print("Feedback: ", end="")
        for letter in feedback:
            print(letter, end="")
        feedback.clear()
        print("")
        #Step 6: Print out score. If error is given, doesn't count to score, just like the sample on the instructions.
        #Note: Score is added per proper guess until guess is correct. if score > 10, you lose
        score = score + 1
        if answer[0] == guess[0] and answer[1] == guess[1] and answer[2] == guess[2] and answer[3] == guess[3]:
            print("Score: -" + str(int(score)))
        if score > 10:
            break

main()