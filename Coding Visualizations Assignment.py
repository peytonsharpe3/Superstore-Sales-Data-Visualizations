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
# Total sales by category and subcategory
sales = df.groupby(["Category", "Sub_Category"])["Sales"].sum().reset_index()

# Sort from lowest to highest so highest sales appear on top
sales = sales.sort_values(["Category", "Sales"])

# Create pivot table
sales_pivot = sales.pivot(
    index="Category",
    columns="Sub_Category",
    values="Sales"
).fillna(0)

# Keep subcategories in sales order
order = sales["Sub_Category"].tolist()
sales_pivot = sales_pivot[order]

# Create stacked bar graph
sns.set_theme()

ax = sales_pivot.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 7),
    colormap="tab20"
)

# Label each stack with the correct subcategory
for container, subcategory in zip(ax.containers, sales_pivot.columns):
    labels = [
        subcategory if value > 0 else ""
        for value in container.datavalues
    ]
    ax.bar_label(
        container,
        labels=labels,
        label_type="center",
        fontsize=8
    )

plt.title("Sales Split by Category and Subcategory", loc="center")
plt.xlabel("Category")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=0)
plt.legend().remove()
plt.tight_layout()
plt.show()