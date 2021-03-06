# just blindly crawling the web starting from seed page

# get_page() procedure for getting the contents of a webpage as a string

import urllib
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""


# procedure for finding and returning the next url from the passing page parameter
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

# procedure for finding the union of two lists
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
    return p


# given a seed page, it will return all the links in that page
def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


# procedure for adding a new keyword,url pair to index
def add_to_index(index,keyword,url):
    for each in index:
        if each[0] == keyword:
            urls = each[1]
            if url not in urls:
                urls.append(url)
            return
    new_keyword = [keyword,[url]]
    index.append(new_keyword)
        

def add_page_to_index(index,url,content):
    words = content.split();
    for each in words:
        add_to_index(index,each,url)


# for crawling the web, constrained on the maximum different pages crawled
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()                    
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index,page,content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index


# Running the program with given seed pagec and max_pages
print crawl_web("http://www.udacity.com/cs101x/index.html")


