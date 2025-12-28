# Real Estate Market Aggregator ETL Project

## Overview

This repository contains a lightweight ETL (Extract, Transform, Load) project that aggregates real estate listings from multiple online sources into a single, structured dataset.

The goal of the project is to practice and demonstrate core ETL concepts using real-world data, including multi-source extraction, data cleaning, schema standardization, and loading data into a relational database for analysis.

## Project Scope

### Included
- Multi-source data extraction  
- Data cleaning and normalization  
- Deduplication of listings  
- Loading into a relational database  

### Not Included
- Streaming or real-time ingestion  
- Large-scale distributed processing  
- Complex orchestration or monitoring systems  
- Cloud-native deployment  

## ETL Workflow

### 1. Extract
- Scrape real estate listings from multiple platforms  
- Collect structured and semi-structured listing data  
- Save extracted data for further processing  

### 2. Transform
- Standardize field names and formats  
- Convert prices, sizes, and counts into consistent data types  
- Remove duplicate listings across sources  
- Filter incomplete or invalid records  

### 3. Load
- Load cleaned data into a relational database  
- Create tables optimized for simple querying and analysis  

## Data Fields

The dataset includes common real estate attributes such as:

- Property ID  
- Price  
- Address and ZIP Code  
- Square Footage  
- Bedrooms and Bathrooms  
- Property Type  
- Listing Source  

## Technology Stack

- **Language:** Python  
- **Data Processing:** Pandas  
- **Database:** PostgreSQL (or equivalent)  
- **Storage:** Local filesystem  
- **Optional Tools:** Jupyter Notebooks for validation  
