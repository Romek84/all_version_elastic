import requests

# <em>Elasticsearch version 8.13.2</em>

url = "https://www.elastic.co/guide/en/elasticsearch/reference/current/es-release-notes.html#es-release-notes"

def get_elastic_website():
    response = requests.get(url)

    return response.text

def all_version_elastic():


    text = get_elastic_website()
    text_splited= text.split("\n")

    elastic_versions = [

    ]
    index = 0

    search = f"Elasticsearch"

    for line in text_splited:
        # index = index+1 #dwie wersje
        index +=1
        line.find(search)
        # print(line.find(search))
        # print(f"{index} = {line}")
        if line.find(search)!=-1:           #jeżeli to nie jest -1 przechodzi dalej
            em_index_start = line.find("<em>")
            em_index_end = line.find("</em>")
            if em_index_start !=-1 and em_index_end != -1: #jeżeli "em" istnieją to dane są ok i przechodzimy dalej.
                line_parsed = line[em_index_start+26:em_index_end]

                elastic_versions.append(line_parsed) # jeżeli




    return elastic_versions



