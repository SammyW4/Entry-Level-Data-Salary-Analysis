import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ds_salaries.csv")
df = df.drop(columns=["Unnamed: 0"])
df.head()
df.columns

df_filtered = df[
    (df["experience_level"] == "EN") &
    (df["company_location"] == "US")
]

df_filtered.shape

salary_stats = df_filtered.groupby("company_size")["salary_in_usd"].agg(["mean", "median", "count"]).round(0)
salary_stats

df_filtered.boxplot(column="salary_in_usd", by="company_size")
plt.title("Entry-Level Salary by Company Size (US)")
plt.suptitle("")
plt.xlabel("Company Size")
plt.ylabel("Salary in USD")
plt.show()

df_filtered.isnull().sum()
df_filtered.describe()
df_filtered["company_size"].unique()

salary_stats
df_filtered.shape

print(df_filtered.head()) 
print(salary_stats)       