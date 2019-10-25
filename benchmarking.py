import scrabble
import json
import random
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# build_anagram_fast()

n=20

with open(r'D:/anagram_dict_fast.json', 'r') as f:
    anagrams = json.load(f)

results = {'anagram': np.zeros(n), 'counting': np.zeros(n), 'semibrute': np.zeros(n)}

for i in range(1, n):
    for j in range(10):
        ll = random.choices("abcdefghijklmnopqrstuvwxyz", k=i)

        results['anagram'][i-1] += scrabble.anagram_lookup(ll, anagrams)[0]

        with open(r'D:/brit-a-z.txt', 'r') as f:
            results['counting'][i-1] += scrabble.letter_counting(f, ll)[0]

        with open(r'D:/brit-a-z.txt', 'r') as f:
            results['semibrute'][i-1] += (scrabble.semi_brute(f, ll)[0])

df = pd.DataFrame(data=results, index=(range(1,n)))
print(df)
sns.set()

sns.lineplot(data=df)
plt.show()
