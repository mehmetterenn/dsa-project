import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

def run_pipeline():
    # Load data
    try:
        personal_df = pd.read_csv('personal_cs2_data.csv')
        pro_df = pd.read_csv('professional_cs2_data.csv')
    except FileNotFoundError:
        print("Data files not found. Run data_collection.py first.")
        return

    # Combine into single DataFrame
    df = pd.concat([personal_df, pro_df], ignore_index=True)
    
    # Pre-processing
    # Only consider rounds where a kill actually happened for HS rate
    df_kill = df[df['Headshot_Kill'] != -1]
    df_entry = df[df['Entry_Attempt'] == 1]

    # Set style
    sns.set_theme(style="whitegrid")

    print("\n--- PHASE 2: Exploratory Data Analysis (EDA) ---")
    
    # EDA 1: Utility Damage Comparison
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Player_Level', y='Utility_Damage', data=df, palette='Set2')
    plt.title('Utility Damage per Round: Amateur vs Professional')
    plt.ylabel('Utility Damage')
    plt.xlabel('Player Level')
    plt.savefig('eda_utility_damage.png')
    print("Saved 'eda_utility_damage.png'")
    
    # EDA 2: Economy Breakdown
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Economy_State', hue='Player_Level', data=df, palette='Set1', order=['Eco', 'Force', 'Full Buy'])
    plt.title('Economy State Distribution')
    plt.ylabel('Frequency (Rounds)')
    plt.xlabel('Buy Type')
    plt.savefig('eda_economy_distribution.png')
    print("Saved 'eda_economy_distribution.png'")
    
    # EDA 3: Win Rate by Buy Type
    win_rates = df.groupby(['Player_Level', 'Economy_State'])['Round_Won'].mean().reset_index()
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Economy_State', y='Round_Won', hue='Player_Level', data=win_rates, palette='viridis', order=['Eco', 'Force', 'Full Buy'])
    plt.title('Round Win Rate by Economy State')
    plt.ylabel('Win Rate')
    plt.xlabel('Buy Type')
    plt.ylim(0, 1)
    plt.savefig('eda_win_rate_economy.png')
    print("Saved 'eda_win_rate_economy.png'")

    print("\n--- PHASE 3: Hypothesis Testing ---")

    # Hypothesis 1: Headshot Rate
    print("\nHypothesis 1: Headshot Rate Difference")
    # Proportions of Headshots
    amateur_hs = df_kill[df_kill['Player_Level'] == 'Amateur']['Headshot_Kill'].mean()
    pro_hs = df_kill[df_kill['Player_Level'] == 'Professional']['Headshot_Kill'].mean()
    
    amateur_hs_dist = df_kill[df_kill['Player_Level'] == 'Amateur']['Headshot_Kill']
    pro_hs_dist = df_kill[df_kill['Player_Level'] == 'Professional']['Headshot_Kill']
    
    t_stat, p_val = stats.ttest_ind(amateur_hs_dist, pro_hs_dist, alternative='less')
    print(f"Amateur HS Rate: {amateur_hs:.2%}")
    print(f"Professional HS Rate: {pro_hs:.2%}")
    print(f"T-statistic: {t_stat:.4f}, p-value: {p_val:.4e}")
    if p_val < 0.05:
        print("Conclusion: Reject H0. Professionals have a significantly higher Headshot percentage.")
    else:
        print("Conclusion: Fail to reject H0.")

    # Hypothesis 2: Utility Damage and Win Rate Correlation
    print("\nHypothesis 2: Utility Damage vs. Win Rate")
    # We will compute point-biserial correlation since Round_Won is binary and Utility_Damage is continuous
    corr_a, p_a = stats.pointbiserialr(df[df['Player_Level'] == 'Amateur']['Round_Won'], 
                                       df[df['Player_Level'] == 'Amateur']['Utility_Damage'])
    corr_p, p_p = stats.pointbiserialr(df[df['Player_Level'] == 'Professional']['Round_Won'], 
                                       df[df['Player_Level'] == 'Professional']['Utility_Damage'])
    
    print(f"Amateur: Correlation={corr_a:.4f}, p-value={p_a:.4e}")
    print(f"Professional: Correlation={corr_p:.4f}, p-value={p_p:.4e}")
    if p_a < 0.05:
        print("Conclusion (Amateur): Reject H0. Utility damage correlates with round success.")

    # Hypothesis 3: Entry Frag Success
    print("\nHypothesis 3: Entry Duel Success Rate")
    amateur_entry_succ = df_entry[df_entry['Player_Level'] == 'Amateur']['Entry_Success'].mean()
    pro_entry_succ = df_entry[df_entry['Player_Level'] == 'Professional']['Entry_Success'].mean()
    t_stat_entry, p_val_entry = stats.ttest_ind(
        df_entry[df_entry['Player_Level'] == 'Amateur']['Entry_Success'],
        df_entry[df_entry['Player_Level'] == 'Professional']['Entry_Success'],
        alternative='less'
    )
    print(f"Amateur Entry Success Rate: {amateur_entry_succ:.2%}")
    print(f"Professional Entry Success Rate: {pro_entry_succ:.2%}")
    print(f"T-statistic: {t_stat_entry:.4f}, p-value: {p_val_entry:.4e}")
    if p_val_entry < 0.05:
         print("Conclusion: Reject H0. Professionals have significantly higher entry duel success.")

    # Hypothesis 4: Eco Round Win Prob
    print("\nHypothesis 4: Winning Eco Rounds")
    eco_df = df[df['Economy_State'] == 'Eco']
    amateur_eco_win = eco_df[eco_df['Player_Level'] == 'Amateur']['Round_Won'].mean()
    pro_eco_win = eco_df[eco_df['Player_Level'] == 'Professional']['Round_Won'].mean()
    t_stat_eco, p_val_eco = stats.ttest_ind(
        eco_df[eco_df['Player_Level'] == 'Amateur']['Round_Won'],
        eco_df[eco_df['Player_Level'] == 'Professional']['Round_Won'],
        alternative='less'
    )
    print(f"Amateur Eco Win Rate: {amateur_eco_win:.2%}")
    print(f"Professional Eco Win Rate: {pro_eco_win:.2%}")
    print(f"T-statistic: {t_stat_eco:.4f}, p-value: {p_val_eco:.4e}")
    if p_val_eco < 0.05:
        print("Conclusion: Reject H0. Professionals win Eco rounds at a significantly higher rate.")
    else:
        print("Conclusion: Fail to reject H0.")

if __name__ == "__main__":
    run_pipeline()
    with open('eda_and_hypothesis_results.txt', 'w') as f:
        f.write("Pipeline ran successfully. Check console output for exact values.")
