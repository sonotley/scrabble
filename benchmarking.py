import scrabble
import json
import random
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# with open(r'brit-a-z.txt', 'r', encoding = "ISO-8859-1") as f:
#     scrabble.build_anagram_fast(f)

max_letters = 7
repeats = 1
with open(r'anagram_dict_fast.json', 'r', encoding = "ISO-8859-1") as f:
    anagrams = json.load(f)

results = {'Anagrams': np.zeros(max_letters), 'Letter Counting': np.zeros(max_letters), 'Semi-Brute': np.zeros(max_letters),
           'Brute Force': np.zeros(max_letters)}

for i in range(1, max_letters + 1):
    for j in range(repeats):
        ll = random.choices("abcdefghijklmnopqrstuvwxyz'", k=i)

        results['Anagrams'][i - 1] += scrabble.anagram_lookup(ll, anagrams)[0]

        with open(r'brit-a-z.txt', 'r',encoding = "ISO-8859-1") as f:
            results['Letter Counting'][i - 1] += scrabble.letter_counting(f, ll)[0]

        with open(r'brit-a-z.txt', 'r',encoding = "ISO-8859-1") as f:
            results['Semi-Brute'][i - 1] += (scrabble.semi_brute(f, ll)[0])

        with open(r'brit-a-z.txt', 'r',encoding = "ISO-8859-1") as f:
            results['Brute Force'][i - 1] += (scrabble.brute(f, ll)[0])

df = pd.DataFrame(data=results, index=(range(1, max_letters + 1)))
print(df)
df.index.name = 'Number of letters'
df.to_csv('bench.csv')
sns.set()


g = sns.barplot(data=df[-1:], log=True)
g.set_ylim(0.00001, 1000)

plt.show()

sns.lineplot(data=df[df.columns[:4]])
plt.xticks(range(1, max_letters + 1))

plt.show()
