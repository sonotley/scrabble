import scrabble
import json

# build_anagram_fast()

with open(r'D:/anagram_dict_fast.json', 'r') as f:
    anagrams = json.load(f)

ll = list('cataclysmic')
print(scrabble.anagram_lookup(ll, anagrams))

with open(r'D:/brit-a-z.txt', 'r') as f:
    print(scrabble.letter_counting(f, ll))

with open(r'D:/brit-a-z.txt', 'r') as f:
    print(scrabble.semi_brute(f, ll))
