import pandas as pd          
import matplotlib.pyplot as plt 

df = pd.read_excel("books_full.xlsx") 

print("Successfully load Data")
print(f"Total Rows   : {df.shape[0]}")   
print(f"Total Columns: {df.shape[1]}")  

print("Data Structure")
print(df.head())          
print()
print("Column Data Types:")
print(df.dtypes)          
print()

print("Data Cleaning")
df["Price"] = df["Price"].str.replace("[^0-9.]", "", regex=True).astype(float)
print("price  is now clear (£ this sign is remove now)")

rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["Rating_Num"] = df["Rating"].map(rating_map)
print("Rating is convert into numbers( one=1,two=2)")
print()

print("Missing Values")
print(df.isnull().sum())  
print()

print("Summary Statistics")
print(df["Price"].describe())   
print()
print("Average Price per Rating:")
print(df.groupby("Rating")["Price"].mean().round(2)) 
print()

print("Hypothesis Test")
avg_by_rating = df.groupby("Rating_Num")["Price"].mean()
print("Avg Price by Rating Number:")
print(avg_by_rating.round(2))

if avg_by_rating.is_monotonic_increasing:
    print("\nResult: Hypothesis is correct,rating increase,price aslo increase" )
else:
    print("\nResult: Hypothesis is wrong, rating and price have no clear patern")
print()


fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.suptitle("Books EDA - Task 2", fontsize=16, fontweight="bold")


axes[0, 0].hist(df["Price"], bins=8, color="steelblue", edgecolor="white")
axes[0, 0].set_title("Price Distribution")
axes[0, 0].set_xlabel("Price (£)")
axes[0, 0].set_ylabel("Number of Books")


rating_order = ["One", "Two", "Three", "Four", "Five"]
rating_counts = df["Rating"].value_counts().reindex(rating_order)
axes[0, 1].bar(rating_counts.index, rating_counts.values, color="coral", edgecolor="white")
axes[0, 1].set_title("Rating Distribution")
axes[0, 1].set_xlabel("Rating")
axes[0, 1].set_ylabel("Count")

avg_price = df.groupby("Rating_Num")["Price"].mean()
axes[1, 0].plot([1, 2, 3, 4, 5], avg_price.values, marker="o", color="green", linewidth=2)
axes[1, 0].set_title("Avg Price per Rating (Hypothesis)")
axes[1, 0].set_xlabel("Rating (1=One Star, 5=Five Star)")
axes[1, 0].set_ylabel("Avg Price (£)")
axes[1, 0].set_xticks([1, 2, 3, 4, 5])

top5 = df.nlargest(5, "Price")[["Title", "Price"]]
top5["Title_Short"] = top5["Title"].str[:20]   # Title ko short karo graph ke liye
axes[1, 1].barh(top5["Title_Short"], top5["Price"], color="purple", edgecolor="white")
axes[1, 1].set_title("Top 5 Most Expensive Books")
axes[1, 1].set_xlabel("Price (£)")

plt.tight_layout()
plt.savefig("eda_result.png", dpi=130, bbox_inches="tight")  
plt.show()                                                    

print("=" * 50)
print("EDA Complete!")
print("=" * 50)