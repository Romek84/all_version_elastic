from Elastic1 import all_version_elastic
import tarfile
import requests

def unzip_file(filename):
    with tarfile.open(filename) as file:
        file.extractall('NewVersion')


def download_elastic_version(version):
    url = f"https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{version}-darwin-x86_64.tar.gz"
    response = requests.get(url)
    filename = f"elastic-version{version}.tar.gz"
    if response.status_code == 200:
        with open(filename,"wb") as file:
            file.write(response.content)
            print("File downloaded successfully!")
        unzip_file(filename)
    else:
        print("Failed to download the file.")


# download_elastic_version("8.11.4")
# download_elastic_version("8.12.1")

# print(all_version_elastic())

def download_new_version():
    elastic_list = all_version_elastic()
    elastic_list[0]
    newest_version = elastic_list[0]
    download_elastic_version(elastic_list[0])

download_new_version()

# print(download_new_version())


