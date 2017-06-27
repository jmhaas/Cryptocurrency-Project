import nltk
import warnings
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

warnings.warn('Code is Deprecated', DeprecationWarning)

tokenizer = RegexpTokenizer(r'\w+')

stop_words = set(stopwords.words('english'))

all_words_pos = []
with open("pos_news_titles.txt", "r") as f_pos:
    for line in f_pos.readlines():
        words = tokenizer.tokenize(line)
        for w in words:
            if w.lower() not in stop_words:
                all_words_pos.append(w.lower())

pos_res = nltk.FreqDist(all_words_pos)

all_words_neg = []
with open("neg_news_titles.txt", "r") as f_neg:
    for line in f_neg.readlines():
        words = tokenizer.tokenize(line)
        for w in words:
            if w.lower() not in stop_words:
                all_words_neg.append(w.lower())

neg_res = nltk.FreqDist(all_words_neg)

all_words_neu = []
with open("neu_news_titles.txt", "r") as f_neu:
    for line in f_neu.readlines():
        words = tokenizer.tokenize(line)
        for w in words:
            if w.lower() not in stop_words:
                all_words_neu.append(w.lower())

neu_res = nltk.FreqDist(all_words_neu)
