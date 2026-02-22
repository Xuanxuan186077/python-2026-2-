my_tuple = ("apple", "banana", "cherry", "date", ("elderberry", "fig", "grape"), isinstance(42, int))
a, b, c, d, e, f = my_tuple
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e[0]}, {e[1]}, {e[2]}")
print(f"f: {f}")
for index in range(len(my_tuple)):
    print(f"the item {index}: {my_tuple[index]}")
c = "i am changed"
m = c + " myself"
print(m)
m = m.replace("i", "you")
m = m.replace("am", "are")
m = m.replace("myself", "yourself")
print(m)
c = m[1]
print(c)
d = m[1:10:2]
print(d)
print(len(my_tuple))
print(len(m))