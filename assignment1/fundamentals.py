import pandas as pd
import matplotlib.pyplot as plt

article_info_df = pd.read_csv("articleInfo.csv")
author_info_df = pd.read_csv("authorInfo.csv")

merge_df = pd.merge(article_info_df, author_info_df, on='Article No.')
merge_df = merge_df.fillna(0)

fig, ax = plt.subplots()
merge_df["Year"].value_counts().plot(ax = ax, kind="line")
fig.savefig("freq.pdf")
print(merge_df)