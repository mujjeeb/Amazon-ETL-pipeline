from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# The  URL of the amazon product 
URL = "https://www.amazon.com/dp/B018UQ5AMS?ref_=Oct_DLandingS_D_506cd8bf_NA"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Get the product title (Column 1)
product_title = (driver.find_element(By.ID, value='productTitle')).text

#get the product category (Column 2)
category = (driver.find_element(By.CLASS_NAME, value='a-list-item')).text

#get the price of the product (Column 3)
price_whole = (driver.find_element(By.CLASS_NAME, value='a-price-whole')).text
price_decimal = (driver.find_element(By.CLASS_NAME, value='a-price-fraction')).text
price = f"{price_whole}.{price_decimal}"

#Get the merchant name and order fulfiller (Column 4)
try:
    # Wait for the element to be visible
    merchant_element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, 'tabular-buybox'))
    )

    # Extract the text within the element
    merchant_text = merchant_element.text

except Exception as e:
    merchant_text = "CLEAN SKIN CLUB"
    print("Error:", e)



# Get Product details (Column 5)
try:
    product_details = (driver.find_element(By.ID, value='detailBulletsWrapper_feature_div')).text

except Exception as e:
    product_details  = 'N/A'
    print("Error:", e)


# Get review date and country of review (Column 6)
review_date_element = (driver.find_elements(By.CLASS_NAME, value='review-date'))
review_date_and_country_list =[]
for tag in review_date_element:
   review_date_country = tag.text
   review_date_and_country_list.append(review_date_country)
print(len(review_date_and_country_list))



#Get the review text (Column 7)
review_element = (driver.find_elements(By.CLASS_NAME, value='review-text-content'))
review_list=[]
for tag in review_element:
    review_text = tag.text
    review_list.append(review_text)
print(len(review_list))


# Get the review title (Column 8)
review_title_element = (driver.find_elements(By.CLASS_NAME, value='review-title'))
review_title_list=[]
for tag in review_title_element:
    review_title = tag.text
    review_title_list.append(review_title)
print(len(review_title_list))




# Get reviewer's name (Column 9)
reviewer_name_element = (driver.find_elements(By.CLASS_NAME, 'a-profile-name'))
unfiltered_reviewers_name_list=[]
for tag in reviewer_name_element:
    new_name = tag.text
    unfiltered_reviewers_name_list.append(new_name)

# Use list comprehension to remove empty values
reviewer_name_list = [value for value in unfiltered_reviewers_name_list if value != ""]
print(len(reviewer_name_list))


# Get the ratings for the reviews (Column 10)
rating_elements = (driver.find_elements(By.CSS_SELECTOR,"a.review-title-content > i > span.a-icon-alt"))
rating_elements_list =[]
for tag in rating_elements:
    rating_text = tag.get_attribute('innerHTML')
    rating_elements_list.append(rating_text)

foreign_rating_elements = (driver.find_elements(By.CSS_SELECTOR,"i[data-hook='cmps-review-star-rating']"))
for tag in foreign_rating_elements:
    foreign_rating_text = tag.get_attribute('innerHTML')
    rating_elements_list.append(foreign_rating_text)

print(len(rating_elements_list))

if len(rating_elements_list) == len(reviewer_name_list) == len(review_title_list) == len(review_list) == len(review_date_and_country_list):
    len_of_df = len(rating_elements_list)

else:
    print("The length's of the columns don't match")

# List out the Columns
product_title_list = [product_title] * len_of_df
category_list = [category] * len_of_df
price_list = [price] * len_of_df
merchant_text_list = [merchant_text] * len_of_df
product_details_list = [product_details] * len_of_df
review_date_and_country_list
review_list
review_title_list
reviewer_name_list
rating_elements_list
URL_list = [URL] * len_of_df


new_df = pd.DataFrame({'product_name':product_title_list , 'category': category_list, 'price': price_list, 'merchant_info':merchant_text_list, 'product_details':product_details_list, 'date_and_country_of_review':review_date_and_country_list, 'review':review_list, 'review_title':review_title_list, 'reviewer_name':reviewer_name_list, 'rating_elements': rating_elements_list, 'product_url': URL})

# Close browser window
driver.quit()

print(new_df)

# # Save file as CSV
# new_df.to_csv('amazon_raw_data.csv',index=False)

# Append to a csv file
new_df.to_csv('amazon_raw_data.csv', mode='a', header=False, index=False)

