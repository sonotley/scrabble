import time
import itertools
import json


def timed(fn):
    def wrapped(*args, **kwargs):
        tic = time.time()
        r = fn(*args, **kwargs)
        toc = time.time()
        return toc - tic, r

    return wrapped


@timed
def letter_counting(words, letters):
    result = set()
    for word in words:
        w = word.strip()
        if all((w.count(letter) <= letters.count(letter) for letter in word)) and not w == '':
            result.add(w)
    return result


@timed
def brute(words, letters):
    result = set()
    for word in words:
        for n in range(1, len(letters) + 1):
            for pseudoword in itertools.permutations(letters, n):
                if word.strip() == "".join(pseudoword):
                    result.add(word.strip())
    return result


def _pseudowords(letters):
    pwords = set()
    llist_sorted = sorted(letters)
    for n in range(1, len(llist_sorted) + 1):
        for pseudoword in itertools.combinations(llist_sorted, n):
            pwords.add("".join(pseudoword))
    return pwords


@timed
def semi_brute(words, letters):
    pwords = _pseudowords(letters)
    result = set()
    for word in words:
        if "".join(sorted(word.strip())) in pwords:
            result.add(word.strip())
    return result


@timed
def build_anagram_fast(words):
    anagrams = {}
    for word in words:
        word = word.strip()
        w_sorted = "".join(sorted(word))
        try:
            anagrams[w_sorted].append(word)
        except KeyError:
            anagrams.update({w_sorted: [word]})

    with open(r'D:/anagram_dict_fast.json', 'w') as f:
        json.dump(anagrams, f)


@timed
def anagram_lookup(letters, anagrams):
    pwords = _pseudowords(letters)
    result = set()
    for pw in pwords:
        try:
            result.update(anagrams[pw])
        except KeyError:
            pass
    return result
