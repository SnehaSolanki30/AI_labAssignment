import time
import re

# ==========================================================
# PROBLEM STATEMENT:
# Implement a Natural Language Processing (NLP) Text 
# Preprocessing pipeline performing Lowercasing, Punctuation 
# Removal, Tokenization, Stop-word Removal, and Suffix Stemming.
# ==========================================================

STOP_WORDS = {
    "is", "the", "and", "a", "an", "in", "to", "of", "for", "on", "with", "are", "was"
}

def simple_stemmer(word):
    """Reduces common English word suffixes to their root form."""
    for suffix in ("ing", "ed", "ly", "es", "s"):
        if len(word) > 4 and word.endswith(suffix):
            return word[:-len(suffix)]
    return word


def preprocess_text(raw_text):
    """Runs complete NLP text cleaning and normalization pipeline."""
    start_time = time.time()

    # 1. Lowercase & remove punctuation
    cleaned = re.sub(r'[^a-z\s]', '', raw_text.lower())

    # 2. Tokenization (split into words)
    tokens = cleaned.split()

    # 3. Stop-word Removal
    filtered_tokens = [word for word in tokens if word not in STOP_WORDS]

    # 4. Stemming
    stemmed_tokens = [simple_stemmer(word) for word in filtered_tokens]

    exec_time = (time.time() - start_time) * 1000
    return tokens, filtered_tokens, stemmed_tokens, exec_time


if __name__ == "__main__":
    sample_sentence = "Artificial Intelligence is rapidly transforming the world of computing and robotics!"

    tokens, no_stopwords, stemmed, elapsed = preprocess_text(sample_sentence)

    print("=== NLP Text Preprocessing Pipeline ===")
    print(f"Original Text     : {sample_sentence}")
    print(f"1. Tokens         : {tokens}")
    print(f"2. No Stop-words  : {no_stopwords}")
    print(f"3. Stemmed Words  : {stemmed}")
    print(f"Execution Time    : {elapsed:.4f} ms")
