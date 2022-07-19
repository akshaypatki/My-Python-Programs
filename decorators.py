""" 
'''def shout(text):
    return text.upper()


print(shout('hello'))
yell = shout
print(yell('hello'))


# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
#    greeting = func()
    print(greeting)

greet(shout)
greet(whisper)

def halu(kasa):
    return kasa.lower()

def jorat(kasa):
    return kasa.upper()

string = "je sangayacha te ikde liyachya."

def bola(kasa):
    sangto = kasa(string)
    print (sangto)

bola (jorat)
bola (halu)
#newline

"""
# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x + y

    return adder

add_15 = create_adder(90)

print (create_adder(15),20)
print (add_15(20))
print(add_15(10))