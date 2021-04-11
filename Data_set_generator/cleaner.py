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

def cleaner(query) :
    opener = open(query + "_full_text.txt", 'r')
    original_text = opener.read()
    text = stripTags(original_text)
    text = deleteTags(text)
    text = "".join(text)
    text = ' '.join(text.split())
    fl = open(query + "_cleaned.txt", 'a')
    fl.write(text)
