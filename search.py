from importlib.resources import contents
import os,requests
from bs4 import BeautifulSoup
import youtube
lists4=os.listdir('C:\\')
try:
    b=lists4.index('songs')
    print('found')
except ValueError:
    os.mkdir('C:\\songs')
sngname=''
dwn=''
linkgen=''
def searchfile(d):
 global sngname
 url='https://www.google.com/search?q='
 songname=d   
 r=requests.get(url+songname+'pagalworldpw')
 htmlcontent=r.content 
 soup2=BeautifulSoup(r.content, 'html.parser')
 r1=soup2.find_all('div','egMi0 kCrYT')
 global finallink,r6 
 r2=r1[0].contents

 try:
  for i in r2:
    e1=i.get('href')
    print(e1)
  finallink=requests.get('https://www.google.com'+e1)
  soup3=BeautifulSoup(finallink.content, 'html.parser')
  link4=soup3.find('span')
  global dwn
  dwn=link4.parent['href']
  print(dwn)
  sngname=link4.parent['download']
 except:
     try:
         r=requests.get(url+songname+'song youtube')

         
         soup2=BeautifulSoup(r.content, 'html.parser')
         r1=soup2.find_all('div','egMi0 kCrYT')
         r2=r1[0].contents
         for i in r2:
          e1=i.get('href')
         properlink='https://www.google.com'+e1
         print(properlink)
         global linkgen
         sngname,linkgen= youtube.yt(properlink)
         print(sngname)
         dwn=''
         
     except:     

        del dwn
        del sngname
        del linkgen
    
        print('song no found')
        sngname='not found'
def download():

 
 try:
  finalr=requests.get(dwn)
  loc='C:\\songs'
  finalpath=loc+'\\'+sngname

  with open(finalpath,"wb") as f:
      f.write(finalr.content)
      f.close()
      print('done')
      os.startfile(finalpath)

 except:
      name1= youtube.ytdwn(linkgen)
      print(sngname)
      print('done boss') 
      os.startfile(name1)
     

       