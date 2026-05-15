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

# ----------------------------
# MODULE 4: CLUSTERING
# ----------------------------

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Pick columns useful for clustering
cluster_data = df_filtered[[
    "salary_in_usd",
    "company_size",
    "employment_type",
    "remote_ratio"
]].copy()

# Turn category columns into numbers
cluster_data_encoded = pd.get_dummies(cluster_data, columns=["company_size", "employment_type"], drop_first=True)

# Scale data so salary does not overpower everything
scaler = StandardScaler()
cluster_scaled = scaler.fit_transform(cluster_data_encoded)

# Test different k values
inertias = []
silhouette_scores = []
k_values = range(2, 8)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(cluster_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(cluster_scaled, labels))

# Elbow method graph
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertias, marker="o")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Entry-Level Salary Clusters")
plt.show()

# Silhouette score graph
plt.figure(figsize=(8, 5))
plt.plot(k_values, silhouette_scores, marker="o")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Scores for Different k Values")
plt.show()

# Choose k = 3 because we are comparing small, medium, and large style groups
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_filtered["cluster"] = kmeans.fit_predict(cluster_scaled)

# View cluster summary
cluster_summary = df_filtered.groupby("cluster")["salary_in_usd"].agg(["mean", "median", "count"]).round(0)
print(cluster_summary)

# ----------------------------
# MODULE 6: SUPERVISED LEARNING
# ----------------------------

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Pick features and target
model_data = df_filtered[[
    "salary_in_usd",
    "company_size",
    "employment_type",
    "remote_ratio"
]].copy()

# Turn category columns into numbers
model_data_encoded = pd.get_dummies(model_data, columns=["company_size", "employment_type"], drop_first=True)

X = model_data_encoded.drop(columns=["salary_in_usd"])
y = model_data_encoded["salary_in_usd"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict salaries
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", round(mae, 2))
print("R-squared:", round(r2, 3))

# Compare actual vs predicted
results = pd.DataFrame({
    "Actual Salary": y_test,
    "Predicted Salary": y_pred.round(0)
})

print(results.head(10))