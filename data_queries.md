# **How does SQL unlock Rental Market Insights?**
<br>

### **Create a table to store property data**
I use **Dbeaver** as a database management tool. First, we need to create table `property_data` in schema `public`. Then import data from `cleaned_property_data.csv`
```SQL
CREATE TABLE public.property_data (
	address TEXT,
	suburb TEXT,
	state TEXT,
	post_code INTEGER,
	price DECIMAL,
	property_type TEXT,
	bed INTEGER,
	bath INTEGER,
	parking INTEGER);
```
<br>

### Exploring the number of properties in each state in the dataset
``` SQL
SELECT state, COUNT(*) AS total_properties
FROM public.property_data 
GROUP BY state 
ORDER BY total_properties DESC;
```
Result:

<img width="254" alt="image" src="https://github.com/user-attachments/assets/f5437255-1915-4d96-8925-0725a8b17d48" /> <br>
<br>

### Analyzing the average rental prices by STATE
```SQL
SELECT state, ROUND(AVG(price), 2) AS average_rent
FROM public.property_data 
GROUP BY state
ORDER BY average_rent DESC;
```
Result:

<img width="239" alt="image" src="https://github.com/user-attachments/assets/8d53fa2f-ee2c-48a4-a35e-0d635af6f4e3" /> <br>
<br>

### Identifying TOP 10 SUBURBs with the highest average rental prices?
```SQL
SELECT suburb, state, ROUND(AVG(price), 2) AS average_rent
FROM public.property_data
GROUP BY suburb, state
ORDER BY average_rent DESC
LIMIT 10;
```
Result:

<img width="359" alt="image" src="https://github.com/user-attachments/assets/c18baea0-8e7c-4fca-a0d2-c4cb94775ce2" /> <br>
<br>

### Analyzing average rental prices by property type
``` SQL
SELECT property_type, ROUND(AVG(price), 2) AS average_rent
FROM public.property_data 
GROUP BY property_type
ORDER BY average_rent DESC;
```
Result:

<img width="293" alt="image" src="https://github.com/user-attachments/assets/852605e9-1c0d-42c6-82e5-32f8b91d3603" /> <br>
<br>

### Exploring affordable family-sized properties with 3+ bedrooms and 2+ bathrooms
```SQL
SELECT address, suburb, state, price, bed, bath
FROM public.property_data
WHERE bed >= 3 AND bath >= 2 AND price <= 550
ORDER BY price ASC;
```
Result:

<img width="664" alt="image" src="https://github.com/user-attachments/assets/6e31f5f4-cb89-4956-8562-6cb8bd63be7f" /> <br>
<br>

### Exploring the rental market for One-Bedroom, One-Bathroom properties
```SQL
SELECT address, suburb, state, price, property_type, bed, bath, parking,
	CASE
		WHEN price < 350 THEN 'Low price'
		WHEN price BETWEEN 350 AND 600 THEN 'Medium price'
		ELSE 'High price'
	END AS price_category
FROM public.property_data
WHERE state = 'NSW' AND bed = 1 AND bath = 1
ORDER BY price ASC;
```
- New South Wales (NSW)
	+ Property type: the majority are Apartment/Unit/Flat.
	+ There are only 2 properties available at low prices (below $AUD350 per week). 
	+ The most expensive properties are in premium areas such as **Sydney CBD, Bondi Beach, and Barangaroo**.
	+ Highest rental price: $AUD1600 per week.

- Victoria (VIC):
	+ Properties in Victoria are predominantly **medium-priced** in the one-bedroom, one-bathroom category.
	+ Highest rental price: $AUD700 per week.

- Tasmania (TAS): The highest price is $AUD400 per week.

→ **NSW remains the most expensive state for one-bedroom, one-bathroom properties**
