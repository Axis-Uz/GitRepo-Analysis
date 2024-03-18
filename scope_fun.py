from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from ast import literal_eval
import re
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation


def plot_missing_values(df_nl: pd.DataFrame):
    '''Give Plot of Feature with Null Values if they exist'''
    temp = df_nl.isna().sum().sort_values(ascending=False)
    temp = temp[temp.values > 0]
    plt.bar(temp.index, temp.values, color='#c1b5fd')
    plt.xlabel('Features')
    plt.ylabel("Number of Missing Values")
    plt.title("Missing Values in Each Column")
    for i, v in enumerate(temp.values):
        plt.text(i, v+0.1, str(v), ha='center', va='bottom')
    plt.show()


def generate_wordcloud(df_wc, feature):
    if feature not in df_wc:
        return f"No column named {feature} in the given data"
    words = ''
    df_wc = df_wc[df_wc.notna()]
    for i, r in df_wc.iterrows():
        text = ""
        if type(r[feature]) == str:
            if r[feature].__contains__('[') or r[feature].__contains__('{'):
                text = literal_eval(r[feature])
            else:
                text = re.split('-| ,| \s+', r[feature])
        for word in text:
            words += word + " "

    word_cloud = WordCloud(
        colormap='binary',
        width=800,
        height=500,
        stopwords=set(STOPWORDS)
    )
    word_cloud.generate(words)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(word_cloud)
    plt.title(f"{feature}:{len(words)}")
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()



sw = set(stopwords.words('english'))
pc = set(punctuation)


def count_description(sentence: str):
    tokens = word_tokenize(sentence)
    cleaned_tokens = [t for t in tokens if t not in sw and t not in pc]

    return len(cleaned_tokens)
