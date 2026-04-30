# Entry-Level Data Salary Analysis

## Project Overview
This project analyzes whether larger companies pay more for entry-level data jobs in the United States.

As someone preparing to enter the data field, I wanted to see if company size affects salary for entry-level roles. The goal was to use salary data to help students and early-career job seekers make more informed decisions about where to apply.

## Research Question
Do larger companies pay more for entry-level data jobs in the U.S.?

## Dataset
The dataset used was `ds_salaries.csv`, which contains data science salary information.

For this analysis, I focused on:

- `experience_level`
- `salary_in_usd`
- `company_size`
- `company_location`
- `job_title`

The data was filtered to only include:
- Entry-level roles (`experience_level = EN`)
- U.S.-based companies (`company_location = US`)

After filtering, the dataset contained 31 entry-level U.S. positions.

## Tools Used
- Python
- pandas
- matplotlib

## What I Did
1. Loaded the salary dataset using pandas
2. Removed an unnecessary index column
3. Filtered the data to focus on entry-level U.S. roles
4. Grouped salaries by company size
5. Calculated mean, median, and count for each company size
6. Created a boxplot to compare salary distributions
7. Checked for missing values and reviewed summary statistics

## Key Findings
Large companies appeared to have the highest average salary, but the median salary was much closer to smaller companies.

This suggests that a few high-paying roles may raise the average salary for large companies. Because salaries can be skewed by outliers, the median gives a better idea of what a typical entry-level worker might expect.

Overall, company size alone does not guarantee much higher pay.

## Why This Matters
For students and entry-level job seekers, this analysis shows that smaller companies can still offer competitive pay. Salary is important, but company size should not be the only factor when deciding where to apply.

Other factors like role responsibilities, growth opportunities, benefits, and work environment should also be considered.

## Limitations
- The filtered dataset only had 31 entry-level U.S. roles
- Cost of living was not included
- Bonuses, equity, and benefits were not included
- Entry-level roles may vary by company
- The dataset may not represent every industry

## Files in This Repository
- `ds_salaries.csv` — salary dataset
- `salary_analysis.py` — Python code for analysis
- `README.md` — project explanation

## Medium Post
I also wrote a Medium post explaining this analysis in a more detailed way:

[Do Larger Companies Pay More for Entry-Level Data Jobs?](https://medium.com/inst414-data-science-tech/do-larger-companies-pay-more-for-entry-level-data-jobs-7ff8e6bd4bc2)
