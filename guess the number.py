import random

playagain = 'y'
while playagain != 'n':
    gc = 0
    actual = random.randint(1, 100)
    while True and gc<10:
        x= int(input ('\n Guess the number I have on my mind. Enter your guess: ',))
        gc += 1
        if x < actual:
            print ("number is bigger than", x, "\n you have", int(10-gc),"attempts left")
            continue
        elif x > actual:
            print ("number is smaller than", x,  "\n you have", int(10-gc),"attempts left")
            continue
        elif x == actual:
            print ("congratulations you lucky ba**ard. You guessed it in ", gc, "count/s" )
            break
    if gc>=9:
        print("you took a  long time to guess. Too bad. The secret number on my mind was", actual)

    playagain = input('play again? y/n :')
    continue
