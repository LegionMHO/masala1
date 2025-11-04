# Foydalanuvchidan parol so'raymiz
parol = input("Parolni kiriting: ")

# Parolni tekshirish
if len(parol) <= 6:
    print("Xato! Parol 6 ta belgidan ko'p bo'lishi kerak!")
elif "123" in parol:
    print("Xato! Parolda 123 raqamlar ketma-ketligi mavjud bo'lmasligi kerak!")
else:
    print("Parol muvaffaqiyatli qabul qilindi!")
