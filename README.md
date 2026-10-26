# Regression Analysis -- Profit Analysis

A data analytics project that explores how startup spending relates to
profit. The project combines Python-based regression analysis with an
interactive Power BI dashboard to support business understanding and
profit estimation.

## Project Overview

The goal of this project is to analyze startup expenditure across
Research and Development (R&D), Administration, and Marketing, and study
how these expenses relate to company profit. The dataset contains **50
startup records** across **3 states**: California, Florida, and New
York.

## Objectives

-   Explore the relationship between startup spending and profit.
-   Build a Multiple Linear Regression model to estimate profit.
-   Compare profitability across states.
-   Present findings through an interactive Power BI dashboard.

## Tools and Technologies

-   **Python**
-   **Pandas** -- data handling and preparation
-   **Scikit-learn** -- Multiple Linear Regression and model evaluation
-   **Power BI** -- interactive dashboards and visual analysis
-   **Orange** -- visual machine-learning workflow, if used in the
    project workflow

## Dataset

The dataset is `startup.csv` and includes these columns:

  Column                                  Description
  --------------------------------------- ------------------------------------------
  `R&D Spend` / `RD_Spend`                Amount spent on research and development
  `Administration`                        Administrative expenditure
  `Marketing Spend` / `Marketing_Spend`   Marketing expenditure
  `State`                                 State associated with the startup record
  `Profit`                                Profit reported for the startup

The source CSV uses the column names `RD_Spend` and `Marketing_Spend`.

## Methodology

1.  **Load and inspect data** using Pandas.
2.  **Prepare features and target** by using R&D Spend, Administration,
    and Marketing Spend as input variables and Profit as the target.
3.  **Train a regression model** using Scikit-learn's
    `LinearRegression`.
4.  **Evaluate the model** using the evaluation metrics calculated in
    the Python workflow, such as MAE, MSE, and R², where available.
5.  **Visualize findings** in Power BI using state-wise profit analysis
    and spending-category comparisons.

## Power BI Dashboard

The report contains **2 dashboard pages**:

### Page 1 -- State-wise Profit Analysis

-   Compares profitability across California, Florida, and New York.
-   Helps identify differences in profit between the three states.
-   Supports further investigation of regional business performance.

### Page 2 -- Profit Analysis by Department

-   Compares spending across R&D, Administration, and Marketing.
-   Helps explore spending patterns alongside company profit.
-   Supports discussion of budget allocation and cost management.

## Key Project Highlights

-   Analyzed **50 records** across **3 states**.
-   Studied **3 spending variables** to estimate profit using Multiple
    Linear Regression.
-   Built a **2-page Power BI dashboard** for state-wise profitability
    and expenditure analysis.
-   Used data visualization and regression analysis to support
    data-driven business discussions.

## How to Run the Python Analysis

1.  Clone or download this repository.

2.  Ensure Python is installed.

3.  Install the required libraries:

    ``` bash
    pip install pandas scikit-learn matplotlib
    ```

4.  Place `startup.csv` in the project folder.

5.  Open and run the project notebook or Python script in Jupyter
    Notebook, VS Code, or your preferred Python environment.

> Update the file path and column names in your code if they differ from
> the dataset.

## Repository Structure

``` text
Regression-Analysis-Profit-Analysis/
├── startup.csv
├── Profit Analysis.pbix
├── README.md
└── analysis notebook or Python script (if included)
```

## Conclusion

This project demonstrates how regression analysis and business
intelligence dashboards can be used together to explore startup
profitability. The regression model estimates profit from spending
variables, while the Power BI report makes state-level and
spending-related patterns easier to review.

## Future Improvements

-   Report verified model performance metrics (MAE, MSE, and R²).
-   Add an Actual vs. Predicted Profit chart.
-   Investigate feature importance and regression coefficients.
-   Add interactive filters and more detailed business recommendations.

------------------------------------------------------------------------

**Project Type:** Data Analytics \| **Focus:** Regression Analysis,
Profit Analysis, Data Visualization
