import numpy as np
import pandas as pandas
import os
import math
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress


def calculateStudent(a, n):
    return (a * math.sqrt(n - 2)) / math.sqrt(1 - a * a)


os.chdir('/home/kirill/PythonProjects/SA')

data = pandas.read_excel('soybean-large.xlsx')

a = data.iloc[:, 9].values
b = data.iloc[:, 10].values

_, _, r_kof, _, _ = linregress(a, b)

print(linregress(a, b))
print('Математическое ожидание: ' + str(np.mean(a)) + "; " + str(np.mean(b)))
print('Дисперсия: ' + str(np.var(a)) + "; " + str(np.var(b)))
print('СКО: ' + str(np.std(a)) + "; " + str(np.std(b)))
print('Коэффициент корреляции: ' + str(r_kof))
print('T-статистика Cтьюдента: ' + str(calculateStudent(r_kof, a.size)))
print('Теснота связи: очень слабая обратная зависимость.')

X_train, X_test, y_train, y_test = train_test_split(a, b, test_size=1/3, random_state=0)

regressor = LinearRegression()
regressor.fit(np.array(X_train).reshape((-1,1)), np.array(y_train).reshape((-1,1)))

plt.scatter(X_train, y_train, color='red')
plt.plot(np.array(X_train).reshape((-1,1)), regressor.predict(np.array(X_train).reshape((-1,1))), color='blue')
plt.title('System analysis')
plt.xlabel('Protein')
plt.ylabel('Oil')
plt.show()
