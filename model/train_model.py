import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [2, 3, 7],
    [3, 2, 10],
    [1, 4, 5],
    [4, 2, 14],
    [5, 1, 20],
    [2, 5, 5]
])
y = np.array([8, 6, 9, 4, 3, 10])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'model/study_model.pkl')
