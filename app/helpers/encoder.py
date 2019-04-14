""" Module for encoders management """

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

ENCODERS = {"tfidf": TfidfTransformer, "count": CountVectorizer}


def encode(method, corpus, **kwargs):
    """ Encoder Creation """
    encoder = ENCODERS.get(method)
    encoder_object = encoder(**kwargs)
    return encoder_object.fit_transform(corpus)


def get_encoder(method, corpus, **kwargs):
    """ Encoder getter """
    encoder = ENCODERS.get(method)
    encoder_object = encoder(**kwargs)
    encoder_object.fit_transform(corpus)
    return encoder_object
