import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0

data_H = [0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 75, 100, 150, 200, 250, 300, 650, 950, 1500]
data_B = [0, 0.15, 0.20, 0.25, 0.3, 0.35, 0.4, 0.45, 0.50, 0.55, 0.60, 0.65, 0.9, 1., 1.12, 1.2, 1.25, 1.3, 1.45, 1.5, 1.55]

for x, y in zip(data_H, data_B):
    plt.scatter(x, y)

p = np.polyfit(data_B, data_H, 9)

data_B_app = np.linspace(0, 1.6, 1600)
data_H_app = np.polyval(p, data_B_app)

plt.plot(data_H_app, data_B_app)
plt.xlabel("H, A/м")
plt.ylabel("B, Тл")

data_mu = list(data_B_app / data_H_app / mu_0)
max_mu = max(data_mu)
print("Максимальная мю:", max_mu)
print("Значение H:", data_H_app[data_mu.index(max_mu)])

plt.show()
