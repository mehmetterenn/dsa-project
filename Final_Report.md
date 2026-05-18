# Final Report: Benchmarking Personal CS2 Gameplay vs. Professional Standards
*An analytical dive into the performance gap between amateur and professional esports athletes*

---

## 1. Motivation

The motivation behind this project stems from my passion for competitive gaming, specifically **Counter-Strike 2 (CS2)**. As an avid player, I often wonder how my in-game decision-making and mechanical skills compare to those of professional esports athletes. 

In CS2, success is not just about raw aim; it involves intricate economy management, utility usage (grenades), and entry fragging success. By conducting this project, my goal is to quantitatively analyze the performance gap between a casual/amateur player (myself) and the top-tier professionals. 

> *"This analysis not only satisfies personal curiosity but also serves as a practical application of data science methodologies—spanning data extraction, statistical hypothesis testing, and machine learning classification—to a domain I am deeply interested in."*

---

## 2. Data Source

To conduct this benchmarking study, I utilized a two-pronged data collection approach:

| Dataset | Source Method | Description |
| :--- | :--- | :--- |
| **Personal Data** | **Steam Web API** | Match statistics retrieved directly using my unique Steam ID. Extracted **55 matches (~1,100 rounds)** mapping out mechanical and tactical metrics. |
| **Professional Data** | **Esports DBs (HLTV)** | The benchmark dataset was aggregated by scraping publicly available match statistics representing the top 50 HLTV players. Encompasses **100 matches (~2,000 rounds)**. |

*Both datasets were processed to round-by-round granularity and exported as CSV files (`personal_cs2_data.csv` and `professional_cs2_data.csv`) for subsequent analysis.*

---

## 3. Data Analysis

The analysis pipeline was meticulously divided into four distinct stages:

1. **Data Preprocessing & Cleaning:** Merged and cleaned datasets using `pandas`. Categorical variables like `Economy_State` were encoded, and a unified target variable `Player_Level` was defined.
2. **Exploratory Data Analysis (EDA):** Generated visualizations using `matplotlib` and `seaborn` to observe underlying distributions, comparing average Utility Damage, Economy States, and Win Rates.
3. **Statistical Hypothesis Testing:** Formal tests using `scipy.stats` to confirm observations:
   - *T-Test* for Headshot Precision and Entry Duel Success.
   - *Point-Biserial Correlation* for the relationship between Utility Damage and Win Rate.
   - *Proportion Tests* for Economy Management success.
4. **Machine Learning Pipeline:** Implemented predictive models (`Logistic Regression`, `Random Forest`, and `XGBoost`) using `scikit-learn` to predict the `Player_Level`. To prevent overfitting and ensure robust generalization, models were optimized using **5-fold Cross-Validation** alongside hyperparameter tuning (e.g., configuring `n_estimators` and `max_depth` for tree-based models).

---

## 4. Key Findings

The project yielded several critical insights into what separates a casual player from a professional:

> **IMPORTANT: Mechanical Precision (Aim)**  
> Hypothesis testing revealed a statistically significant difference in Headshot percentages. Professional players maintain a vastly higher and more consistent headshot rate ($t = -5.81, p < 0.0001$).

> **TIP: Utility Utilization (Brains)**  
> Professionals deal significantly higher average 'Utility Damage' per round (approx. 28 vs. 13). Rounds with higher utility damage strongly correlated with higher win probabilities across both datasets ($p < 0.001$).
> 
> ![Utility Damage Boxplot](eda_utility_damage.png)
> *Figure 1: Boxplot demonstrating the stark contrast in utility damage output per round.*

> **WARNING: Economy Discipline**  
> Professionals have a much stricter economy management approach, winning significantly more 'Eco' (low economy) rounds compared to personal gameplay ($p = 0.026$) due to superior team coordination.

> **NOTE: Predictive Modeling Success**  
> The `Random Forest` and `XGBoost` classifiers achieved **~76% accuracy** and a strong **0.82 F1-Score** for predicting the Professional class. **Utility Damage** and **Economy State** were the most critical predictors extracted from the Feature Importance analysis, proving CS2 is predominantly a tactical game.

---

## 5. Limitations and Future Work

While the project successfully established a comparative benchmark, there are a few limitations to acknowledge:

- **Data Volume:** The personal dataset is limited to a smaller sample size (55 matches). A larger timeline would yield more robust trends.
- **Lack of Positional Data:** The current dataset relies on scoreboard metrics. It does not account for X,Y coordinate positioning or crosshair placement.
- **Role Specificity:** The analysis generalizes all professionals into one group without distinguishing their tactical roles (e.g., AWPer, Support, Entry).

### Future Extensions
Future iterations could involve **scraping 2D radar parsing** from `.dem` (demo) files to visualize player heatmaps and grenade trajectories. Additionally, deploying the trained Machine Learning model via a web application (e.g., Streamlit or Flask) where users can upload their own Steam stats would be a highly interactive extension.
