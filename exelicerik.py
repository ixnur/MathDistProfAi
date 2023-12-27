"""
import pandas as pd

dosya_adi = '/home/nur/Masaüstü/APLM IFLUX Values 1988 - 2019.xlsx'

excel_data = pd.ExcelFile(dosya_adi)

sayfa_adlari = excel_data.sheet_names

for sayfa in sayfa_adlari:
    print(sayfa)
"""
import pandas as pd
dosya_adi = '/home/nur/Masaüstü/APLM IFLUX Values 1988 - 2019.xlsx'
excel = pd.ExcelFile(dosya_adi)
sayfa = excel.sheet_names
for sayfa in sayfa:
    veri = excel.parse(sayfa)
    if not veri.empty:
        print(f"Sayfa Adı: {sayfa}")
        print("Sütun İsimleri:")
        print(veri.columns.tolist())
        print("İlk Beş Satır:")
        print(veri.head())
        print("\n" + "="*50 + "\n")
