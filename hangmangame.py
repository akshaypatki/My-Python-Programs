import random
key = 1
i=0
while True:
    lines = open('hangmansource.txt').read().splitlines()
    guessword =random.choice(lines)
    count = len(guessword)
    print (count * "*")

    done = 0
    letter = ""
    while done < count:
        letter = input('enter your guess',)
        if letter in guessword:
            print ("cool")
            done +=1
        else : print ("keep trying")
        continue




    print("Yipee:the word was",guessword, "and it was",count," letters long")


    if input('play again? y/n' ,) != 'n' : continue
    else: break
    continue