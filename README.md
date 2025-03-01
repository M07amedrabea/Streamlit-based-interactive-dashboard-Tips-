# Tips Dashboard

## Overview

This project is a **Streamlit-based interactive dashboard** that visualizes the **Tips dataset** from Seaborn. It provides various insights and visualizations to explore the relationship between different features, such as total bill, tip amount, gender, smoking status, and time of day.

## Features

- **Sidebar Controls**:

  - Categorical Filtering: Filter by `sex`, `smoker`, `day`, or `time`.
  - Numerical Filtering: Filter by `total_bill` or `tip`.
  - Row & Column Filtering for facet plots.

- **Main Metrics Display**:

  - Maximum & Minimum values for `total_bill` and `tip`.

- **Visualizations**:

  - **Scatter Plot**: `total_bill` vs `tip` with filtering options.
  - **Bar Chart**: `Sex vs Total Bill`.
  - **Pie Charts**:
    - `Smoker vs Tips`
    - `Days vs Tips`

## Requirements

Ensure you have the following Python libraries installed:

```sh
pip install streamlit pandas numpy plotly
```

## How to Run

1. Place the `tip.csv` dataset and `tip.jpg` image in the correct path.
2. Run the Streamlit app:
   ```sh
   streamlit run tips.py
   ```
3. Open the provided URL in your web browser to explore the dashboard.

## Notes

- Ensure the dataset `tip.csv` is correctly placed in the specified path.
- Modify the file path for loading the dataset if needed.
- The dashboard is designed for educational and exploratory purposes.

