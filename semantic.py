# semantic.py
import spacy

# Load the larger model
nlp = spacy.load("en_core_web_md")

# Compare semantic similarities
tokens = nlp("cat monkey banana")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
