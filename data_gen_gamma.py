# -*- coding: utf-8 -*-
"""data-gen-gamma.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vr5T8lyxr6ocLsFgfNiNCLEdBgMHV2yb
"""

import numpy as np

K = 2
n = 1000
vals = np.random.gamma(shape=K,size=n)
print(K)
a = 10
b = 16
c = 44
print(a+c+b)

import pandas as pd

df = pd.DataFrame(vals)
print(df.describe())

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(x=vals, bins=30)
plt.title('Histograma de tiempos de servicio')
plt.xlabel('Tiempos de servicio')
plt.ylabel('Frecuencia')
plt.show()

from scipy.stats import gamma
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,10,0.01)  
plt.plot(x, gamma.pdf(x, a=K))
plt.title('Función de densidad gamma(K=2)')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.show()

import statsmodels.api as sm
import scipy.stats as stats
fig = sm.qqplot(data=vals, dist=gamma, distargs=(2,), line='45')
plt.show()

import matplotlib.pyplot as plt
# histograma
count, bins, ignored = plt.hist(x=vals, bins=30, density=True)

# densidad normal(3, 0.5)
x= np.arange(1,10,0.01)
plt.plot(x, gamma.pdf(x, a=K))

plt.title('Tiempos de servicio')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.show()