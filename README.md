# DSA 210: Benchmarking Personal CS2 Gameplay vs. Professional Standards

## Project Motivation
This project aims to analyze the performance gap between my personal Counter-Strike 2 gameplay and professional benchmarks. Using data extracted from the Steam Web API and simulated parameters, we compare key metrics like Headshot (HS) ratios, utility efficiency, and eco-round success.

## Repository Contents
- `data_collection.py`: Script to connect to the Steam API and fetch/generate the CS2 matched player records.
- `eda_hypothesis.py`: Conducts Exploratory Data Analysis (EDA) and calculates 4 key hypothesis tests using the extracted CSV files.
- `personal_cs2_data.csv`: The extracted dataset containing personal matches and rounds.
- `professional_cs2_data.csv`: The extracted enrichment dataset for professional standards.
- `requirements.txt`: Python package dependencies.
- `*.png`: EDA Visualizations output.

## How to Reproduce the Analysis

1. **Install Dependencies:**
   First, ensure you have Python 3 installed. Then install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. **Step 1: Data Collection:**
   Run the data collection script to pull the data via the Steam Web engine and generate the exact datasets.
   ```bash
   python data_collection.py
   ```
   *Note: This will output `personal_cs2_data.csv` and `professional_cs2_data.csv` to your current directory.*

3. **Step 2: EDA & Hypothesis Testing:**
   Run the analysis script to output the statistics and generate new P-values.
   ```bash
   python eda_hypothesis.py
   ```
   *Check your console for the direct hypothesis test outputs and the directory for the generated `.png` graphs.*
