import pandas as pd

def check_dataset(filename):
    df = pd.read_csv(filename)
    errors = 0
    for index, row in df.iterrows():
        expression = row['Expression']
        result = row['Result']
        try:
            if eval(expression) != result:
                print(f"Hata: İfade: {expression}, Beklenen Sonuç: {result}, Gerçek Sonuç: {eval(expression)}")
                errors += 1
        except Exception as e:
            print(f"Hata: İfade: {expression}, Hata Mesajı: {str(e)}")
            errors += 1
    if errors == 0:
        print("Veri seti doğru.")
    else:
        print(f"{errors} hata bulundu.")

dataset_filename = "simple_dataset.csv"
check_dataset(dataset_filename)
