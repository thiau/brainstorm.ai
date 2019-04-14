from app.helpers.encoder import encode
from app.nlp.text_process import TextProcessor
from app.nlp.cluster import Clustering


def start_clustering(documents):
    text_processor = TextProcessor(sentences=documents)
    text_processor.process_text()
    corpus = text_processor.get_corpus()

    encoded_count = encode("count", corpus)
    encoded_tfidf = encode("tfidf", encoded_count)

    clustering = Clustering(features=encoded_tfidf, corpus=corpus)
    clustering.cluster("dbscan", eps=1, min_samples=1, n_jobs=4)
    cluster_ds = clustering.get_cluster_dataset()

    return cluster_ds
