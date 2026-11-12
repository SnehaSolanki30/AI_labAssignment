import time
import math
from collections import defaultdict

# ==========================================================
# PROBLEM STATEMENT:
# Implement a Multinomial Naive Bayes Classifier from scratch 
# to perform Sentiment Analysis (Positive vs. Negative) on 
# short text reviews.
# ==========================================================

class NaiveBayesSentiment:
    def __init__(self):
        self.class_word_counts = {"Positive": defaultdict(int), "Negative": defaultdict(int)}
        self.class_doc_counts = {"Positive": 0, "Negative": 0}
        self.vocab = set()

    def train(self, dataset):
        for text, label in dataset:
            self.class_doc_counts[label] += 1
            for word in text.lower().split():
                self.class_word_counts[label][word] += 1
                self.vocab.add(word)

    def predict(self, sentence):
        total_docs = sum(self.class_doc_counts.values())
        vocab_size = len(self.vocab)
        scores = {}

        for label in ["Positive", "Negative"]:
            # Prior log probability
            log_prob = math.log(self.class_doc_counts[label] / total_docs)
            total_words_in_class = sum(self.class_word_counts[label].values())

            # Laplace-smoothed word likelihoods
            for word in sentence.lower().split():
                word_count = self.class_word_counts[label][word]
                log_prob += math.log((word_count + 1) / (total_words_in_class + vocab_size))

            scores[label] = log_prob

        return max(scores, key=scores.get)


if __name__ == "__main__":
    start_time = time.time()

    training_reviews = [
        ("this product is amazing and super fast", "Positive"),
        ("great quality and awesome experience", "Positive"),
        ("love the clean design and smooth performance", "Positive"),
        ("terrible quality and very slow service", "Negative"),
        ("bad experience waste of money", "Negative"),
        ("awful product broke after one day", "Negative")
    ]

    model = NaiveBayesSentiment()
    model.train(training_reviews)

    test_review = "awesome design and super smooth experience"
    result = model.predict(test_review)
    elapsed = (time.time() - start_time) * 1000

    print("=== NLP Sentiment Analysis (Naive Bayes) ===")
    print(f"Test Review         : '{test_review}'")
    print(f"Predicted Sentiment : {result}")
    print(f"Execution Time      : {elapsed:.4f} ms")
