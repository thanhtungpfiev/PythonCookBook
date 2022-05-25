# Created by Admin at 5/14/2022
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

word_counts.update(morewords)
top_three = word_counts.most_common(3)
print(top_three)

a = Counter(words)
b = Counter(morewords)
c = a + b
print(c)
top_three = c.most_common(3)
print(top_three)
