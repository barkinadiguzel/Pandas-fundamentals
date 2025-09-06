import pandas as pd
import numpy as np

# -------------------------------
# 1) Create a Series
# -------------------------------
my_series = [5, 9, 13, 53]
my_index = ["A", "B", "C", "D"]
var = pd.Series(my_series, my_index)
print(var)

# -------------------------------
# 2) Create a DataFrame
# -------------------------------
my_cols = ["monday", "tuesday", "friday"]
mydata = np.random.rand(4, 3)
my_df = pd.DataFrame(mydata, my_index, my_cols)
print(my_df)

# -------------------------------
# 3) View first/last rows
# -------------------------------
print(my_df.head(2))   # Quick look at first rows
print(my_df.tail(2))   # Quick look at last rows

# -------------------------------
# 4) Dataset info & shape
# -------------------------------
print(my_df.info())    # Show columns, non-null count, types
print(my_df.shape)     # Dimensions (rows, columns)

# -------------------------------
# 5) Descriptive statistics
# -------------------------------
print(my_df['monday'].describe())

# -------------------------------
# 6) Select specific value
# -------------------------------
print(my_df.iloc[0, 2])  # Access by index position
# loc[] can be used to access by label

# -------------------------------
# 7) Value counts (frequency)
# -------------------------------
print(my_df['monday'].value_counts())  # Count unique values

# -------------------------------
# 8) Groupby + size
# -------------------------------
print(my_df.groupby('monday').size())  # Group by column and count

# -------------------------------
# 9) Apply value_counts across all columns
# -------------------------------
print(my_df.apply(pd.value_counts))


# =============================================================
# SECOND EXAMPLE WITH CUSTOM DATA
# =============================================================

# Create a DataFrame
data = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Ali", "Ayşe"],
    "yas": [20, 22, 21, 20, 22],
    "sehir": ["Ankara", "İstanbul", "İzmir", "Ankara", "İstanbul"]
}
df = pd.DataFrame(data)

# 1) First rows
print(df.head())

# 2) Last rows
print(df.tail())

# 3) Info about dataset
print(df.info())

# 4) Descriptive statistics for numerical columns
print(df.describe())

# 5) Count duplicates of entire rows
print(df.value_counts())

# 6) Count frequencies of a single column
print(df["isim"].value_counts())

# 7) Check for missing values
print(df.isnull().sum())

# 8) Fill missing values with mean
df["yas"] = df["yas"].fillna(df["yas"].mean())

# 9) Detect duplicate rows
print(df.duplicated())

# 10) Drop duplicate rows
df = df.drop_duplicates()

# 11) Add a new column
df["yas_iki_kati"] = df["yas"] * 2

# 12) Drop a column
df = df.drop("yas_iki_kati", axis=1)

# 13) Filter rows by condition
print(df[df["sehir"] == "Ankara"])

# 14) Groupby + mean
print(df.groupby("sehir")["yas"].mean())

# 15) Sort values
print(df.sort_values(by="yas", ascending=False))

# 16) Reset index
print(df.reset_index(drop=True))

# 17) String operations on columns
print(df[df["isim"].str.endswith("e")])

# 18) Apply value_counts to each column
for col in df.columns:
    print(f"Column: {col}")
    print(df[col].value_counts(), "\n")

# 19) Select rows where isim is Ali or Ayşe
print(df[df["isim"].isin(["Ali", "Ayşe"])])

# 20) Update specific values (change Ayşe's age to 23)
df.loc[df["isim"] == "Ayşe", "yas"] = 23

# 21) Drop missing values
print(df.dropna())

# 22) Fill missing values with dictionary
df.fillna({"yas": "not_entered", "sehir": "Unknown"}, inplace=True)

# 23) Groupby + sum
print(df.groupby("isim")["yas"].sum())

# 24) Save to CSV
df.to_csv("veri.csv", index=False)
