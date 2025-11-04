n = int(input("Son kiriting (n): "))

if n < 1:
    print("n kamida 1 bo'lishi kerak.")
else:
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            continue
        s += i
    print(f"1 dan {n} gacha juft sonlar yig'indisi = {s}")