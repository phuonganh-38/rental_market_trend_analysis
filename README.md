# Rental Market Trend Analysis
---

## **Description**
This project involves scraping rental property data from [domain](https://www.domain.com.au/) website, performing data cleaning from raw data, and designing an ERD. This represents a comprehensive property management system by incorporating essential related information that cannot be directly scraped from the website, which ensures a complete and well-structured database design.
<br>

## **Project structure**
- `scraper.py`: a Python script to scrape property data from [domain](https://www.domain.com.au/) website
- `database.py`: A script to create a database to store data
- `properties.db`:  SQLite database file for storing scraped property data
- `properties.csv`: Raw property data 
- `data_cleaning_and_EDA.ipynb`: a script for cleaning data and performing EDA
- `cleaned_property_data.csv`: cleaned data for analysis
- `property_data_management_ERD.png`: Entity-Relationship Diagram (ERD) for a real estate management database
- `requirements.txt`:  a list of all Python packages required to run the project.
- `README.md`: a markdown file
<br>

## **How was the data scraped?**

<br>

## **How was the data cleaned?**
After scraping data from the web, I saved it in 2 formats: `properties.db` and `properties.csv`

Let's start with a quick check of the dataset's shape and info:
```python
df.shape
>> (996, 9)
```

```python
df.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 996 entries, 0 to 995
Data columns (total 9 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   Address        996 non-null    object
 1   Suburb         996 non-null    object
 2   State          996 non-null    object
 3   Post code      996 non-null    int64 
 4   Price          996 non-null    object
 5   Property type  996 non-null    object
 6   Bed            996 non-null    object
 7   Bath           996 non-null    object
 8   Parking        996 non-null    object
dtypes: int64(1), object(8)
```
Everything appears quite great - no missing values. But is our dataset truly flawless? Are numeric values truly numeric? Are categorical values consistent?
`Price`, `Bed`, `Bath`, and `Parking` were stored as an **object** instead of a **numeric** type. This means that something is incorrect within our data. Let's explore and fix it!
<br>

1. **Inconsistencies in `Price`**

> I found that values of `Price` are in various formats, including:
> - Plain numeric values ($690)
> - Decimals ($850.00)
> - Descriptive formats ($750 pw, $750 PER WEEK, $750 Per week, $750 per week, $750 weekly)
> - Incorrect typos ($4000/w)
> - Comma-separated currency format ($1,150)
> - Noisy entries ($650 per week!! Fully Air-conditioned Property!)
> To standardize these values, I implemented a solution: a regular expression pattern to extract numeric values while ignoring unnecessary characters.

Here is how it worked:
- `\d`: match the first digit.
- `[\d,]*`: continued matching as long as the characters were digits or commas.
- The function concatenated all matched digits, stripping out words, special characters, and symbols.

```python
def extract_numbers(price):
    if isinstance(price, str): # Ensure dtype of 'Price' is string
        match = re.search(r'\d[\d,]*', price) # Apply regex
        return int(match.group().replace(',', '')) if match else None # Remove commas and convert to integer
    return None

# Apply to column Price
df['Price'] = df['Price'].apply(extract_numbers)
```
<br>

2. **Extraneous text in numeric fields**

> This issue occurs in 3 fields (`Bed`, `Bath`, and `Parking`) when numeric values are mixed with unnecessary text (e.g: 2 Beds, 4 Parking), making it difficult to process or analyze the data numerically.
To address this issue, I extract only numeric values.

```python
def extract_count(count):
    if isinstance(count, str):
        numbers = ''.join(re.findall(r'\d+', count)) # Use regex to find
        return int(numbers) if numbers else None
    return None
```

Then, apply the function to `Bed`, `Bath`, and `Parking`

```python
df['Bed'] = df['Bed'].apply(extract_count)
df['Bath'] = df['Bath'].apply(extract_count)
df['Parking'] = df['Parking'].apply(extract_count)
```
Let's check the dtypes of `Bed`, `Bath`, and `Parking`. These values are now stored as **float** instead of **integers**. Since a property cannot have half a bedroom or bathroom, we needed to convert them into whole numbers. I also filled missing values with 0.
```python
# Handle missing values and convert values to int
df['Bed'] = df['Bed'].fillna(0).astype(int)
df['Bath'] = df['Bath'].fillna(0).astype(int)
df['Parking'] = df['Parking'].fillna(0).astype(int)
```
<br>

3. Cleaning up Address
> An issue was spotted in the `Address` column - all values ended with a trailing comma, and possibly with invisible spaces.
> To clean this up, let's strip these unnecessary characters:

```python
# Remove comma and any whitespace at the end of column "Address"
df['Address'] = df['Address'].str.rstrip(', ')
```
<br>

4. Check inconsistencies in `Suburb` and `State` names

Let's print out unique names of `Suburb` and `State`
→ There is no whitespace, all characters are uppercase.
```python
df["Suburb"].unique()
```
```python
df["State"].unique()
```
<br>

Now, let's uncover the diversity within our dataset. How many unique suburbs are represented?
```python
unique_suburb = df["Suburb"].nunique()
print(f"Number of unique suburbs: {unique_suburb}")
```
> Number of unique suburbs: 475
<br>

5. Check null values
```python
df.isnull().sum()

Address          0
Suburb           0
State            0
Post code        0
Price            2
Property type    0
Bed              0
Bath             0
Parking          0
dtype: int64
```
> Null values only appear in `Price`. One possible method would be filling them with mean values.

However, we first need to take a look at prices to explore whether our dataset contains unreasonable values.
Let's take a look at the distribution of property prices!

<img width="531" alt="image" src="https://github.com/user-attachments/assets/36cd31db-dfc9-4641-8d24-a6db0dd7c8ff" />

Some properties are listed at an unreasonably low rent — suspiciously close to zero, while there are several extremely expensive listings.

**Low rent: Errors or Hidden insights?**

In reality, finding a property at such a very low weekly rent of under $100 is almost impossible. Therefore, these listings could be errors (possibly missing digits, the sellers forget to input the rent, or they might represent parking space rentals rather than actual properties)

**High rent: Luxury properties or Anomalies?**

Let's explore deeply properties with the rent exceeding $3,000 per week:

```python
high_rent = df[df["Price"]>=3000]
```
<img width="553" alt="image" src="https://github.com/user-attachments/assets/e697bfc1-9321-4a54-a835-25e01938fad1" />
It seems that the high-rent properties are reasonable and possible. All properties in this range had 3-6 bedrooms, multiple bathrooms, and lots of parking space, making them luxury homes. Additionally, these properties were located in some of the most expensive suburbs in Australia reported by [Domain](https://www.domain.com.au/news/the-top-10-most-expensive-suburbs-in-australia-in-2024-are-worth-a-cool-55-1-million-combined-1259885/). Thus, we do not need to remove these records.


## **Environment details**
- python==3.11.5
- pandas==2.1.1
- numpy==1.24.3
- sqlite3==3.41.2
- selenium==4.21.0


## **References**
https://www.domain.com.au/news/the-top-10-most-expensive-suburbs-in-australia-in-2024-are-worth-a-cool-55-1-million-combined-1259885/
