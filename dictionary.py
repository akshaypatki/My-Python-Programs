dictionary = {"name": "something you refer by",
              "age": "how old is someone or something",
              "notify": "bring to notice",
              "fast": "rapid speed",
              "crib": "where babies sleep",
              "bed": "where adults sleep",
              "coin": "what is money"
              }

flag = False


def mydictionary():
    query = input('search the dictionary. Enter the work and hit Enter')
    for key in dictionary.keys():
        if query == key:
            print(key, "means", dictionary[key])
            flag = True
    if flag == False:
        print("not found")


mydictionary()
