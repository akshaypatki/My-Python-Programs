# userinput = int(input('enter a number between 4 and 9',))
#
# if userinput != 0:
#     count = userinput
#     while count >= 0:
#         for i in range(count):
#             print("*", end =" "),
#         count = count -1
#         print ("")

count = int(input('enter a count for the astro pattern',))

var = count

while var != 0:
    for i in range(var):
        print ("*", end="")
    var -= 1
    # count -= 1
    print("")













