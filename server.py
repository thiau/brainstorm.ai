from server import TextProcessor
from server import encode

documents = [
    "I want to conquer the world",
    "world been had done languages cities mice 2"
]

text_processor = TextProcessor(sentences=documents)
text_processor.process_text()
sentence_tokens = text_processor.get_sentence_tokens()
corpus = text_processor.get_corpus()

print(sentence_tokens)
print(corpus)

# encoded_count = encode("count", sentence_tokens)
encoded_tfidf = encode("tfidf", sentence_tokens)

print(encoded_tfidf)