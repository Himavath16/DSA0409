import string
from collections import Counter


reviews = [
    "The product is really good and I loved the quality!",
    "Good product but the delivery was slow.",
    "I am not happy with the product quality.",
    "Excellent quality and fast delivery!",
    "The product is okay but could be better."
]


def preprocess(text):
    text = text.lower()                                  
    text = text.translate(str.maketrans('', '', string.punctuation))  
    return text

cleaned_reviews = [preprocess(review) for review in reviews]


all_text = " ".join(cleaned_reviews)


words = all_text.split()


word_frequency = Counter(words)


print("Word Frequency Distribution:\n")
for word, freq in word_frequency.items():
    print(f"{word}: {freq}")
