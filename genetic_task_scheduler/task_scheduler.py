import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("GA_tasks.xlsx", engine="openpyxl")
print(df.columns)
resources = df[df.columns[::2]]
times = df[df.columns[1::2]].cumsum()
print(times["T"])

fig,ax = plt.subplots()
ax.bar(resources["R"],times["T"])
plt.show()