from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import csv
from database import create_database, insert_property

# Set up Chrome option
chrome_options = Options()

# Set uo service
service = Service('/Users/phuonganhpham/chromedriver/chromedriver')

# Set up the webdriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Create database
create_database()

# Create a list to store data
data = []

# Navigate to domain.com
for i in range (1, 51):
    driver.get(f"https://www.domain.com.au/rent/?excludedeposittaken=1&page={i}")
    WebDriverWait(driver,30).until(lambda x:x.find_element(By.CLASS_NAME,"css-1mf5g4s"))
    listings = driver.find_elements(By.CLASS_NAME,"css-1qp9106")
    
    for item in listings:
        try:
            # Extract property details
            address = item.find_element(By.XPATH,"div/div[2]/div/a/h2/span[1]").text 
            suburb = item.find_element(By.XPATH,"div/div[2]/div/a/h2/span[2]/span[1]").text
            state = item.find_element(By.XPATH,"div/div[2]/div/a/h2/span[2]/span[2]").text
            post_code = item.find_element(By.XPATH,"div/div[2]/div/a/h2/span[2]/span[3]").text
            price = item.find_element(By.CLASS_NAME,"css-mgq8yx").text
            property_type = item.find_element(By.CLASS_NAME, "css-693528").text
            
            try:
                bed = item.find_element(By.XPATH,"div/div[2]/div/div[2]/div[1]/div/span[1]/span").text
                bed = " ".join(bed.split())
            except:
                bed = "Unknown"

            try:
                bath = item.find_element(By.XPATH,"div/div[2]/div/div[2]/div[1]/div/span[2]/span").text
                bath = " ".join(bath.split())
            except:
                bath = "Unknown"
            
            try:
                parking = item.find_element(By.XPATH,"div/div[2]/div/div[2]/div[1]/div/span[3]/span").text
                parking = " ".join(parking.split())
            except: 
                parking = "Unknown"

            # Store data in list
            data.append([address, suburb, state, post_code, price, property_type, bed, bath, parking])


            # Insert property details into the database
            insert_property(address, suburb, state, post_code, price, property_type, bed, bath, parking)

        except Exception as e:
            print(f"Error processing property: {e}")

# Close the browser
driver.quit()

csv_file = 'properties.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Header 
    writer.writerow(['Address', 'Suburb', 'State', 'Post code', 'Price', 'Property type', 'Bed', 'Bath', 'Parking'])

    # Write data
    writer.writerows(data)