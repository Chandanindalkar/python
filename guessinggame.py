secret_word = input('Player 1 - Enter the Secret Word for Player 2 to guess:')
print('Player 2 - Guess the Secret Word')
guess = ''
guess_limit = 3
guessed = 1
guesses = False

while guess != secret_word and not guesses:
    if guessed <= guess_limit:
        print('Enter your guess:')
        guess = input()
        left = guess_limit - guessed
        guessed = guessed + 1
        print('Guesses left:'+str(left))

    else:
        guesses = True

if guesses:
    print('You Lose')

else:
    print('You Win')
