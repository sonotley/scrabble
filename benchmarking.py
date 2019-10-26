import scrabble
import json
import random
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# with open(r'brit-a-z.txt', 'r', encoding = "ISO-8859-1") as f:
#     scrabble.build_anagram_fast(f)

max_letters = 20
repeats = 10
with open(r'anagram_dict_fast.json', 'r', encoding = "ISO-8859-1") as f:
    anagrams = json.load(f)

results = {'anagram': np.zeros(max_letters), 'counting': np.zeros(max_letters), 'semibrute': np.zeros(max_letters),
           'brute': np.zeros(max_letters)}

for i in range(1, max_letters + 1):
    for j in range(repeats):
        ll = random.choices("abcdefghijklmnopqrstuvwxyz'", k=i)

        results['anagram'][i - 1] += scrabble.anagram_lookup(ll, anagrams)[0]

        with open(r'brit-a-z.txt', 'r',encoding = "ISO-8859-1") as f:
            results['counting'][i - 1] += scrabble.letter_counting(f, ll)[0]

        with open(r'brit-a-z.txt', 'r',encoding = "ISO-8859-1") as f:
            results['semibrute'][i - 1] += (scrabble.semi_brute(f, ll)[0])

        # with open(r'brit-a-z.txt', 'r',encoding = "ISO-8859-1") as f:
        #     results['brute'][i - 1] += (scrabble.brute(f, ll)[0])

df = pd.DataFrame(data=results, index=(range(1, max_letters + 1)))
print(df)
df.to_csv('bench.csv')
sns.set()

sns.lineplot(data=df)
plt.show()
