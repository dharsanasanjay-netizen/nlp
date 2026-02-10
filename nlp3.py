import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
posts=[
"I love this new phone battery life is amazing",
"This update is very bad and disappointing",
"Amazing camera and great performance",
"I love the camera quality and the battery performance"
]

nltk.download("stopwords")
stwords = set(stopwords.words('english'))
ug,bg,tg=[],[],[]
for post in posts:
    post = post.lower()
    post = re.sub(r'[^a-z\s]',"", post)
    words = [w for w in post.split() if w not in stwords]
    ug.extend(words)
    bg.extend(zip(words, words[1:]))
    tg.extend(zip(words, words[2:]))
    ugc = Counter(ug)
    bgc = Counter(bg)
    tgc = Counter(tg)
    print("Top Unigrams", ugc.most_common(3))
    print("\nTop BIgrams", bgc.most_common(3))
    print("\nTop Trigrams", tgc.most_common(3))


from textblob import TextBlob
print("\nSentiment ANalysis")
for post in posts:
    blob = TextBlob(post)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        print("Positive")
    elif polarity < 0:
        print("Negative")
    else:
        print("Neutral")
    print(f"Post: '{post}' - Polarity: {polarity}")
