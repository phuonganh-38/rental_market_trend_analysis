# **How does SQL unlock Rental Market Insights?**
<br>

### **Create a table to store property data**
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

### **How many properties count for each state in the dataset?**
``` SQL
SELECT state, COUNT(*) AS total_properties
FROM public.property_data 
GROUP BY state 
ORDER BY total_properties DESC;
```

<img width="254" alt="image" src="https://github.com/user-attachments/assets/f5437255-1915-4d96-8925-0725a8b17d48" />


### **Which state has the highest rental price?**
```SQL
SELECT state, ROUND(AVG(price), 2) AS average_rent
FROM public.property_data 
GROUP BY state
ORDER BY average_rent DESC;
```
Result:

<img width="239" alt="image" src="https://github.com/user-attachments/assets/8d53fa2f-ee2c-48a4-a35e-0d635af6f4e3" /> <br>
<br>

### **Which suburbs have the highest rental price?**
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

``` SQL
SELECT property_type, ROUND(AVG(price), 2) AS average_rent
FROM public.property_data 
GROUP BY property_type
ORDER BY average_rent DESC;
```
Result:

<img width="291" alt="image" src="https://github.com/user-attachments/assets/7fbbfe29-7ff9-4132-ba44-ed9d91b34b02" />



```SQL
SELECT address, suburb, state, price, bed, bath
FROM public.property_data
WHERE bed >= 3 AND bath >= 2 AND price <= 550
ORDER BY price ASC;
```
Result:

<img width="664" alt="image" src="https://github.com/user-attachments/assets/6e31f5f4-cb89-4956-8562-6cb8bd63be7f" />


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
almost is Apartment/Unit/Flat
there are only 2 property (<350) 
most expensive property: sydney cbd, bondi beach and barangagoo
The most expensive property is at Barangaroo ~ 1600pw

VIC: almost medium price, the highest price for a one-bedroom and one-bathroom property is $700
TAS: the highest price for a one-bedroom and one-bathroom property is $400
