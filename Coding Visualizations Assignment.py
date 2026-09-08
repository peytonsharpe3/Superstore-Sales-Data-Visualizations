# Exploring the dataset
# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Superstore_Sales - Superstore_Sales.csv")

# Display the number of observations (rows) and variables (columns)
print(df.shape)

#Creating a Line graph showing the Category Sales made by the Superstore Year on year.
# Convert Sales to numeric
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

# Convert Order_Date to datetime and create an Order Year variable
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Order_Year"] = df["Order_Date"].dt.year

# Group the data by year and category and calculate total sales
category_sales_year = (
    df.groupby(["Order_Year", "Category"], as_index=False)["Sales"]
      .sum()
)

# Create line graph
plt.figure(figsize=(10, 6))

sns.lineplot(
    data=category_sales_year,
    x="Order_Year",
    y="Sales",
    hue="Category",
    marker="o"
)

plt.title("Superstore Category Sales Year over Year", loc="center")
plt.xlabel("Order Year")
plt.ylabel("Total Sales ($)")
plt.xticks(sorted(category_sales_year["Order_Year"].dropna().unique()))
plt.ticklabel_format(style="plain", axis="y")
plt.legend(title="Category")
plt.tight_layout()

plt.show()