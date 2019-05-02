import pandas as pd
import matplotlib.pyplot as plt

sensor_data = pd.read_csv('temperature.csv')

plt.plot(sensor_data.column_b, sensor_data.column_c)
