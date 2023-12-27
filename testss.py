import numpy as np
import joblib
import time
simple_model_filename = "/home/nur/Masaüstü/simple_trained_model.joblib"
loaded_simple_model = joblib.load(simple_model_filename)
for i in range(1, 11):
    x_val = np.random.uniform(1, 500)  
    sin_problem = np.sin(x_val)
    cos_problem = np.cos(x_val)
    integral_problem = x_val**2
    unknown_problem = 2 * x_val - 1 
    new_data = [f"{x_val}*sin({x_val}) + {x_val}*cos({x_val}) + {x_val}**2 + 2*{x_val} - 1"]
    prediction = loaded_simple_model.predict(new_data)
    start_time = time.time()
    prediction = loaded_simple_model.predict(new_data)
    end_time = time.time()
    print(f"Problem {i} - x: {x_val:.4f}:")
    print(f"Sin Problemi - Gerçek Değer: {sin_problem:.4f}, Tahmini Değer: {prediction[0]:.4f}")
    print(f"Cos Problemi - Gerçek Değer: {cos_problem:.4f}, Tahmini Değer: {prediction[0]:.4f}")
    print(f"İntegral Problemi - Gerçek Değer: {integral_problem:.4f}, Tahmini Değer: {prediction[0]:.4f}")
    print(f"Bilinmeyenli Denklem Problemi - Gerçek Değer: {unknown_problem:.4f}, Tahmini Değer: {prediction[0]:.4f}")
    print(f"Çözme Süresi: {end_time - start_time:.6f} saniye")
    print()
