# Advent of Code
# Day 02 -- Part B

import sys

def match_word(word1, word2):
    result = ''
    for c1, c2 in zip(word1, word2):
        if c1 == c2:
            result += c1
    return result

def solve(ids):
    for i, word1 in enumerate(ids):
        for word2 in ids[i+1:]:
            match = match_word(word1, word2)
            if len(match) == len(word1) - 1:
                return match

ids = []
for id in sys.stdin:
    ids.append(id)
print solve(ids)
