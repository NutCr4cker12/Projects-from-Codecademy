import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("WorldCupMatches.csv")
df[("Total Goals") = df["Home Team Goals"] + df["Away Team Goals"]]
goals = pd.read_csv("goals.csv")

print(df.head())

sns.set_Style("whitegrid")
sns.set_context("poster")

f, ax = plt.subplots(figsize=(12,7))
ax = sns.barplot(data=df,x="Year",y="Total Goals")
plt.show()
