# ETL Pipeline with SQL Database

## Overview

This project involves extracting data from Amazon product pages using Selenium, transforming and cleaning the data using Python and Pandas, and loading the processed data into a PostgreSQL database. The ETL (Extract, Transform, Load) pipeline is divided into three main steps, each implemented in a separate script or Jupyter notebook.

## Project Structure

### 1. `main.py` - Data Extraction

The `main.py` script utilizes Selenium to scrape information from an Amazon product page. Here's a brief overview of the key steps:

- **Step 1: Set Up Selenium WebDriver**
  - Import necessary Selenium modules.
  - Set up Chrome options, including the "detach" option for running Chrome in the background.
  
- **Step 2: Extract Information**
  - Retrieve the product title, category, price, merchant information, product details, review details, and ratings from the Amazon product page.
  
- **Step 3: Create DataFrame**
  - Create a Pandas DataFrame with the extracted data.
  
- **Step 4: Save to CSV**
  - Save the raw data to a CSV file (`amazon_raw_data.csv`) in append mode.

### 2. `amazon_data_reconstruction.ipynb` - Data Cleaning

The `amazon_data_reconstruction.ipynb` Jupyter notebook focuses on cleaning the raw data. Key steps include:

- **Step 1: Load Data**
  - Load the raw data from the CSV file into a Pandas DataFrame.
  
- **Step 2: Clean Product Details Column**
  - Strip unnecessary characters and clean the 'product_details' column.
  
- **Step 3: Extract Product SKU (ASIN)**
  - Identify and extract the product SKU (ASIN) from the 'product_details' column.
  
- **Step 4: Delete Rows**
  - Delete rows where 'ASIN' is not found in the 'product_details' column.
  
- **Step 5: Save Cleaned Data**
  - Save the cleaned data to a new CSV file (`cleaned_amazon_review_data.csv`).

### 3. `amazon_data_loading.ipynb` - Data Loading

The `amazon_data_loading.ipynb` Jupyter notebook focuses on loading the cleaned data into a PostgreSQL database. Key steps include:

- **Step 1: Read Cleaned Data**
  - Read the cleaned data from the CSV file into a Pandas DataFrame.
  
- **Step 2: Define Engine and Load Data**
  - Define a SQLAlchemy engine for the PostgreSQL database.
  - Load the cleaned data into the 'amazon_products_table' in the PostgreSQL database.

## Running the Pipeline

1. Execute `main.py` to extract data from the Amazon product page and save it to `amazon_raw_data.csv`.
2. Run `amazon_data_reconstruction.ipynb` to clean and preprocess the raw data, saving the result to `cleaned_amazon_review_data.csv`.
3. Execute `amazon_data_loading.ipynb` to load the cleaned data into the PostgreSQL database.

Ensure you have the necessary dependencies installed, including Selenium, Pandas, and the appropriate PostgreSQL libraries for SQLAlchemy.

The data extracted, cleaned, and loaded into a PostgreSQL database from Amazon product pages can be utilized for various purposes, including:

1. **Market Research:** Analyze product categories, prices, and customer reviews to gain insights into market trends, customer preferences, and competitor performance.

2. **Product Analytics:** Understand the popularity of specific products, their pricing strategies, and customer sentiments through ratings and reviews.

3. **Competitor Analysis:** Compare product offerings, prices, and customer feedback for similar products from different sellers.

4. **Price Monitoring:** Track changes in product prices over time, helping businesses make informed pricing decisions.

5. **Customer Sentiment Analysis:** Analyze customer reviews to understand sentiments, identify common issues or positive aspects, and improve products or services.

6. **Recommendation Systems:** Use the data to build recommendation systems, suggesting similar products based on customer preferences and behaviors.

7. **Database for Web Applications:** The PostgreSQL database can serve as a backend data source for web applications, allowing users to search and explore product information.

8. **Data Exploration and Visualization:** Explore the data visually through charts and graphs to identify patterns, trends, and outliers.

Remember to comply with Amazon's terms of service when using data scraped from their website and ensure that your use aligns with legal and ethical considerations. Additionally, consider data privacy and security aspects when handling customer reviews and other sensitive information.

Feel free to adjust the code and adapt the pipeline based on your specific use case.
