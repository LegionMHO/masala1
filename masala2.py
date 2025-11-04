
fruits = {
    'olma': 5000,
    'banan': 3000,
    'apelsin': 4000
}

def main():
    print("Mavjud mahsulotlar va narxlari (so'm):")
    for name, price in fruits.items():
        print(f" - {name}: {price}")
    total = 0
    while True:
        prod = input("Mahsulot kiriting (yoki 'exit' chiqish): ").strip().lower()
        if prod == 'exit':
            break
        if prod not in fruits:
            print("Bunday mahsulot mavjud emas. Ro'yxatni tekshiring.")
            continue
        qty_str = input("Nechta? ").strip()
        try:
            qty = int(qty_str)
            if qty <= 0:
                print("Iltimos musbat butun son kiriting.")
                continue
        except ValueError:
            print("Xato: butun son kiriting.")
            continue
        cost = fruits[prod] * qty
        total += cost
        print(f"{qty} {prod} uchun {cost} so'm qo'shildi. Jami: {total} so'm")
    print(f"Umumiy narx: {total} so'm")

if __name__ == '__main__':
    main()
