#! /home/pat/anaconda3/bin/python3.7

from nltk.tokenize import TreebankWordTokenizer
import nltk
from nltk.util import ngrams
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as sklearn_stop_words
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import numpy as np


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
nltk.download('stopwords')
ntlk_stop_words = nltk.corpus.stopwords.words('english')

stop_words = list(set(ntlk_stop_words) | set(sklearn_stop_words))
stop_words.append("``")
stop_words.append('"')
tokenizer = TreebankWordTokenizer()   # takes into account common english contractions

tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}

def get_wordnet_pos(tag):
    return tag_dict.get(tag, wordnet.NOUN)


def stem(word):
    return stemmer.stem(word).strip("'")

def caseFolding(document):
    return document.lower()

def computeNgrams(wordList, n):
    return list(ngrams(wordList, n))

def removeStopWords(wordList):
    return [x for x in wordList if x and x not in stop_words]

def tokenizeOne(text):
    tokenList = word_tokenize(text)
    return tokenList
    
def tokenizeTwo(tokenList):
    return tokenizer.tokenize(tokenList)

def removePunctuation(tokenList):
    return [k for k in tokenList if k not in "- \t\n.,;!?:"]

def lemmatize(tokenList, tags):
    return list(map(lambda x,y : lemmatizer.lemmatize(x, pos=y), tokenList, [get_wordnet_pos(k[1]) for k in tags]))

def extractVocabulary(document):
    document = caseFolding(document)
    oneGrams = tokenizeOne(document)
    tags = nltk.pos_tag(oneGrams)
    oneGrams = lemmatize(oneGrams, tags)
    oneGrams = tokenizeTwo(" ".join(oneGrams))
    oneGrams = removePunctuation(oneGrams)
    oneGrams = list(map(stem, oneGrams))
    twoGrams = computeNgrams(oneGrams, 2)
    threeGrams = computeNgrams(oneGrams, 3)
    fourGrams = computeNgrams(oneGrams, 4)
    # filtering stop words and uncommon ngrams
    oneGrams = removeStopWords(oneGrams)    # barely useful
    
    return oneGrams

def sideOfPlane(Normal, V):
    return np.asscalar(np.sign(np.dot(Normal, V)))


if __name__ == '__main__':
    testFname = "test.txt"
    with open(testFname, "r") as f:
        test = f.read()
    oneGrams = extractVocabulary(test)
    with open("oneGrams.txt", "w+") as f:
        f.write("\n".join(oneGrams))
    

