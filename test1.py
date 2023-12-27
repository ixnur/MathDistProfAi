import sympy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x, y, z = sp.symbols('x y z')

dataset_filename = "/home/nur/Masaüstü/dataset.csv"
data = pd.read_csv(dataset_filename)

for index, row in data.iterrows():
    expression_str = row['Expression']
    result = row['Result']
    expression = sp.sympify(expression_str)
    evaluated_result = expression.evalf(subs={x: 1, y: 1, z: 1})

    #if np.abs(evaluated_result - result):
        #print(f"Doğrulama başarılı - İfade: {expression_str}, Beklenen Sonuç: {result}")
    #else:
        #print(f"Doğrulama başarısız - İfade: {expression_str}, Beklenen: {result}, Bulunan: {evaluated_result}")

plt.figure(figsize=(10, 6))
plt.bar(expression_str, [1] * len(expression), color='pink', alpha=0.7, label='Doğrulama Başarısızlığı')
plt.title('Doğrulama')
plt.xlabel('Veri Seti')
plt.ylabel('Doğrulama')
plt.legend()
plt.show()