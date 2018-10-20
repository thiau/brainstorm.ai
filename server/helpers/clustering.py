from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.stem.snowball import SnowballStemmer
import re
import pandas as pd

stopwords = nltk.corpus.stopwords.words('portuguese')