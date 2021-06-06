import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv
file =open('books.csv','w',newline='\n')
file_c=csv.writer(file)
file_c.writerow(['Title','author','price'])

p={'page':'books','send[shop.catalog][order]':1,'send[shop.catalog][reset]':1}
h={'Accept-Language':'en-US'}
url='https://www.lit.ge/'

while p['send[shop.catalog][reset]']<200:
    r=requests.get(url,params=p,headers=h)
    contenet=r.text

    soup=BeautifulSoup(contenet,'html.parser')
    section=soup.find('section',{'class':'list-holder'})
    all_books = section.find_all('article',{'class':'item-holder'})

    for each in all_books:
        t_bar=each.find ('div',{'class':'title-bar'})
        title=t_bar.a.text
        print(title)
        author=t_bar.b.a.text
        price=each.button.text.strip()
        print(title)
        file_c.writerow([title,author,price])
    p['send[shop.catalog][reset]'] += 15
    sleep(randint(1,15))

file.close()
