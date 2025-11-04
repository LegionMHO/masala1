n = int(input("Son kiriting: "))

for i in range(1, n + 1):
    if i % 5 != 0:  # 5 ga karrali bo'lmagan sonlarni tekshirish
        print(f"{i} ning kvadrati = {i * i}")
