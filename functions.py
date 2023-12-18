# author: Myungkeun Park

import streamlit as st
try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError as e:
    st.warning(f"{e}")

st.set_option('deprecation.showPyplotGlobalUse', False)

def load_data_ver1():
    return pd.read_csv('./github_dataset.csv')

def load_data_ver2():
    return pd.read_csv('./repository_data.csv')

def compute_statistics(df, column, name_column):
    stats = {
        "Mean": round(df[column].mean(), 2),
        "Median": round(df[column].median(), 2),
        "Mode": round(df[column].mode()[0], 2),
        "Lower Quartile": round(df[column].quantile(0.25), 2),
        "Upper Quartile": round(df[column].quantile(0.75), 2),
        "Max Value": df[column].max(),
        "Min Value": df[column].min()
    }

    max_idx = df[column].idxmax()
    min_idx = df[column].idxmin()

    stats["Max Value Repository"] = df.loc[max_idx, name_column]
    stats["Min Value Repository"] = df.loc[min_idx, name_column]

    return stats

def top_languages(df, column='primary_language'):
    return df[column].value_counts().head(10)

def languages_used_stats(df, column='languages_used'):
    num_languages = df[column].apply(lambda x: len(x.split(',')) if pd.notnull(x) else 0)
    return {
        "Mean": round(num_languages.mean(), 2),
        "Median": num_languages.median()
    }

def top_licenses(df):
    return df['licence'].value_counts().head(10)

def plot_language_distribution(df, column='primary_language'):
    language_counts = df[column].value_counts()
    plt.figure(figsize=(12, 8))
    sns.barplot(y=language_counts.values, x=language_counts.index)
    plt.xticks(rotation=90)
    plt.ylabel('Count')
    plt.xlabel('Language')
    plt.title('Top Languages Distribution for Version 1')
    
def plot_language_distribution_2(df, column='primary_language', top_n=50):
    language_counts = df[column].value_counts().head(top_n)
    plt.figure(figsize=(12, 8))
    plt.xticks(rotation=90)
    sns.barplot(y=language_counts.values, x=language_counts.index)
    plt.ylabel('Count')
    plt.xlabel('Language')
    plt.title('Top Languages Distribution for Version 2')
