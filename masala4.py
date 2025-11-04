# Oylar lug'atini yaratamiz
oylar = {
    1: "Yanvar",
    2: "Fevral",
    3: "Mart",
    4: "Aprel",
    5: "May",
    6: "Iyun",
    7: "Iyul",
    8: "Avgust",
    9: "Sentabr",
    10: "Oktabr",
    11: "Noyabr",
    12: "Dekabr"
}

# Foydalanuvchidan oy raqamini so'raymiz
try:
    oy_raqami = int(input("Oy raqamini kiriting (1-12): "))
    
    # Oy raqami to'g'ri oraliqda ekanligini tekshiramiz
    if 1 <= oy_raqami <= 12:
        print(f"{oy_raqami}-oy: {oylar[oy_raqami]}")
    else:
        print("Xato! Iltimos 1 dan 12 gacha bo'lgan raqam kiriting.")
except ValueError:
    print("Xato! Iltimos faqat raqam kiriting.")
