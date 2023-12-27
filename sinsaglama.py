import math

sayi = 10

sinus_degeri = math.sin(math.radians(sayi))

dogrulama_degeri = 0.17364817766693033

print(f"Sinüs({sayi}): {sinus_degeri}")

if math.isclose(sinus_degeri, dogrulama_degeri):
    print("Doğrulama başarılı!")
else:
    print("Doğrulama başarısız!")
