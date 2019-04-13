from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize
import re
import pandas as pd

stemmer = SnowballStemmer("portuguese")
stopwords = stopwords.words("portuguese")


def tokenize_and_stem(text):
    tokens = [
        word for sent in sent_tokenize(text) for word in word_tokenize(sent)
    ]
    filtered_tokens = []
    for token in tokens:
        if re.search("[a-zA-Z]", token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    print(stems)
    return stems


def tokenize_only(text):
    tokens = [
        word.lower() for sent in sent_tokenize(text)
        for word in word_tokenize(sent)
    ]
    filtered_tokens = []

    for token in tokens:
        if re.search("[a-zA-Z]", token):
            filtered_tokens.append(token)
    return filtered_tokens


def cluster(documents, num_cluster):
    tfidf_vectorizer = TfidfVectorizer(
        max_df=0.8,
        max_features=200000,
        min_df=0.0,
        stop_words=stopwords,
        use_idf=True,
        tokenizer=tokenize_only,
        ngram_range=(1, 3))
    matrix = tfidf_vectorizer.fit_transform(documents)

    km = KMeans(n_clusters=3, init="random")
    km.fit_predict(matrix)
    clusters = km.labels_.tolist()
    return clusters


# result = {"question": documents, "cluster_id": clusters}
# result_df = pd.DataFrame(result, index=clusters).sort_values(
#     by="cluster_id", ascending=True)
