import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd
import numpy as np

x, y, z = sp.symbols('x y z')

dataset_filename = "Masaüstü/dataset.csv"
data = pd.read_csv(dataset_filename)

failures = []

for index, row in data.iterrows():
    expression_str = row['Expression']
    result = row['Result']
    expression = sp.sympify(expression_str)
    evaluated_result = expression.evalf(subs={x: 1, y: 1, z: 1})
    if np.abs(evaluated_result - result) > 0:
        print(f"Doğrulama başarısız - İfade: {expression_str}, Beklenen: {result}, Bulunan: {evaluated_result}")
        failures.append(index)

plt.figure(figsize=(10, 6))
plt.bar(failures, [1] * len(failures), color='red', alpha=0.7, label='Doğrulama Başarısızlığı')
plt.title('Doğrulama Başarısızlıkları')
plt.xlabel('Veri Seti İndeksi')
plt.ylabel('Doğrulama Başarısızlığı')
plt.legend()
plt.show()
