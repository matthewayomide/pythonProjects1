#build a guessd d number game
"""take the user name ,print hi + the name and say i ve guess  a number btw 1,100 and you have 8 trials to guess it
if guess is less than zero or greater than 100 - print guess is out of play
the user only has 8 trials
if the guess is wrong ,let the user guess again
if the user guess right . congratulate d user and print the number of times it took to guess right"""


from random import randint


start = 1
end = 100
value = randint(start,end)
print('GUESS THE NUMBER GAME')

name = (input('Please input your name'))
print(f'Hello {name}!. I have thought of a number between {start} and {end}.\nyou have 8 trials to guess the right number')

def game():
    count = 0
    guess = None

    try:
        while guess != value:
                guess = int(input('input your guess'))

            # for i in range(9):
                if guess < start or guess > end:
                    print(f'your guess it out of play, choose between {start} and {end} ')
                    count +=1

                if value > guess:
                    print('The number is higher')
                    count +=1
                if value < guess:
                    print('The number is lower')
                    count +=1



                if count > 8:

                   print(f'Sorry you have exceeded the number of trials allowed.\nThe number is {value}.\nTry again next time.')
                   break

        else:
            print(f'Congratulation {name}! You guess the number right.\nThe number is {value}.\nIt took you {count} trials')




    except ValueError:
        print('please input a number')
        game()

if __name__ =='__main__':
    game()

