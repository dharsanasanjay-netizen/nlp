import spacy

base = spacy.load("en_core_web_sm")

input_text = """
GR Mano is a highly skilled software engineer.
who has been working here at infosys for the past ten years.
he completed his masters degree from anna university.
he is currently living in virudhunagar.
"""

doc = base(input_text)

print("\nNOUN PHRASES")
for chunk in doc.noun_chunks:
    print(chunk.text)

print("\nVERB PHRASES")
for token in doc:
    if token.pos_ == "VERB":
        print(token.text)

print("\nADJECTIVE PHRASES")
for token in doc:
    if token.pos_ == "ADJ":
        print(token.text)

print("\nPREPOSITIONAL PHRASES")
for token in doc:
    if token.pos_ == "ADP":
        # Collect preposition and its object subtree
        phrase = " ".join([tok.text for tok in token.subtree])
        print(phrase)
