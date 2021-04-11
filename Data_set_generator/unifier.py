import os
def unifier(query, number_of_files):
    query = str(number_of_files) + "_" + query
    queryfolder = os.listdir(query + '/text_files')
    full_file_text = query + "_full_text.txt"

    data = ""
    for file in queryfolder:
        with open(query + '/text_files/' + file) as fp:
            data = fp.read()
        fl = open(full_file_text, 'a')
        fl.write(data)
