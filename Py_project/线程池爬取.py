import requests

def download_one_page(url) :
    resp = requests.get(url)
    print(resp.text)

if __name__ == "__main__" :
    url = ""
    download_one_page()