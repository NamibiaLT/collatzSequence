print('Pick a number')
userNumber = int(input())


def collatz(number):
    while number > 1:
        if number % 2 == 0: # even number
            evenNumber = number // 2
            print(str(evenNumber))
            number = evenNumber
        elif number % 2 == 1: # odd number
            oddNumber = 3 * number + 1
            print(str(oddNumber))
            number = oddNumber
    
collatz(userNumber)
