import string
from collections import Counter
import matplotlib.pyplot as plt


feedback_data = [
    "I love the new product! It's amazing and very useful.",
    "The service was terrible and the product is not good.",
    "Amazing experience! I love it!",
    "Not satisfied with the product. Bad quality.",
    "Great service and fast delivery. I love it!",
    "The product quality is excellent and I am happy.",
    "Delivery was slow and customer support is bad."
]


stop_words = {
    "the", "and", "is", "am", "are", "was", "were", "be", "to", "it", "with", "a",
    "an", "i", "not", "very", "of", "in", "on", "for", "this", "that", "so"
}


def preprocess_text(text_list):
    cleaned_words = []

    for sentence in text_list:
       
        sentence = sentence.lower()

        
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))

      
        words = sentence.split()

        
        words = [word for word in words if word not in stop_words]

        cleaned_words.extend(words)

    return cleaned_words


words = preprocess_text(feedback_data)

word_freq = Counter(words)


N = int(input("Enter the number of top frequent words to display: "))


top_words = word_freq.most_common(N)
print("\nTop", N, "most frequent words:")
for word, freq in top_words:
    print(f"{word}: {freq}")


words_list = [item[0] for item in top_words]
freq_list = [item[1] for item in top_words]

plt.figure(figsize=(10, 5))
plt.bar(words_list, freq_list)
plt.title(f"Top {N} Most Frequent Words in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
