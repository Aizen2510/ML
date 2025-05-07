from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np


# Mass, Radius, Distance, Label (Yes=1.0, No=0.0)
raw_data = [
    ["5.97*10^24", 6371, 1.0, "Yes"],
    ["1.90*10^27", 69911, 5.2, "Yes"],
    ["1.00*10^22", 1188, 39.5, "Yes"],
    ["6.00*10^20", 300, 60.0, "No"],
    ["2.00*10^21", 450, 35.0, "No"],
    ["3.00*10^23", 2439, 0.39, "Yes"],
    ["1.20*10^29", 100000, 1.2, "Yes"],
    ["1.00*10^19", 200, 70.0, "No"],
    ["1.50*10^20", 350, 50.0, "No"],
    ["2.50*10^20", 320, 40.0, "No"]
]

# Chuyển mass sang float, label sang số
X_train = []
y_train = []

for row in raw_data:
    mass = float(row[0].replace('*10^', 'e'))
    radius = row[1]
    distance = row[2]
    label = 1.0 if row[3] == "Yes" else 0.0
    X_train.append([mass, radius, distance])
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

X_test = [
    [1.00e+20, 300, 10.0],  # Có khả năng là "No"
    [6.00e+24, 6400, 1.0]   # Có khả năng là "Yes"
]

# PIPELINE CHUẨN HÓA + KNN
knn_model = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('classifier', KNeighborsClassifier(n_neighbors=3, metric='minkowski', p=2))
])
# metric='minkowski' công thức khoảng cách Minkowski (tổng quát của nhiều loại khoảng cách)
# HUẤN LUYỆN + DỰ ĐOÁN
knn_model.fit(X_train, y_train)
y_pred = knn_model.predict(X_test)

# IN KẾT QUẢ
print("Dự đoán của mô hình:", y_pred)
