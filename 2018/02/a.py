import sys
from collections import defaultdict

ids = []
for id in sys.stdin:
    ids.append(id)

def compute_occurrences(id):
    occur = defaultdict(int)
    for letter in id:
        occur[letter] += 1
    return occur

def count_exists(occur, count):
    for val in occur.values():
        if val == count:
            return True
    return False

def solve(ids):
    two_count = 0
    three_count = 0
    for id in ids:
        occur = compute_occurrences(id)
        two_count += 1 if count_exists(occur, 2) else 0
        three_count += 1 if count_exists(occur, 3) else 0
    return two_count * three_count

print solve(ids)
