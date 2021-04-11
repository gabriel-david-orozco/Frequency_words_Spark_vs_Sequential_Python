import urllib.request, math, os
def results(query, kwparse, fromYear, fromMonth, toYear, toMonth, numberofentries):
    if not os.path.exists(query):
        os.makedirs(query) # making a seprate directory for storing webpages
    else:
         print("Folder with similar name already exsists. Please delete the folder and Run again.")
         exit()
    start = 0

    # Determine the max number of pages (dividing by 10 as on website we get 10 results per page)
    pagelimit = numberofentries / 10
    pagelimit = math.ceil(pagelimit)      #rounding up number to next greater integer

    for page in range (0, pagelimit):
        url = 'https://www.oldbaileyonline.org/search.jsp?gen=1&form=searchHomePage&_divs_fulltext='
        url += query
        url += '&kwparse=' + kwparse
        url += '&fromYear=' + fromYear
        url += '&fromMonth=' + fromMonth
        url += '&toYear=' + toYear
        url += '&toMonth=' + toMonth
        url += '&start=' + str(start)
        url += '&count=0'

        response = urllib.request.urlopen(url)
        content = response.read()
        filename = query + '/' + 'SearchResults' + str(start) #save the results with different file names
        f = open(filename + ".html", 'wb')
        f.write(content)
        f.close

        start = start + 10
