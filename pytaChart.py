#! /usr/bin/env python

"""pytaChart.py: a bar chart from a dataframe of text statistics"""

import pandas as pd, matplotlib as mpl

# Import data from file into dataframe
df = pd.read_csv("textStats.csv", ",")

# Sort by the longest text
by_longest = df.sort_values(by="Count", axis=0, ascending=False) 

# Draw the graph (note use of ggplot)
mpl.style.use('ggplot')
ax = by_longest[['Count','Lexicon']].plot(kind='bar', 
                                           title ="Text Stats",
                                           figsize=(15,10),
                                           legend=True,
                                           fontsize=12)
ax.set_xlabel("Text",fontsize=12)
ax.set_ylabel("Word Count",fontsize=14)
ax.set_xticklabels(list(by_longest['Text'])) 
mpl.pyplot.show()