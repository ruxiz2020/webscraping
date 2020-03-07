from googlesearch import search
#for url in search('"Breaking Code" WordPress blog', stop=2):

def gen_url(keyword, num):

    list_url = []
    for url in search(keyword + ' google', stop=num):
        list_url.append(url)

    return list_url
