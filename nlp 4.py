from collections import Counter
from nltk.util import ngrams


text = """
Speech recognition system helps users type faster.
speech recognition models predict the next word.
predictive text systems use language modes.
speech recognition and predictive text are important.
"""


tokens = text.lower().split()


ug = Counter(tokens)
bg = Counter(ngrams(tokens, 2))
tg = Counter(ngrams(tokens, 3))


V = len(ug)
k = 1


context = ["speech", "recognition"]


nextwords = set(tokens)

scores = {}

for word in nextwords:
    
    laplace = (bg[(context[1], word)] + 1) / (ug[context[1]] + V)

    
    addk = (bg[(context[1], word)] + k) / (ug[context[1]] + k * V)

    
    if bg[(context[0], context[1])] > 0 and tg[(context[0], context[1], word)] > 0:
        backoff = tg[(context[0], context[1], word)] / bg[(context[0], context[1])]
    elif bg[(context[1], word)] > 0:
        backoff = bg[(context[1], word)] / ug[context[1]]
    else:
        backoff = ug[word] / sum(ug.values())

    
    i1, i2, i3 = 0.5, 0.3, 0.2

    
    if bg[(context[0], context[1])] > 0:
        tri = tg[(context[0], context[1], word)] / bg[(context[0], context[1])]
    else:
        tri = 0

    
    if ug[context[1]] > 0:
        bi = bg[(context[1], word)] / ug[context[1]]
    else:
        bi = 0


    uni = ug[word] / sum(ug.values())

    
    interp = i1 * tri + i2 * bi + i3 * uni

    
    scores[word] = (laplace + addk + backoff + interp) / 4


suggestions = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

print("Input:", " ".join(context))
print("Next word suggestions:")
for w, p in suggestions:
    print(w)
