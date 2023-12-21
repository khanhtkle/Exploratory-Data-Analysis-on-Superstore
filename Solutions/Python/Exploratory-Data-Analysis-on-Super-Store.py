# Analyzing Superstore: Uncovering Insights through Data Exploration

# Introduction
 
# Superstore is a little shop in Canada that sells furniture, office supplies, and technology products to regular consumers, businesses, and home offices. The information we have includes details about sales, profits, and the location of each order. 

# Our goal is to find out where Superstore can improve and identify chances for the business to grow.
 
# Business Questions

# - Which Category is Best Selling and Most Profitable?
# - What are the Best Selling and Most Profitable Sub-Category?
# - Which is the Top Selling Sub-Category?
# - Which Customer Segment is Most Profitable?
# - Which is the Preferred Ship Mode?
# - Which Region is the Most Profitable?
# - Which City has the Highest Number of Sales?
 
# Who is Reading this Analysis?

# - We assume Superstore is a family business with 1 or 2 owners really into it. These owners might not be great at reading charts or complex stats, so we will keep our analysis simple.

# - Our goal is to give the owners easy-to-understand info to help them make smart choices for boosting business money. We will focus on finding where things can get better and suggest ideas and ways to sell more.

# ---
# Preparing the Environment
 
# We will import the necessary libraries and load the data set.
 
# - Pandas - Data manipulation
# - Matplotlib and Seaborn - Data visualisation

# Import libraries and create aliases
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
get_ipython().run_line_magic('matplotlib', 'inline')

# Load the data in CSV format
superstore = pd.read_csv('SampleSuperstore.csv')

# ---
# Data Exploration

# Let's examine the data by using the df.head() and df.tail() functions.

# First 5 rows of the dataset
superstore.head()

# Last 5 rows of the dataset
superstore.tail()

# It's apparent that we have a mix of categorical, geographical, and numerical variables in the dataset.

# Each row signifies an order for an item, including details like quantity, sales, discount, and profit. Additionally, information about the shipment mode, customer segment, and geographical aspects is provided.

# For further insights, we'll utilize df.shape() and df.info().

# Size of the dataset
superstore.shape

# Overview of dataset information
superstore.info()

# The dataset consists of 9,994 rows, including the header, and comprises 13 columns. The data types are accurate and align with their respective values.

# ---- 
# Data Cleaning

# Before delving into the analysis, it's crucial to clean the data or "scrub the dirt." 

# In this analysis, we'll address common issues like missing and duplicate data.

# Handling Missing Values

# Our initial step is to identify whether there are any null values in the dataset.

# Determine the number of null values for each column
superstore.isnull().sum()

# The result indicates that the dataset doesn't contain any null values.

# Duplicate Data

# Next, we'll investigate whether there is any duplicated data in the dataset.

# Determine the number of duplicate rows
superstore.duplicated().sum()

# There are 17 rows with duplicated values. Let's execute another function to inspect these duplicated data.

# Display the duplicated rows
superstore[superstore.duplicated(keep = 'last')]

# Next, we'll use the drop_duplicates() function to eliminate the duplicated rows.

# Remove duplicated rows
superstore.drop_duplicates(inplace = True)

# Determine the number of rows and columns
superstore.shape

# With the removal of duplicated rows, the dataset now consists of 9977 rows instead of the original 9993.

# Calculated Field

# Moving forward, let's create a calculated field for Profit Margin using the formula (Profit \ Sales) * 100.

#  Calculate and add Profit Margin
superstore['Profit Margin %'] = (superstore.Profit / superstore.Sales) * 100
superstore.head(5)

# Now that the dataset has been cleaned, let's proceed with some statistical analysis!

# ---
# Descriptive Statistics

# For a comprehensive descriptive statistical analysis, we'll use df.describe() and set 'include = 'all' to gain insights into the data's spread, central location, and any potential outliers

# Display a statistic overview for the dataset
superstore.describe(include = 'all')

# You may observe 'NaN' values in certain categorical columns, and that's completely acceptable. Categorical values are not intended for calculations, so we can disregard them.

# Our attention is directed towards understanding the unique count and frequency of categorical features. For instance:

# - There are 4 ship modes and 3 customer segments. Nearly half of the orders are from Consumer segment using Standard Class shipment.

# - The store carries 3 category of items with 17 sub-category. 60% of orders are for Office Supplies and at least 15% purchases are for Binders.

# Turning to numerical parameters, it's noteworthy that:

# - 75% of orders makes at least 36% profit margin.
# - Loss-making orders can go up to 275% losses. We must place emphasis on these loss-making sales to cut them off.

# We'll proceed with more analyses below to assess these observations.

# ---
# Exploratory Data Analysis

# 1. Which Category is Best Selling and Most Profitable?

# Identifying "Best Selling" involves examining sales, while "Most Profitable" pertains specifically to profit. To aggregate total values of sales, profit, and quantity for each category, we'll use the df.groupby().sum() function.

# Summerize sales, profit, and quantity by category
category_analysis = pd.DataFrame(superstore.groupby(['Category'])[['Sales', 'Profit', 'Quantity']].sum())
category_analysis

#Customize plots: whitegrid theme, 1x3 subplot grid, 8x5 figure
sns.set_theme(style = 'whitegrid')
figure, axis = plt.subplots(1, 3, figsize = (8, 5))

# Create barplots
cat1 = sns.barplot(x = category_analysis.index, y = category_analysis.Sales, ax = axis[0])
cat2 = sns.barplot(x = category_analysis.index, y = category_analysis.Profit, ax = axis[1])
cat3 = sns.barplot(x = category_analysis.index, y = category_analysis.Quantity, ax = axis[2])

# Set titles
cat1.set(title = 'Sales')
cat2.set(title = 'Profit')
cat3.set(title = 'Quantity')

# Rotate x - axis labels, set font size
plt.setp(cat1.get_xticklabels(), rotation = 'vertical', size = 9)
plt.setp(cat2.get_xticklabels(), rotation = 'vertical', size = 9)
plt.setp(cat3.get_xticklabels(), rotation = 'vertical', size = 9)

# Adjust subplot spacing
figure.tight_layout()

# Key findings include:

# - Furniture, Office Supplies, and Technology all show similar sales figures.
 
# - Technology stands out as the Best Selling category and is notably the Most Profitable as well. Despite its minimal sales volume, this category represents one-off purchases with an extended lifespan of at least 4-5 years.
 
# - While Furniture matches Technology in sales, it ranks as the least profitable, with minimal quantities sold.
 
# - Office Supplies takes the lead in terms of quantity sold, thanks to its relatively affordable nature.
 
# 2. What are the Best Selling and Most Profitable Sub-Category?

# Summerize sales and profit by sub-category
subcat_analysis = pd.DataFrame(superstore.groupby(['Sub-Category'])[['Sales', 'Profit']].sum())

# Sort in descending order based on sales
subcat_sales = pd.DataFrame(subcat_analysis.sort_values('Sales', ascending = False))
subcat_sales

# Sort in descending order based on profit
subcat_profit = pd.DataFrame(subcat_analysis.sort_values('Profit', ascending = False))
subcat_profit

# Customize plots: whitegrid theme, 1x2 subplot grid, 12x6 figure
sns.set_theme(style = 'whitegrid')
figure, axis = plt.subplots(1, 2, figsize = (12, 6))

# Create bar plot for Best Selling Sub-Category
subcat1 = sns.barplot(data = subcat_sales, x = subcat_sales.index, y = subcat_sales.Sales, ax = axis[0])
subcat1.set(title = "Best Selling Sub-Category")
subcat1.set_xticklabels(subcat1.get_xticklabels(),rotation = 'vertical', size = 10)

# Create bar plot for Most Profitable Sub-Category
subcat2 = sns.barplot(data = subcat_profit, x = subcat_profit.index, y = subcat_profit.Profit, ax = axis[1])
subcat2.set(title = "Most Profitable Sub-Category")
subcat2.set_xticklabels(subcat2.get_xticklabels(),rotation = 'vertical', size = 10)

# Adjust subplot spacing
figure.tight_layout()
plt.show()

# Key findings include:

# - Phones and Chairs emerge as the top two best-selling sub-categories.

# - Copiers generate the highest profit, followed by Phones, Accessories, Papers, and Binders. Crafting an effective marketing strategy should prioritize these products.
 
# - Conversely, Machines, Fasteners, Supplies, Bookcases, and Tables exhibit marginal to negative margins. Considerations for the Superstore could involve discontinuing these products, adjusting sale prices, optimizing profit margins, or negotiating lower costs with suppliers.

# 3. Which is the Top Selling Sub-Category?

# Summarize quantity by sub-category
subcat_quantity = pd.DataFrame(superstore.groupby(['Sub-Category'])[['Quantity']].sum())

# Sort in descending order of sales
subcat_quantity = pd.DataFrame(subcat_quantity.sort_values('Quantity',ascending = False))
subcat_quantity

# Create bar plot for Top Selling Sub-Category
sns.set_theme(style = 'whitegrid')
sns.barplot(data = subcat_quantity, y = subcat_quantity.index, x = subcat_quantity.Quantity, palette = 'muted')
plt.title("Top Selling Sub-Category")
plt.show()

# Key findings include:

# - It's crucial for Superstore to maintain consistently well-stocked inventory for the top-selling sub-categories like Binders, Paper, Furnishings, and Phones.

# - Despite being the most profitable, Copiers have a lower sales volume, totaling only 234. Given their higher price and the fact that they are typically utilized for several years, it's reasonable that they have a lower sales frequency compared to other products.
 
# 4. Which Customer Segment is Most Profitable?

# Summarize profit by customer segment
segment_analysis = pd.DataFrame(superstore.groupby(['Segment'])[['Profit']].sum())
segment_analysis

# Create bar plot for Most Profitable Customer Segment
sns.set_theme(style = 'whitegrid')
sns.barplot(data = segment_analysis, x = segment_analysis.index, y = segment_analysis.Profit, palette = 'rocket')
plt.title("Customer Segment Profitability")

plt.show()

# The Consumer segment stands out as the most profitable, followed by the Corporate Segment and Home Office. Consequently, the marketing strategy should prioritize efforts on retaining Consumer and Corporate Segment customers.
 
# 5. Which is the Preferred Ship Mode?

# Create bar plot for Preferred Ship Mode
sns.set_theme(style = 'whitegrid')
sns.countplot(data = superstore, x = 'Ship Mode')
plt.title("Ship Mode")
plt.show()

# Standard Class overwhelmingly emerges as the preferred and potentially the most cost-effective shipment method. The other modes appear less favored among customers, possibly due to higher associated costs.
 
# 6. Which Region is the Most Profitable?

# Summarize profit by region
region_analysis = pd.DataFrame(superstore.groupby(['Region'])['Profit'].sum().reset_index())
region_analysis

# Create pie chart for Most Profitable Region
explode = [0, 0.04, 0, 0.04]
plt.pie(region_analysis.Profit, labels = region_analysis.Region, startangle = 90, autopct = "%1.0f%%", explode = explode)
plt.title("Most Profitable by Region")
plt.show()

# The East and West regions demonstrate the highest profitability.
 
# 7. Which City has the Highest Number of Sales?

# Summarize sales and quantity by city
city_sales = pd.DataFrame(superstore.groupby(['City'])[['Sales', 'Quantity']].sum())

# Sort in descending order of sales                          
city_sales = pd.DataFrame(city_sales.sort_values('Sales', ascending = False))

# Identify the top 10 cities with the highest sales                        
top10 = city_sales[:10]
top10

# Identify the top 10 cities with the lowest sales   
bottom10 = city_sales[-10:]
bottom10

# Customize plots: whitegrid theme, 1x2 subplot grid, 12x5 figure
sns.set_theme(style = 'whitegrid')
figure, axis = plt.subplots(1, 2, figsize = (12, 5))

# Create bar plot for Best Selling Sub-Category
top10c = sns.barplot(data = top10, y = top10.index, x = top10.Sales, palette = 'coolwarm', ax = axis[0])
top10c.set(title = "Top 10 Cities with Highest Sales")
top10c.set_yticklabels(top10c.get_yticklabels(), size = 10)

# Create bar plot for Worst Selling Sub-Category
bottom10c = sns.barplot(data = bottom10, y = bottom10.index, x = bottom10.Sales, palette = 'coolwarm', ax = axis[1])
bottom10c.set(title = "Top 10 Cities with Lowest Sales")
bottom10c.set_yticklabels(bottom10c.get_yticklabels(), size = 10)

# Adjust subplot spacing
figure.tight_layout()
plt.show()

# A notable discrepancy exists between cities with the highest and lowest sales. To optimize marketing efforts, it is crucial to concentrate on the top 10 cities.
 
# --- 
# Strategic Recommendation

# In this final segment, we revisit our initial business inquiries and present our comprehensive business recommendations.
 
# Business Questions

# - Which Category is Best Selling and Most Profitable?
# - What are the Best Selling and Most Profitable Sub-Category?
# - Which is the Top Selling Sub-Category?
# - Which Customer Segment is Most Profitable?
# - Which is the Preferred Ship Mode?
# - Which Region is the Most Profitable?

# Recommendations

# - Prioritize the Technology sub-category, emphasizing high-selling and profitable items like Phones and Chairs. Consider bundling them with less profitable products such as Bookcases, Tables, and Chairs to balance losses.
 
# - Due to significant losses from Bookcases and Tables, explore bundling options with high-selling or profitable sub-categories like Chairs, Copiers, Phones, and Office Supplies. This strategy aims to mitigate losses and enhance overall profitability.
 
# - Recognize the potential time constraints of Home Office customers. Introduce a Home Office package containing essential office products like tables, chairs, phones, copiers, storage solutions, labels, fasteners, and bookcases for a convenient one-stop solution.
 
# - Evaluate the viability of loss-making products like Supplies, Bookcases, and Tables. Options include either removing them from the catalogue or renegotiating with suppliers for more cost-effective solutions.
 
# - Target the Consumer and Corporate Segments, which collectively account for over 70% of the customer base. Focus efforts on customers in the East and West regions within the Top 10 cities with the highest sales. Introduce special promotions and bundles for mass consumers and home offices, complemented by promotional emails or flyers to maximize impact.
