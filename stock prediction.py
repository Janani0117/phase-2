# 📦 Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🧮 Set visualization style
sns.set(style="darkgrid")
plt.rcParams["figure.figsize"] = (12, 6)

# 📁 Load the dataset
df = pd.read_csv('Microsoft Stock Data.csv')  # Update path if needed

# 📌 Preview the data
print("First 5 rows:")
print(df.head())

# 🧼 Data Cleaning
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df = df.sort_index()

# 🔍 Basic Info
print("\nData Summary:")
print(df.describe())
print("\nMissing values:")
print(df.isnull().sum())

# 📊 Plot Closing Price over Time
plt.plot(df['Close'], label='Close Price')
plt.title("Microsoft (MSFT) Stock Closing Price Over Time")
plt.xlabel("Year")
plt.ylabel("Closing Price (USD)")
plt.legend()
plt.show()

# 📉 Moving Averages (50-day and 200-day)
df['MA50'] = df['Close'].rolling(window=50).mean()
df['MA200'] = df['Close'].rolling(window=200).mean()

# 📈 Plot with Moving Averages
plt.plot(df['Close'], label='Close Price', alpha=0.5)
plt.plot(df['MA50'], label='50-Day MA', color='orange')
plt.plot(df['MA200'], label='200-Day MA', color='red')
plt.title("MSFT Close Price with Moving Averages")
plt.xlabel("Year")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

# 🔁 Volume Analysis
sns.lineplot(data=df, x=df.index, y='Volume')
plt.title("Microsoft Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()
