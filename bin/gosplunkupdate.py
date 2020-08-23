#Imports:
import re
import csv
import sys
import codecs
import os.path
import requests
import subprocess
from lxml import html


#Main determines if site can be reached before updating
def Main():
    status = requests.get("https://gosplunk.com")
    if status.status_code == 200:
        goSplunkUpdate()
    else:
        sys.exit()


#CodeBlock:
def goSplunkUpdate():
    if os.path.exists('..\\lookups\\queries.csv'):
        os.remove('..\\lookups\\queries.csv')
    urllist = "https://gosplunk.com/post-sitemap.xml"
    response = requests.get(urllist)
    a = response.text
    uri = re.findall(r'<loc>(.*?)</loc>',a)
    uri.pop(0)
    for url in uri:
        b = requests.get(url).text
        title = re.findall(r'"og:title" content="(.*?)" />',b)
        title = str(title).replace('[','').replace(']','').replace('\'','')
        author = re.findall(r'rel="author">(.*?)<',b)
        author = str(author).replace('[','').replace(']','').replace('\'','')
        category = re.findall(r'"article:section" content="(.*?)" />',b)
        category = str(category).replace('[','').replace(']','').replace('\'','')
        description = re.findall(r'"og:description" content="(.*?)\[',b)
        description = str(description).replace('[','').replace(']','').replace('\'','')
        query = re.findall(r'<textarea.*>\n(.*?)</t',b)
        query = str(query).replace('[','').replace(']','')
        published = re.findall(r'"article:published_time" content="(.*?)" />',b)
        published = str(published).replace('[','').replace(']','').replace('T.*','').replace('\'','')
        modified = re.findall(r'"article:modified_time" content="(.*?)" />',b)
        modified = str(modified).replace('[','').replace(']','').replace('T.*','').replace('\'','')
        
        csv.register_dialect('myDialect', quoting=csv.QUOTE_MINIMAL)
        file_exists = os.path.isfile('..\\lookups\\queries.csv')
        with open('..\\lookups\\queries.csv', 'a+') as csvFile:
            headers = [u'Title', 'Author', 'Category', 'Description', 'Query', 'Published', 'Modified']
            writer = csv.DictWriter(csvFile, delimiter=',', dialect="myDialect", fieldnames=headers)

            if not file_exists:
                writer.writeheader()
        
            writer.writerow({ 'Title': title[1:], 'Author': author[1:], 'Category': category[1:], 'Description': description[1:], 'Query': query[1:], 'Published': published[1:], 'Modified': modified[1:] })


Main()