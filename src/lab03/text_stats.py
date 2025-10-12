import sys
sys.path.append('../lib')
from ..lib import text # normalize, tokenize, count_freq, top_n

s = input()
top = 5
a = text.normalize(s, casefold=True, yo2e=True)
print(a)
print(f"{len(s.split())}")