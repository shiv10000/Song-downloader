import os,requests
import urllib
import re
import sys
from bs4 import BeautifulSoup
lists4=os.listdir('C:\\')

try:
    b=lists4.index('songs')
    print('found')
except ValueError:
    os.mkdir('C:\\songs')
url='https://www.pagalworld.pw/new-punjabi-mp3-songs-download/files.html'
r=requests.get(url)
htmlcontent=r.content 
soup2=BeautifulSoup(r.content, 'html.parser')
link3=soup2.find_all(style='font-weight: 400')
def nextt():
    global htmlcontent
    soup6=BeautifulSoup(htmlcontent, 'html.parser')
    link4=soup6.find('li',class_='next')
    n=link4.contents[0]
    z=n.get('href')
    global url,link3
    url='https://www.pagalworld.pw'+z
    r9=requests.get(url)
    htmlcontent=r9.content 
    soup5=BeautifulSoup(htmlcontent, 'html.parser')
    link3=soup5.find_all(style='font-weight: 400')

def movie():
 a4=list()   
 for i in link3:
    a5=i.string
    a4.append(a5)
 return a4 
sngname=''
def download(o):
    movie=link3[o]
    song=movie.parent['href']
    r4=requests.get('https://www.pagalworld.pw/'+song)
    soup3=BeautifulSoup(r4.content, 'html.parser')
    link4=soup3.find('span')
    dwn=link4.parent['href']
    global sngname
    sngname=link4.parent['download']
    finalr=requests.get(dwn)
    loc='C:\\songs'
    finalpath=loc+'\\'+sngname
    try:
        with open(finalpath,"wb") as f:
            f.write(finalr.content)
            f.close()
            print('done')
    except:
        print('error') 
             

     








