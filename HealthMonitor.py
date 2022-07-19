def getdate():
    import datetime
    return datetime.datetime.now()
index = {1:"akshayrecords.txt", 2:"poojarecords.txt"}
fname = ""
choice = None
print("Welcome to health record management system\n Whose entry are you making? [1] Akshay [2] Pooja Enter number:  ")
name = int(input())
while choice != 3:
    print ("What are you tracking? [1] Weight [2] Diet: [3] I am done ")
    choice = int(input())
    if choice == 1:
        detail = input('Enter the weight in lb :')
    elif choice == 2:
        detail = input('Enter the food intake :',)
    if name in index.keys() and name !=3 :
        newstr = ""
        fname = index[name]
        fhandle = open(fname, "a" )
        fhandle.write(str(name))
        fhandle.write(" ")
        newstr = f"New Entry {name} {choice} {detail}"
        fhandle.write(newstr)

        fhandle.close()
