def argkwargs(normal,*args, **kwargs):
# def argkwargs(normal, **kwargs):
    print(normal)
    for key in args:
        print (key)
    for key2, value  in kwargs.items():
        print ("my fav", key2,"is ",value)


args = ["akshay", "roshan","ritwik","raju","suraj"]
kwargs = {"movie":"don","song":"gazhals","actor":"abhaydeol"}

argkwargs("Wow",*args, **kwargs)
#
# argkwargs("Wow", **kwargs)