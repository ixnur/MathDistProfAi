"""
import math

for x in range(1, 21):
    sinus_degeri = math.sin(x)
    print(f"{x}: {sinus_degeri}")
"""

import math

sayi = 10  # İstediğiniz sayıyı buraya yazın
sinus_degeri = math.sin(math.radians(sayi))

print(f"Sinüs({sayi}): {sinus_degeri}")
