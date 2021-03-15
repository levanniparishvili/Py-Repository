print("Hello")
print('My first pull request')


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import urllib.request

plt.xkcd()


x_axis = [22, 23, 24, 25, 26, 27, 28, 29, 30]
y_axis = [2000, 2500, 2600, 2650, 3000, 3100, 3500, 4000, 6000]
dev_y_axis = [2500, 2800, 3600, 3650, 4000, 4100, 4500, 5000, 8000]

plt.plot(x_axis, y_axis, label='All Devs')
plt.plot(x_axis, dev_y_axis, 'k--', label='Python')
plt.xlabel('Ages')
plt.ylabel('Salary')
plt.title('Median Salary by Age')

plt.tight_layout()

plt.show()