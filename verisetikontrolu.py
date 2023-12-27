#verisetikontrolu
import pandas as pd
import sympy
import random
import matplotlib.pyplot as plt

data_file = "/home/nur/Masaüstü/dataset.csv"
dataset = pd.read_csv(data_file)

print("Veri Seti Örnekleri:")
print(dataset.head())

x, y, z = sympy.symbols('x y z')
results = []

for expression in dataset["Expression"]:
    sympy_expr = sympy.sympify(expression)
    result = sympy_expr.evalf(subs={x: random.uniform(1, 10), y: random.uniform(1, 10), z: random.uniform(1, 10)})
    results.append(result)

plt.figure(figsize=(10, 6))
plt.hist(results, bins=50, color='pink', edgecolor='black')
plt.title('İfadelerin Matematiksel Dağılımı')
plt.xlabel('İfade Sonuçları')
plt.ylabel('Frekans')
plt.show()
