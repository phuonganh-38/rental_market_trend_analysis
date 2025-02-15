# **How does SQL unlock Rental Market Insights?**


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
	parking INTEGER	
);
```


### **Which state has the highest rental price?**
```SQL
SELECT state, ROUND(AVG(price), 2) AS average_rent
FROM public.property_data 
GROUP BY state
ORDER BY average_rent DESC;
```
Result:

### **Which suburbs have the highest rental price?**
```SQL
SELECT suburb, state, ROUND(AVG(price), 2) AS average_rent
FROM public.property_data
GROUP BY suburb, state
ORDER BY average_rent DESC
LIMIT 10;
```

