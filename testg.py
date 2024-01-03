import pandas as pd
import sympy

data_file = "dataset.csv"
dataset = pd.read_csv(data_file)
x, y, z = sympy.symbols('x y z')
for index, row in dataset.iterrows():
    expression = row["Expression"]
    sympy_expr = sympy.sympify(expression)
    
    random_values = {x: random.uniform(1, 10), y: random.uniform(1, 10), z: random.uniform(1, 10)}
    
    result = sympy_expr.evalf(subs=random_values)
    
    print(f"İfade {index + 1}: {expression} -> Sonuç: {result}")
