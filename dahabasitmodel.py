import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
import joblib

dataset1_filename = "/home/nur/Masaüstü/simple_dataset.csv"
dataset2_filename = "/home/nur/Masaüstü/dataset.csv"

df1 = pd.read_csv(dataset1_filename)
df2 = pd.read_csv(dataset2_filename)

df = pd.concat([df1, df2], ignore_index=True)

X = df['Expression']  
y = df['Result']  #(Result sütunu)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)
simple_model = MLPRegressor(hidden_layer_sizes=(10,), max_iter=100, random_state=22)
simple_model_pipeline = Pipeline([
    ('countvectorizer', CountVectorizer(analyzer='char', ngram_range=(1, 3))),
    ('standard_scaler', StandardScaler(with_mean=False)),
    ('simple_model', simple_model)
])

simple_model_pipeline.fit(X_train, y_train)
print(f"eğitim ok!:{X_train}")
y_pred = simple_model_pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"basit modelin test hatası (MSE): {mse}")
simple_model_filename = "simple_trained_model.joblib"
joblib.dump(simple_model_pipeline, simple_model_filename)
loaded_simple_model = joblib.load(simple_model_filename)
new_data = [""]
prediction = loaded_simple_model.predict(new_data)
print("Yüklenen modelle tahmin:", prediction)
