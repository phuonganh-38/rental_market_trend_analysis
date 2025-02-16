-- Create raw table
CREATE TABLE public.property_data (
	address TEXT,
	suburb TEXT,
	state TEXT,
	post_code INTEGER,
	price DECIMAL,
	property_type TEXT,
	bed INTEGER,
	bath INTEGER,
	parking INTEGER	);

-- Explore the number of properties in each state
SELECT state, COUNT(*) AS total_properties
FROM public.property_data 
GROUP BY state 
ORDER BY total_properties DESC;

-- Analyze average rental prices by STATE
SELECT state, ROUND(AVG(price), 2) AS average_rent
FROM public.property_data 
GROUP BY state
ORDER BY average_rent DESC;

-- Analyze average rental prices by property type
SELECT property_type, ROUND(AVG(price), 2) AS average_rent
FROM public.property_data 
GROUP BY property_type
ORDER BY average_rent DESC;

-- Identify TOP 10 SUBURBs with the highest average rental prices
SELECT suburb, state, ROUND(AVG(price), 2) AS average_rent
FROM public.property_data
GROUP BY suburb, state
ORDER BY average_rent DESC
LIMIT 10;

-- Explore affordable family-sized properties with 3+ bedrooms and 2+ bathrooms
SELECT address, suburb, state, price, bed, bath
FROM public.property_data
WHERE bed >= 3 AND bath >= 2 AND price <= 550
ORDER BY price ASC;

-- Exploring the rental market for One-Bedroom, One-Bathroom properties
--- New South Wales
SELECT address, suburb, state, price, property_type, bed, bath, parking,
	CASE
		WHEN price < 350 THEN 'Low price'
		WHEN price BETWEEN 350 AND 600 THEN 'Medium price'
		ELSE 'High price'
	END AS price_category
FROM public.property_data
WHERE state = 'NSW' AND bed = 1 AND bath = 1
ORDER BY price ASC;

--- Victoria
SELECT address, suburb, state, price, property_type, bed, bath, parking,
	CASE
		WHEN price < 350 THEN 'Low price'
		WHEN price BETWEEN 350 AND 600 THEN 'Medium price'
		ELSE 'High price'
	END AS price_category
FROM public.property_data
WHERE state = 'VIC' AND bed = 1 AND bath = 1
ORDER BY price ASC;

--- Tasmania
SELECT address, suburb, state, price, property_type, bed, bath, parking,
	CASE
		WHEN price < 350 THEN 'Low price'
		WHEN price BETWEEN 350 AND 600 THEN 'Medium price'
		ELSE 'High price'
	END AS price_category
FROM public.property_data
WHERE state = 'TAS' AND bed = 1 AND bath = 1
ORDER BY price ASC;


