import random
import sys

def mainMenu():
    #turnMenu()
    # This is the main menu where the user first arrives
    print("Welcome to Dragon Adventure Quest City Slamajam")
    print("Press P to play")
    print("Press S for scores")
    print("Press E to exit program")
    userInput = input("").upper()
    if userInput == "P":
        dragoncreation()
    elif userInput == "S":
        scoreMenu()
    elif userInput == "E":
        sys.exit()
    else:
        print("Not Valid Input")
        mainMenu()

class dragon:
  # This class gives attributes the dragon, which is essentially the user's character throughout the game
    def __init__(self, name = '', color = '', health = 50, gold = 0):
        self.name = name
        self.color = color
        self.health = health
        self.gold = gold

    def dragonAttack(self, vAttack, vGold):
        self.health -= vAttack
        self.gold += vGold
        self.gold = int(self.gold)
        self.health = int(self.health)
        print('Current Health: '+str(self.health)+' Current Gold: '+str(self.gold))

    def stall(self):
        self.health += 10
        if self.health >= 50:
            self.health = 50
        print("Health: " + str(self.health))

def dragoncreation():
  	# This creates the user's character
    userDragon = dragon()

    name = input("Hello! What is your name? ")
    color = input("What color would you like your dragon to be? ")
    player = (name + " the " + color + " dragon")
    confirm = input("Is " + name + " the " + color + " dragon correct? Y/N " ).upper()
    if confirm == 'Y':
        file = open('Scores.txt','a')
        file.write("Name: "+player+'\n')
        file.close()
        turnMenu(userDragon)
    elif confirm == 'N':
        dragoncreation()
    else:
        print("Not yes or no")
        dragoncreation()

def turnMenu(dragon):
    # This function contains the main game play
    turn = 0
    while turn <= 10 and dragon.health >= 0:
        print("Press P choose a city to pillage")
        print("Press S to stall for health")
        print("Press Q to quit game mode")
        turnsLeft = 10-turn
        print("Turns remaining: "+str(turnsLeft))
        userInput2 = input("").upper()
        if userInput2 == "P":
            turn += 1
            cityOptions(dragon)
        elif userInput2 == "S":
            turn +=1
            dragon.stall()
        elif userInput2 == 'Q':
            endGame()
        else:
            print("Not valid input")
    if turn > 10 or dragon.health < 0:
        print("Final Score: " + str(dragon.gold))
    hallOfFame(dragon)
    mainMenu()

def hallOfFame(dragon):
    file = open('Scores.txt', 'a')
    file.write('Score: '+ str(dragon.gold)+'\n')
    return

def cityOptions(dragon):
  	# This function allows the user to choose which city to attack
    Houston = village(200,20)
    Dallas = village(200,20)
    Austin = village(100, 10)
    SanAntonio = village(125, 13)
    ElPaso = village(175, 18)
    print('Type the first letter of the city you would like to attack!')
    print('(A)ustin')
    print('(D)allas')
    print('(E)l Paso')
    print('(H)ouston')
    print('(S)an Antonio')
    CD = input("").upper()
    if CD == "H":
        attackphase(Houston,dragon)
    elif CD == "A":
        attackphase(Austin,dragon)
    elif CD == "D":
        attackphase(Dallas,dragon)
    elif CD == "E":
        attackphase(ElPaso,dragon)
    elif CD == "S":
        attackphase(SanAntonio,dragon)
    else:
        print("That's not a city!")
        cityOptions(dragon)

    #ask user what city they want to attack
    #have attack phase play out
    #return to turn menu

def scoreMenu():
  	# This function shows the user the scores
    file = open("Scores.txt","r")
    for x in file:
        print(x.strip("\n"))
    leaving = input("Press anything to go to menu")
    str(leaving)
    if leaving == '':
        mainMenu()
    else:
        mainMenu()


class village:
  # This class creates the various villages that can be attacked
  def __init__(self, gold = 100, damage = 25 ):
      self.gold = gold
      self.damage = damage

def probability():
	# This is our random number generator. It is used to determine how much gold you recieve, as well as how much damage you take
   # returns a percentage
   percent = random.random()
   return percent

def attackphase(village, dragon):
  	# This is the function in which the dragon attacks the village and changes to health and damage are assessed
    vDamage = village.damage
    vGold = village.gold
    finalDamage = vDamage * probability()
    finalGold = vGold * probability()
    finalDamage = int(finalDamage)
    finalGold = int(finalGold)
    print("Damage taken: "+str(finalDamage)+" Gold gained: "+str(finalGold))
    dragon.dragonAttack(finalDamage, finalGold)

def endGame():
  # This ends the game if the player so chooses to
    sys.exit()

def main():
    mainMenu()

main()
