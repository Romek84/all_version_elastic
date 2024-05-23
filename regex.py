import re

line = "ljadshasjldhsakjd s  <em>Elasticsearch version 8.13.2</em> lashjdjlas"

search_regex = r"<em>Elasticsearch version (\d+\.\d+\.\d+)<\/em>"



match = re.search(search_regex, line)
if match is not None:

    version = match.group(1)


    print(version)  
