import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gasPrice = pd.read_csv('gas_prices.csv')
plt.plot(gasPrice.Year, gasPrice.Canada)
plt.show()

