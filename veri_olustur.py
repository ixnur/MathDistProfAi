import numpy as np
import sympy
import random
import pandas as pd
import time

def generate(unique_data):
    x, y, z = sympy.symbols('x y z')
    expression = sympy.sympify(random.choice([
        random.randint(1, 10) * x + random.randint(1, 10) * y - random.randint(1, 10) * z,
        sympy.sin(random.uniform(1, 10) * x) * sympy.cos(random.uniform(1, 10) * y),
        sympy.exp(random.uniform(1, 10) * x) + sympy.log(random.uniform(1, 10) * y),
        sympy.sqrt(random.uniform(1, 10) * x) * sympy.cosh(random.uniform(1, 10) * y),
        random.uniform(1, 10) * sympy.atan(random.uniform(1, 10) * x) + sympy.acos(random.uniform(1, 10) * y),
        sympy.tan(random.uniform(1, 10) * x) / sympy.cot(random.uniform(1, 10) * y),
        sympy.E * sympy.log(random.uniform(1, 10) * x),
        sympy.gamma(random.uniform(1, 10) * x) - sympy.sin(y),
        sympy.atan(random.uniform(1, 10) * x) + sympy.acos(random.uniform(1, 10) * y),
        sympy.sin(random.uniform(1, 10) * x) * sympy.cos(random.uniform(1, 10) * y),
        sympy.log(random.uniform(1, 10) * x) + sympy.exp(random.uniform(1, 10) * y),
        sympy.sqrt(random.uniform(1, 10) * x) * sympy.cosh(random.uniform(1, 10) * y),
        sympy.cos(random.uniform(1, 10) * x) / sympy.tan(random.uniform(1, 10) * y),
        sympy.E * sympy.log(random.uniform(1, 10) * x) + sympy.sqrt(random.uniform(1, 10) * y),
        sympy.atan(random.uniform(1, 10) * x) * sympy.acos(random.uniform(1, 10) * y),
        sympy.sin(random.uniform(1, 10) * x) * sympy.exp(random.uniform(1, 10) * y),
        sympy.log(random.uniform(1, 10) * x) + sympy.sqrt(random.uniform(1, 10) * y),
        sympy.cos(random.uniform(1, 10) * x) * sympy.atan(random.uniform(1, 10) * y),
        sympy.gamma(random.uniform(1, 10) * x) + sympy.log(random.uniform(1, 10) * y),
    ]))
    extra = [random.uniform(1, 10), random.uniform(1, 10), random.uniform(1, 10)]
    expression += extra[0] * sympy.sin(extra[1] * x) + extra[2] * sympy.cos(extra[1] * y)
    result = expression.evalf(subs={x: random.uniform(1, 10), y: random.uniform(1, 10), z: random.uniform(1, 10)})

    while not sympy.im(result) == 0 or str(expression) in unique_data:
        expression, result = generate(unique_data)
    return expression, float(result)

def create_and_save_dataset(num_samples, filename, sleep_interval=10000, sleep_duration=1):
    X = []
    y = []
    unique_data = set()
    print("Veri seti oluşturuluyor...")

    for i in range(num_samples):
        expression, result = generate(unique_data)
        X.append(str(expression))
        y.append(result)
        unique_data.add(str(expression))

        if (i + 1) % sleep_interval == 0 and i > 0:
            print(f"{i + 1} örnek oluşturuldu. {sleep_duration} saniye bekleniyor...")
            time.sleep(sleep_duration)

    dataset = pd.DataFrame({'Expression': X, 'Result': y})
    dataset.to_csv(filename, index=False)
    print(f"Veri seti başarıyla kaydedildi: {filename}")

num_samples = 50000 
dataset_filename = "dataset.csv"
create_and_save_dataset(num_samples, dataset_filename)
