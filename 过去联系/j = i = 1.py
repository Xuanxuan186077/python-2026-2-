j = i = 1
while i <= 9:
    while j <= i:
        print(f"{j}*{i}={i*j}", end="\t")
        j += 1
    print()
    i += 1
    j = 1