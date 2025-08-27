# Data Cleaning Showcase

**Author:** Ben Deines  
**Start date:** 2025-08-25

 # Data Cleaning Showcase

## Overview
This project demonstrates a structured approach to **data cleaning and validation**.  
The goal is to take a messy, real-world dataset and transform it into a reliable, analysis-ready dataset.  
The project highlights profiling, cleaning, and rule-based validation techniques that are crucial for data quality and analytics.

## Dataset
- Source: [UCI Adult Income Dataset](https://archive.ics.uci.edu/ml/datasets/adult)   
- Size: ~32,000 rows, 15 columns  
- Messiness includes:
  - Missing values represented as `" ?"`
  - Inconsistent categorical labels
  - Mixed data types (numeric stored as text)

## Process
The project is organized into **three Jupyter notebooks**:
1. **01_profile_raw.ipynb** – Profiling the raw dataset (shape, data types, missing values, duplicates, outliers).  
2. **02_clean_transform.ipynb** – Cleaning steps:
   - Standardizing text
   - Handling nulls and placeholders
   - Converting data types
   - Removing duplicates
3. **03_validate_qa.ipynb** – Rule-based validation:
   - Non-null checks for key fields
   - Value range checks (e.g., age between 0–120)
   - Uniqueness checks (e.g., ID fields)

## Reports
- **Data Dictionary** – definitions and valid ranges/types for each field.  
- **Issues Log** – records of profiling findings and how they were resolved.  

## Tools Used
- Python (Pandas, NumPy)
- Jupyter Notebook
- Custom helper scripts (`src/utils.py`, `src/dq_rules.py`)

## Results
- Replaced ~5% placeholder values (`" ?"`) with `NaN` and imputed where appropriate.  
- Standardized 12 categorical labels.  
- Removed ~8% duplicate rows.  
- Ensured data quality with validation rules (all checks passed).  





