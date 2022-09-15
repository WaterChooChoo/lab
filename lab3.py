play = 'Y'
# the main while loop for the game, checks at the end for user input Y or N
while play == 'Y':
    guess = 0
    print('Welcome to the Flarsheim Guesser!')
    userNum = int(input('Choose a number from 1 - 100. ' ))
    # makes sure the number is within bounds
    while userNum > 100 or userNum < 0:
        print('Your number must be between 1 and 100.')
        userNum = int(input('Choose a number from 1 - 100. ' ))
    # checks userNum / 3 remainder to make sure its valid
    userNum3 = int(input('What is the remainder of your number when divided by 3? ' ))
    while (userNum3 > 2) or (userNum3 < 0):
        if userNum3 > 2:
            print('The remainder must be less than 3.\n')
        else:
            print('The remainder must be 0 or greater.\n')
        userNum3 = int(input('What is the reaminder of your number when divided by 3? ' ))
    # checks userNum / 5 remainder to make sure its valid
    userNum5 = int(input('What is the remainder of your number when divided by 5? ' ))
    while (userNum5 > 4) or (userNum5 < 0):
        if userNum5 > 4:
            print('The remainder must be less than 5.\n')
        else:
            print('The remainder must be 0 or greater.\n')
        userNum5 = int(input('What is the reaminder of your number when divided by 5? ' ))
    # checks userNum / 7 remainder to make sure its valid
    userNum7 = int(input('What is the remainder of your number when divided by 7? ' ))
    while (userNum7 > 6) or (userNum7 < 0):
        if userNum7 > 6:
            print('The remainder must be less than 7.\n')
        else:
            print('The remainder must be 0 or greater.\n')
        userNum7 = int(input('What is the reaminder of your number when divided by 7? ' ))
    # compiles all remainders to get the final guess
    while guess != userNum:
        for i in range(101):
            if i % 3 == userNum3:
                if i % 5 == userNum5:
                    if i % 7 == userNum7:
                        guess = i
                        print(f'your number is {guess}')
    # asks if they want to play again
    play = input('Would you like to play again? ')
    while play != 'N' and play != 'Y':
        print(f'{play} is not a valid answer.')
        play = input('Would you like to play again? (Y or N) ')
    
                            
print('Thanks for playing!')
