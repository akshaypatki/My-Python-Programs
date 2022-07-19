var = input('enter the calculation')
if str(var) == "45*3":
    print ("your answer is 555")
elif str(var) == "56+9":
    print ("your answer is 77")
elif str(var) == "56/6":
    print ("your answer is 4")
elif str(var) != "0":
    print ("your answer is", eval(var))