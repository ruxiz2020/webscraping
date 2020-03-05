import requests
import base64
from bs4 import BeautifulSoup
from langdetect import detect


def decode_foreign_text(string):

    lang = detect(string)
    if lang!="en":
        st = base64.b64encode(string.encode('utf-8'))
        return st
    else:
        return string

def extract_text_from_html(url):

    response = requests.get(url)
    data = response.content.decode('utf-8', errors="replace")

    soup = BeautifulSoup(data, "lxml")
    page = soup.findAll('p')

    list_text = []
    for pp in page:

        text = pp.getText()
        if text.strip()!='':
            list_text.append(text)
        #print(text)

    return list_text


def decode_paragraph(list_sentences):

    list_text
    for string in list_sentences:

        st = decode_foreign_text(string)
        list_text.append(st)

    return list_text

if __name__=="__main__":

    #URL = "https://www.bbc.com/news/science-environment-51761833"
    URL = "https://news.sina.com.cn/c/2020-03-05/doc-iimxyqvz7921464.shtml"

    list_text = extract_text_from_html(URL)
    #for ss in list_text:
    #    print(u(ss).encode('utf-8'))
    #list_text = decode_paragraph(list_text)
    print(list_text)
