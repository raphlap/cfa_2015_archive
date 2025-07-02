# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

for abstract in abstracts :
    word_fd = nltk.FreqDist(abstract)
    bigram_fd = nltk.FreqDist(nltk.bigrams(abstract))
    finder = BigramCollocationFinder(word_fd, bigram_fd)
    finder.apply_freq_filter(2)
    finder.apply_word_filter(lambda w:w in nltk.corpus.stopwords.words('english'))
    scored = finder.score_ngrams(bigram_measures.raw_freq)

all_scores = []
for abstract in abstracts :
    word_fd = nltk.FreqDist(abstract)
    bigram_fd = nltk.FreqDist(nltk.bigrams(abstract))
    finder = BigramCollocationFinder(word_fd, bigram_fd)
    finder.apply_freq_filter(2)
    finder.apply_word_filter(lambda w:w in nltk.corpus.stopwords.words('english'))
    scored = dict(finder.score_ngrams(bigram_measures.raw_freq))
    all_scores.append(scored)

abstracts_bis = list(Data['abstract'].values())
tokenized_abstracts_bis = word_tokenize(unicode(abstracts_bis))
all_scores = []
word_fd = nltk.FreqDist(tokenized_abstracts_bis)
bigram_fd = nltk.FreqDist(nltk.bigrams(tokenized_abstracts_bis))
finder = BigramCollocationFinder(word_fd, bigram_fd)
finder.apply_freq_filter(2)
finder.apply_word_filter(lambda w:w in nltk.corpus.stopwords.words('english'))
scored = dict(finder.score_ngrams(bigram_measures.raw_freq))
all_scores.append(scored)

import nltk
bigram_measures = nltk.collocations.BigramAssocMeasures()
word_fd = nltk.FreqDist(tokenized_abstracts_bis)
bigram_fd = nltk.FreqDist(nltk.bigrams(tokenized_abstracts_bis))
finder = BigramCollocationFinder(word_fd, bigram_fd)
finder.apply_freq_filter(2)
finder.apply_word_filter(lambda w:w in nltk.corpus.stopwords.words('english'))
scored = dict(finder.score_ngrams(bigram_measures.raw_freq))
scored

td_matrix = {}
for idx in range(len(abstracts)):
    abstract = abstracts[idx]

    bibcodes = Data['bibcode'][str(idx)]
    percentage_frenchness = Data['percentage of FR authors'][str(idx)]
    td_matrix[(bibcodes, percentage_frenchness)] = {}
    for bigram in scored.iterkeys():
        td_matrix[(bibcodes, percentage_frenchness)][bigram] = scored[bigram]