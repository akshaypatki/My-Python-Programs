directory = {"husband":"akshay", "wife":"pooja","son":"siddhu","family":{"man":"male","woman":"female"}}
print(directory ["family"]["woman"])
directory [10] = "dasara"
print(directory)
del directory["wife"]
print(directory)

dir = directory.copy()
del dir["husband"]
print(dir)