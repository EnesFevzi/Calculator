def hesapMakinesi(a, b, islem):
    if islem not in "+-*/":
        return ("doğru düzgün bişey yaz adamın canını sıkma")

    if islem == "+":
        return (str(a) + " + " + str(b) + " = " + str(a + b))

    if islem == "-":
        return (str(a) + " - " + str(b) + " = " + str(a - b))

    if islem == "*":
        return (str(a) + " * " + str(b) + " = " + str(a * b))

    if islem == "/":
        return (str(a) + " / " + str(b) + " = " + str(a / b))


while True:
    try:
        a = int(input("ilk sayıyı giriniz"))
        b = int(input("ikinci sayıyı giriniz"))
        islem = input("+-*/ lütfen bir işlem seçiniz")
        print(hesapMakinesi(a, b, islem))

    except:
        print("Yanlış Method")