import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk
nltk.download('punkt')
feedback_data = [
    "Great service, loved the product!",
    "Product was okay, but shipping took too long.",
    "Terrible experience, would not recommend.",
    "Amazing product! Will definitely buy again."
]
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text.lower())
    return [word for word in words if word not in stop_words]
word_freq = Counter()
for feedback in feedback_data:
    word_freq.update(preprocess_text(feedback))
N = int(input("Enter the value of N: "))
top_words = word_freq.most_common(N)
print(f"Top {N} most frequent words:")
for word, frequency in top_words:
    print(f"{word}: {frequency}")
words, frequencies = zip(*top_words)
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title(f'Top {N} Most Frequent Words')
plt.xticks(rotation=45)
plt.show()
