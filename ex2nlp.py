import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab') 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, RegexpStemmer

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')

text = """
The product quality is very good
and I am extremely happy with the service.
The delivery was late, but the customer support was helpful.
Overall the experience was positive and I would recommend this
company.
"""

# Prepare stopwords set
stop_words = set(stopwords.words('english'))

# Tokenize and remove stopwords
words = [w for w in word_tokenize(text.lower()) if w.isalpha() and w not in stop_words]

print("Words after stop removal:\n", words)

# Initialize stemmers
porter = PorterStemmer()
snowball = SnowballStemmer("english")
lancaster = LancasterStemmer()
regex = RegexpStemmer('ing$|ed$|ly$|es$|s$')

# Apply stemming
print("\nPorter Stemmer:", [porter.stem(w) for w in words])
print("\nSnowball Stemmer:", [snowball.stem(w) for w in words])
print("\nLancaster Stemmer:", [lancaster.stem(w) for w in words])
print("\nRegex Stemmer:", [regex.stem(w) for w in words])
