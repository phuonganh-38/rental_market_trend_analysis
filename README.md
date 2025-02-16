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
- `cleaned_property_data.csv`: cleaned data for analysis
- `data_cleaning.ipynb`: a Jupyter Notebook that outlines the data cleaning process
- `exploratory_data_analysis.jpynb`: a Jupyter Notebook for performing exploratory data analysis (EDA), visualizing key trends, relationships, and distributions in the data.
- `README.md`: a markdown file providing an overview of the project, including a description, project structure, and links to key files for easy navigation
- `data_cleaning.md`: a markdown file that outlines the data cleaning process
- `data_queries.md`: a markdown file that describes SQL queries to answer key business questions and generate insights
- `property_data_management_ERD.png`: Entity-Relationship Diagram (ERD) for a real estate management database
- `requirements.txt`:  a list of all Python packages required to run the project
<br>


[**How is the data cleaned?**](data_cleaning.md)

[**What does the data reveal?**](exploratory_data_analysis.ipynb)

[**How does SQL unlock Rental Market Insights?**](data_queries.md)

## **Environment details**
- python==3.11.5
- pandas==2.1.1
- numpy==1.24.3
- sqlite3==3.41.2
- selenium==4.21.0
<br>

## **References**
Domain. (2024). *The top 10 most expensive suburbs in Australia in 2024 are worth a cool $55.1 million combined*. Domain. https://www.domain.com.au/news/the-top-10-most-expensive-suburbs-in-australia-in-2024-are-worth-a-cool-55-1-million-combined-1259885/

