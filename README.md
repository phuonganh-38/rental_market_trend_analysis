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

Let's start with a quick check of dataset's shape and info:
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
Everything appeared quite great - no missing values. But is our dataset truely flawless? Are numeric values truly numeric? Are categorical values consistent?
`Price`, `Bed`, `Bath`, and `Parking` were stored as an **object** instead of a **numeric** type. This means that something is incorrect within our data. Let's explore and fix it!
<br>

**Inconsistancies in `Price`**

I found that `Price` are in various formats, including:

- Plain numeric values ($690)
- Decimals ($850.00)
- Descriptive formats ($750 pw, $750 PER WEEK, $750 Per week, $750 per week, $750 weekly)
- Incorrect typos ($4000/w)
- Comma-separated currency format ($1,150)
- Noisy entries ($650 per week!! Fully Air-conditioned Property!)

Standardizing price: The pattern \d[\d]* matches any sequence starting with a digit followed by digits or commas. It will stop matching at the first non-digit/non-comma character.

\d: match the first digit

[\d,]*: match digits and commas, keep matching as long as the characters are digits and commas




## **Environment details**
- python==3.11.5
- pandas==2.1.1
- numpy==1.24.3
- sqlite3==3.41.2
- selenium==4.21.0
