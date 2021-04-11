import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def stripTags(pageContents):  # Removes the headers of the html
    startLoc = pageContents.find('<p>')
    endLoc = pageContents.find('<br/>')
    pageContents = pageContents[startLoc:endLoc]
    return pageContents


def deleteTags(pageContents):  # This removes the rest of the html components that not corresponds to the original text
    text = []
    for char in pageContents:
        if char == '<':
            inside = 1
        elif inside == 1 and char == '>':
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char
    return text

def deleteStopwords(text): # This function removes the stop words
  text_tokens = word_tokenize(text)
  tokens = [word for word in text_tokens if not word in stopwords.words()]
  weird_characters = [ "\\xc2\\xa0", "\r\n\t\t\t\t\t" ]
  tokens_clean = [word for word in tokens if not word in weird_characters]
  return re.compile(r'\W+',re.UNICODE).split(" ".join(tokens_clean))
  #return tokens_clean

def cleaner(query, number_of_files) :
    query = str(number_of_files) + "_" + query
    opener = open(query + "_full_text.txt", 'r')
    original_text = opener.read()
    text = stripTags(original_text)
    text = deleteTags(text)
    text = "".join(text)
    text = ' '.join(text.split())
    text = deleteStopwords(text)
    text = " ".join(text)
    fl = open(query + "_cleaned.txt", 'a')
    fl.write(text)
