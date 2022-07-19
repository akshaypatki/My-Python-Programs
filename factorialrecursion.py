def recursion (n):
    if n == 1:
        return 1
    elif n > 1:
        return n * recursion(n - 1)
while True:
    num = input('Enter the number for the factorial calculation: ')
    print (recursion(int(num)))
    conti = input ('continue? y/n :')
    if conti == "n":
        break