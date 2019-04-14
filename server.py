from server import TextProcessor, encode, Clustering

documents = [
    "hello my name is thiago", "hello my name is camila",
    "hi my name is camila", "i like to ride car", "i like to ride many cars",
    "i love to drive cars"
]

text_processor = TextProcessor(sentences=documents)
text_processor.process_text()
corpus = text_processor.get_corpus()

encoded_count = encode("count", corpus)
encoded_tfidf = encode("tfidf", encoded_count)

clustering = Clustering(features=encoded_tfidf, corpus=corpus)
clustering.cluster("dbscan", eps=1, min_samples=1, n_jobs=4)
cluster_ds = clustering.get_cluster_dataset()

print(cluster_ds)
