from chromosome import create_chromosome
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("GA_tasks.xlsx", engine="openpyxl")
df = df.rename(columns={"R":"R.0", "T":"T.0"})
# print(df.columns)
# resources = df[df.columns[::2]]
times = df[df.columns[1::2]].cumsum()
# print(times["T.0"])

# fig,ax = plt.subplots()
# ax.bar(resources["R.0"],times["T.0"])
# plt.show()


create_chromosome(times)