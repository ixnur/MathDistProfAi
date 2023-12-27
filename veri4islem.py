import random
import pandas as pd
import time

def generate4islem(unique_data):
    operators = ['+', '-', '*', '/']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(operators)
    if operator == '/' and num1 % num2 != 0:
        return generate4islem(unique_data)
    
    expression = f"{num1} {operator} {num2}"
    result = eval(expression)
    while expression in unique_data or result < 0 or result % 1 != 0:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(operators)
        if operator == '/' and num1 % num2 != 0:
            continue

        expression = f"{num1} {operator} {num2}"
        result = eval(expression)

    return expression, result

def create_and_save_simple_dataset(num_samples, filename, sleep_interval=100, sleep_duration=1):
    X = []
    y = []
    unique_data = set()
    print("Basit veri seti oluşturuluyor...")

    for i in range(num_samples):
        expression, result = generate4islem(unique_data)
        X.append(expression)
        y.append(result)
        unique_data.add(expression)
        if (i + 1) % sleep_interval == 0 and i > 0:
            print(f"{i + 1} örnek oluşturuldu. {sleep_duration} saniye bekleniyor...")
            time.sleep(sleep_duration)

    dataset = pd.DataFrame({'Expression': X, 'Result': y})
    dataset.to_csv(filename, index=False)
    print(f"Basit veri seti başarıyla kaydedildi: {filename}")

num_samples_simple = 1000
simple_dataset_filename = "simple_dataset.csv"
create_and_save_simple_dataset(num_samples_simple, simple_dataset_filename)
