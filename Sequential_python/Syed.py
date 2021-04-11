import urllib.request
import time # added

start_time =  time.time() # added
stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your','8th']
stopwords += ['yours', 'yourself', 'yourselves', 'came', 'came,', 'did', 'xc2xa0', '324', 'rnttttt', '3']

#url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
#webpage = urllib.request.urlopen(url)
#content = webpage.read()

file = open('/home/Frequency_words_Spark_vs_Sequential_Python/' + i, 'r')
content = file.read().split(" ")
def removetags(contents):
    stringcontents = str(contents)
    startread = stringcontents.find("<p>")  # ignoring the contents of html page prior to line 83 tag <p>324
    endread = stringcontents.rfind("<br/>")  # ignoring the contents of html page subsequent to last occurrence of tag
    # <br/> in line 84

    actualcontent = stringcontents[startread:endread]

    i = 0
    b = ''

    for CHAR in actualcontent:        # Removing the remaining tags from actual content

        if CHAR == '<':                # If the character == < ,we are inside a tag ignore the character and change i=1
            i = 1
        elif i == 1 and CHAR == '>':   # If i=1 and the character is (>), we are leaving the tag hence ignore the character
            i = 0
        elif i == 1:
            continue                  # repeat loop and go to the next character in the actualContent string without performing any operation
        else:
            b = b + CHAR              # if we are not inside the tags append the content characters to the b string

    return b


def eliminateStopwords(List, stopwords):  # iterate through all the words in the List & comparing stopwords
    return [words for words in List if
            words not in stopwords]  # If the word doesn't exist in the stopwords, it is returned & append to the list


text = (removetags(content)).lower()  # removing tags from web content and converting into lower case
punct = '''!()[]{};:"\,<>./?@#$%^&*_~'''
initial = " "
for char in text:
    if char not in punct:
        initial = initial + char
for char in initial:
    text1 = initial.replace("-", " ")  # removing "-" from text, I didn't included in "punct" because compounded words
    # like house-door will be considered as housedoor if included in punct
for char in text1:
    text2 = text1.replace("\'", " ")  # similar reason as above in this case "prisoner's" was being considered as prisoners

List = text2.split()
finalList = eliminateStopwords(List, stopwords)
sortedlist = sorted(finalList)
newlist = []
freqs = []
for words in sortedlist:

    if words not in newlist:   # checks to see if word is in newlist
        newlist.append(words)  # if not it adds it to the end newlist
        freqs.append(1)        # and adds 1 to the end of freqs
    else:
        index = newlist.index(words)  # if it is it will find where in newlist
        freqs[index] += 1             # and to change add 1 to the matching index in freq
Dlist = (dict((list(zip(newlist, freqs)))))


def dlistsort(freq):
    dfreq = [(freq[key], key) for key in freq]
    dfreq.sort()
    dfreq.reverse()
    return dfreq


final = dlistsort(Dlist)
for i in final:
    print(i)
end_time =  time.time()
print(f"the total time is" end_time - start_time) # Added
