import random

def main():
   print("Welcome to the Virtual Magic 15 Ball Program.")
   name = input("What is your name? ")
   question = input("Hello " + name + "! What is your question? ")
   answer = ["Yes", "No", "Yes, but not now", " Um, definitely no", "That is a terrible idea", "Why would you even ask that?", "Only on Sundays", "Only if you don't want lunch", "You really wasted a question on that but sure", "Honestly why don't you look up what an 8 ball would say", "Honestly why not", "For what?", "Ummmm. sure", "OK. You do you", "Sure but why?"]
   genNum = random.randint(0,14)
   print(answer[genNum])


main()