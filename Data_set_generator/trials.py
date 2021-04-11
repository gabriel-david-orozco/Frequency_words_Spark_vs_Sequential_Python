def trials(query, number_of_files):
    import os, urllib.request
    query = str(number_of_files) + "_" + query
    #  importing built-in python functions for building file paths
    from os.path import join as pjoin

    # returns a list containing the names of the entries in the directory given by path i.e. "query"
    queryfolder = os.listdir(query)

    url = []


    for files in queryfolder:       # finding searchresults pages in new folder named husband
        if files.find("SearchResults") != -1:
            a = open(query + "/" + files, 'r')
            text = a.read().split(" ")
            a.close()


            for words in text:   # searching for trial individul trial IDs
                if words.find("browse.jsp?id=") != -1:
                    intialchar = words.find("id=") + 3      # isolating each id
                    finalchar = words.find("&")
                    trial = words[intialchar: finalchar]

                    url.append(trial)

    query = query + "/text_files"
    os.makedirs(query)
    for items in url:

        url = "http://www.oldbaileyonline.org/print.jsp?div=" + items  # generating the URL


        response = urllib.request.urlopen(url)   # downloading the page
        content = response.read()


        filename = 'request_' + items + '.txt'           #creating the new filename & placing it in the new directory
        path = pjoin(query, filename)
        print(path)


        f = open(path, 'wb')
        f.write(content)
        f.close
