def main():
    #Step 0: I asked for info in one line:
    #After splitter and fib sequence is negative, i print an error screen.
    data = input("What fib sequence do you want to start at and what code do you want to send?")
    fibsequence, code = data.split(";")
    fibsequence = int(fibsequence) - 1
    if fibsequence < 0:
        print("Error")
    else:
    # I broke each step of the math sequence part by part
    # Step 1: Put ascii of base code into lower case no matter if it's initally lower or upper case
        code = code.lower()
        resultString = []
        for letter in code:
            resultString.append(ord(letter) - 96)

    # Step 2: Make fibonacci sequence. Combine ascii with chosen fibonacii pattern
        fibonacci = [0, 1]
        for i in range(2, 700):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        resultString2 = []
        for letter in code:
            resultString2.append(ord(letter) - 96 + fibonacci[fibsequence])
            fibsequence = fibsequence + 1

    # Step 3: Combine result from Step 2 and mod/% 26. Then turn to ascii upper case
        resultString3 = []
        base = 0
        for letter in code:
            resultString3.append((resultString2[base] % 26) + 64)
            base = base + 1

    # Step 4: Have final result translate into new code
        for letter in resultString3:
            print(chr(letter), end='')


main()