import pandas as pd

def removezerosdot(filename):
    df = pd.read_csv(filename)

    df['Result'] = df['Result'].apply(lambda x: int(x) if x.is_integer() else x)

    df.to_csv(filename, index=False)
    print(f"Trailing zeros başarıyla kaldırıldı ve dosya güncellendi: {filename}")

dataset_filename = "simple_dataset.csv"
removezerosdot(dataset_filename)
