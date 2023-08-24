f = open("some.txt")
c = 0
for I in f:
    print(I, end="")
    if c == 2:
        break
    c += 1
f.close()
