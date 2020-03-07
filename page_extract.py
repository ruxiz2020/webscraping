import requests
import base64
from bs4 import BeautifulSoup
from langdetect import detect
from url_extract import gen_url
from s3writer import s3writer


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
    #URL = "https://news.sina.com.cn/c/2020-03-05/doc-iimxyqvz7921464.shtml"
    URLs = gen_url(keyword="狂犬病", num=30)

    print(len(URLs))
    print(URLs)

    for url in URLs:
        text = extract_text_from_html(url)
        
        s3writer(json_data, s3filename, bucket='breakingpet1.s3.us-west-1.aws.com')
    print(list_text)
