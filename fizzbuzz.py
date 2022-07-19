key = 1
sample = int(input('enter the value : ',))
if sample < 0 or sample > (2 * 10 ** 5):
    print("invalid input")
else:
    while key <= sample:
        if key % 3 == 0 and key % 5 == 0:
            print("FizzBuzz")
        elif key % 3 == 0 and key % 5 != 0:
            print("Fizz")
        elif key % 5 == 0 and key % 3 != 0:
            print("Buzz")
        else:
            print(key)
        key +=1