def toplama(x,y):
    return x + y

def çıkarma(x,y):
    return x - y

def çarpma(x,y):
    return x * y

def bölme(x,y):
    return x / y

print("İşlemi seçin:")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.BÖlme")

while True:
    seçim = input("Seçimi girin(1/2/3/4):")

    if seçim in ('1','2','3','4'):
        try:
            num1 = float(input("İlk sayıyı giriniz:"))
            num2 = float(input("İkinci sayıyı giriniz:"))
        except ValueError:
            print("Yanlış giriş.Lütfen bir numara giriniz.")
            continue

        if seçim == '1':
            print(num1, "+", num2, "=", toplama(num1,num2))
        elif seçim == '2':
            print(num1, "-", num2, "=", çıkarma(num1,num2))
        elif seçim == '3':
            print(num1, "*", num2, "=", çarpma(num1,num2))
        elif seçim == '4':
            print(num1, "/", num2, "=", bölme(num1,num2))
        sonraki_hesaplama = input("Bir sonraki hesaplamayı yapalım mı? (evet,hayır)")
        if sonraki_hesaplama == "hayır":
            break
    else:
        print("Yanlış giriş.")

