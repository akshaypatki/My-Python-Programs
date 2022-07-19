oglist = [1,2,3,4,5,6]
nwlist = list(map(lambda x : (x*x), oglist))
print(nwlist)


def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]

for i in range (101):
    bglist = list (map(lambda x:x(i),func))
    print (bglist)
