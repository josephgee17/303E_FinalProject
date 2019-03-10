def main():
    X = eval(input("What is X?" ))
    Y = eval(input("What is Y?" ))
    Z = eval(input("What is Z?" ))
    mean = (X + Y + Z) / 3
    print("The mean is " + str(mean))


main()


def main():
    X = eval(input("what is X? "))
    odd = (X % 2 == 1)
    even = (X % 2 == 0)
    print("This number is even: " + str(even))
    print("This number is odd: " + str(odd))


main()


def main():
    X = eval(input("what is X? "))
    odd = (X % 2 == 1)
    even = (X % 2 == 0)
    print("This number is even: ", even)
    print("This number is odd: ", odd)


main()


def main():
    myList = [42, 28, 4, 7, 93, 101]
    myList[1] = 42
    ind = 3
    print(myList[5])
    myList.append(55)
    print(myList)
    myList2 = [3, 4]
    myList.extend(myList2)
    print(myList)


main()


#def main():
    #myWeek = ["M", "T", "W", "TH", "F", "S", "SU"]
    #print(myWeek)
    #print(myWeek[2])


#main()


#def main():
    #months = ["Jan", "F", "Mar", "A", "May", "Jun", "Jul", "Au", "S", "O", "N", "D"]
    #print(months)

#main()


def main():
    months = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "August", "Sept", "Oct", "Nov", "Dec"]
    myWeek = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    myWeekN = eval(input("What is the day of the week in number format? ")) - 1
    monthformN = eval(input("What is the number of month? ")) - 1
    dayofmonth = eval(input("what is the day of the month in number format? "))
    year = eval(input("What is the year? "))
    print(myWeek[myWeekN], months[monthformN], dayofmonth, year)

main()


def main():
    x = ((3.99+6.98+4.49)/3)
    print(x)
    print(str((3.99+6.98+4.49)/3))

main()


#def main():
    #x = (4%2) + 2
    #if (x == 2):
    ##if (((4%2) + 2) = 2): is also acceptable as long as its before the end of the if colon
        #print("Yay! x==2!")
    ##if x == 2 is also acceptable
    #else:
        #print("Boo ;( x != 2!")

#main ()

def main():
    x = eval(input("Pick a number 1 through 10: "))
    if (x > 10):
        print("Boo! You did not follow directions!")
    elif (x < 1):
        print("Boo! You did not follow directions!")
    else:
        print("Yay! you followed directions! " + str(x))

main ()

def main():
    count = 5
    if (count > 0):
        print("Python is fun!")
        count = count - 1
        print("Value of count = " + str(count))


main()


def main():

    value = 3

    if(value !=3):
        print("Have a nice day!")
    else:
        print("Have a great day!")


main()


def main():

    number = eval(input("Enter a number between 1-99: "))
    while(number < 1 or number > 99):
        number = eval(input("Enter a number between 1-99: "))


main()


def main():
    num = 2
    for num in range(0, 5):
        print(num)
        if (num == 3):
            break
        for num2 in range(2, 9, 3):
            print(num2)

    #for num in range(0, 3):
        #print(num)


main()


def main():
    for letter in "Stephany":
        print(letter)

    fruits = ["Strawberry", "Apple", "Orange", "Watermelon", "Mango", "Pear", "Peach", "Banana"]
    for fruit in fruits:
        print(fruit)

    for fruit in range(len(fruits)):
        print(fruit)
        print(fruits[fruit])

main()


def main():
    num = []
    for x in range(-5,6,1):
        num.append(x)
    print(num)


main()


def main():
    num = 9
    while (num > 8 and num <= 29):
        print(num)
        num += 3

main()


def main():
    list = []
    num = -5
    while (num > -6 and num <= 5 ):
        list.append(num)
        num += 1
    print(list)

main()


def main():
    list = [9,1,8,99,45,78,14,2,7,69]
    sum = 0
    for val in list:
        sum += val
    print(sum)

main()


def displayUserMenu():
    print("Enter D")
    print("Enter A")
    print("Enter E")


def main():
    displayUserMenu()


main()


def reverseAString(word):
    resultString = ""
    for let in word:
        resultString = let + resultString
    return resultString

def main():
    print(reverseAString("hello"))


main()

def main():

    numbers = []

    while(True):
        try:
            if num > 0:
                num = eval(input("Enter a number: "))
                numbers.append(num)
                #print("Before check " + str(num))
            elif num < 0:
                break
                #print("Before append " + str(num))
                #numbers.append(num)
        except:
            print("Not a number. Try again.")

    numbers.sort()
    print(numbers)

main()

def main():
    #Tuples: Immutable
    tuple1 = ("hello", "goodbye", 1776, 42)
    total = tuple1[2] + tuple1[3]
    print(total)

    numbers = (1, 2, 3, 4, 5, 6, 7, 8)
    print(numbers[2:5])
    newTuple = tuple1 + numbers
    print(newTuple)
    print(len(newTuple))

    t1 = (1, 2, 3, 4)
    t2 = (2, 3, 4)

    print(max(t1))
    print(min(t2))

    t3 = tuple(["hello", "whatever", "something"])
    print(t3)

    #if cmp(t1, t2) == 0:
        #print("match")
    #else:
        #print("not match")


main()

def main():
    numbers = []

    while (True):
        try:
            currNum = (input("Enter a number:"))
            if currNum == "STOP":
                break;
            currNum = float(currNum)
            print("Before check" + str(currNum))
            if (currNum < 0):
                break;
            print("Before append" + str(currNum))
            numbers.append(currNum)
        except:
            print("Not a number! Try that again")

    print(numbers)


main()

def main():
    #try:
    #   code
    ##except <Exception>:
    #   handler code
    #finally:
    #  code

    try:
        x = 42
        y = 0
        #userInput = int(input(""))
        result = x / y
        #print(result)
    except ZeroDivisionError:
        print("oops! you tried to divide by zero")
        result = 1
    #except:
        #print("oops! error occur")
        #result = 1

    print(result)

main()

def main():
    #try:
    #   code
    ##except <Exception>:
    #   handler code
    #finally:
    #  code

    try:
        x = 42
        y = 0
        #userInput = int(input(""))
        result = x / y
        #print(result)
    except ZeroDivisionError:
        print("oops! you tried to divide by zero")
        result = 1
    #except:
        #print("oops! error occur")
        #result = 1

    print(result)

main()
