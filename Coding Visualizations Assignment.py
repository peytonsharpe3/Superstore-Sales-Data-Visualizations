# Exploring the dataset

# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Superstore_Sales - Superstore_Sales.csv")

# Display the number of observations (rows) and variables (columns)
print(df.shape)


#----- Creating a Line graph showing the Category Sales made by the Superstore Year on year -----

# Convert Sales to numeric
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

# Convert Order_Date to date format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create Order Year variable
df["Order_Year"] = df["Order_Date"].dt.year

# Total sales by year and category
yearly_sales = df.groupby(
    ["Order_Year", "Category"]
)["Sales"].sum().reset_index()

# Create line graph
plt.figure(figsize=(10, 6))

sns.lineplot(
    data=yearly_sales,
    x="Order_Year",
    y="Sales",
    hue="Category",
    marker="o"
)

plt.title("Superstore Category Sales Year over Year", loc="center")
plt.xlabel("Order Year")
plt.ylabel("Total Sales ($)")
plt.xticks([2014, 2015, 2016, 2017])
plt.legend(title="Category")
plt.tight_layout()
plt.show()


#----- Creating a Stacked Bar Graph showing Sales split in each Category -----

# Total sales by category and subcategory
sales = df.groupby(
    ["Category", "Sub_Category"]
)["Sales"].sum().reset_index()

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


#----- Creating a Histogram panel of Profit data for each Category -----

# Convert Profit to numeric
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

# Create histogram panel by category
g = sns.displot(
    data=df,
    x="Profit",
    col="Category",
    binwidth=50,
    height=5,
    aspect=1
)

# Set x-axis limits
g.set(xlim=(-500, 500))

# Add axis labels and titles
g.set_axis_labels("Profit ($)", "Count")
g.set_titles("{col_name}")

# Add centered title
g.figure.subplots_adjust(top=0.85)
g.figure.suptitle("Distribution of Profit by Category", x=0.5)

plt.show()

#----- Creating a pie chart showing total Sales by Region -----

# Total sales by region
region_sales = df.groupby("Region")["Sales"].sum()

# Create pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=sns.color_palette("pastel")
)

plt.title("Percentage of Total Sales by Region", loc="center")

plt.tight_layout()
plt.show()