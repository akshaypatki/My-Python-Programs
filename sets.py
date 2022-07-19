s = set()
l = [1, 2, 3, 4]

s_from_list = set(l)

print(s_from_list)
print(type(s_from_list), "\n")

print(s)
print(type(s))

s.add(1)
s.add(2)
s.add(4)

print(s)

s1 = s.intersection({1, 2, 3})

print(s, s1)
print(min(s), len(s), max(s))

print(s.isdisjoint(s1))
