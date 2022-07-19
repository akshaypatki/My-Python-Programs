# f = open("akshay.txt")
# for line in f:
#     print (line,end="")
# f.close()
#
# f = open("akshay.txt")
# content = f.read()
# print (content)
# f.close()

# f = open("akshay.txt")
# content = f.readline()
# print (content)
# content = f.readline()
# print (content)
# content = f.readline()
# print (content)
# f.close()
f = open("akshay.txt")
print("at start", f.tell())
f.close()

f = open("akshay.txt", "a")
print(f.tell())
f.write("\nAkshay is a rockstar")
print(f.tell())

f.close()

f = open("akshay.txt")
print(f.tell())

content = f.read()
print(content)
print(f.tell())

f.close()

with open("akshay.txt") as f:
    a = f.readline()
    print(a)
