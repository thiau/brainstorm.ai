""" Module for Clustering """

from sklearn.cluster import DBSCAN
import pandas as pd


class Clustering:
    def __init__(self, features, corpus):
        self.features = features
        self.corpus = corpus
        self.clusters = list()
        self.MODELS = {"dbscan": DBSCAN}
        self.cluster_dataset = pd.DataFrame()

    def cluster(self, method="dbscan", **kwargs):
        """ Execute Clustering """
        db_scan = self.MODELS.get(method)(**kwargs)
        db_scan.fit(self.features)

        self.clusters = db_scan.labels_.tolist()
        self._generate_cluster_dataset()

    def _generate_cluster_dataset(self):
        columns = {"document": self.corpus, "cluster": self.clusters}
        self.cluster_dataset = pd.DataFrame(
            columns, index=[self.clusters], columns=["document", "cluster"])

    def get_cluster_dataset(self):
        return self.cluster_dataset
