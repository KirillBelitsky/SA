import pandas as pandas
import os
from scipy.stats import t, chi2
import numpy as np
from math import sqrt

def check_hypothesis(t):
    t_table = 1.9623415

    if t < t_table:
        print("Гипотеза верна")
    else:
        print("Гипотеза неверна")


os.chdir('/home/kirill/PythonProjects/SA')
data = pandas.read_excel('soybean-large.xlsx')

x = data.iloc[:, 9].values
y = data.iloc[:, 10].values

data = np.asarray(x)

bounds = t.interval(0.95, len(data) - 1)
mean = np.mean(data)
average_deviation = np.std(data)
print(average_deviation)
mean_interval = [mean + bound * average_deviation / sqrt(len(data)) for bound in bounds]
print('Доверительный интервал для математического ожидания:\t', mean_interval)

dispersion = np.var(data)
print(dispersion)
bounds = [chi2.ppf(0.95, len(data) - 1), chi2.ppf(0.05, len(data) - 1)]
dispersion_interval = [dispersion * len(data) / bound for bound in bounds]
print('Доверительный интервал для дисперсии:\t', dispersion_interval)

first_set = np.asarray(x)
second_set = np.asarray(y)

first_dispersion = np.var(first_set)
second_dispersion = np.var(second_set)

n = 200  # size of first selection
k = 200  # size of second selection
first_selection = first_set[0:0 + n]
second_selection = second_set[0:0 + k]
print(first_selection)
print(second_selection)

first_mean = np.mean(first_selection)
second_mean = np.mean(second_selection)

t_known = (first_mean - second_mean) / sqrt(first_dispersion / n + second_dispersion / k)

print("Для известных дисперсий: ", t_known)
check_hypothesis(t_known)

first_select_dispersion = np.var(first_selection)
second_select_dispersion = np.var(second_selection)

t_unknown = (first_mean - second_mean) / (sqrt(((n - 1) * first_select_dispersion ** 2) + (k - 1) * second_select_dispersion ** 2) /
                                          (n + k) * sqrt(1 / n + 1 / k))

print("Для неизвестных дисперсий: ", t_unknown)
check_hypothesis(t_unknown)