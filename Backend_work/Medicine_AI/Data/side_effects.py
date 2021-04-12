import requests,csv
from bs4 import BeautifulSoup,NavigableString
from string import ascii_lowercase
import io
med_names=[]
c=0

def strip_tags(html, invalid_tags):
    soup = BeautifulSoup(html)

    for tag in soup.findAll(True):
        if tag.name in invalid_tags:
            s = ""

            for c in tag.contents:
                if not isinstance(c, NavigableString):
                    c = strip_tags(str(c), invalid_tags)
                s += str(c)

            tag.replaceWith(s)

    return soup
v1=0
for i in ascii_lowercase:
    for j in range(0,20):
        
            url="https://drugs.com//sfx-"+i+str(j)+".html"
            r=requests.get(url)
            htmlContent=r.content
            soup= BeautifulSoup(htmlContent, 'html.parser')

            c1=0
            for ultag in soup.find_all('ul', {'class': 'ddc-list-column-2'}):

                for litag in ultag.find_all('li'):
                    x=litag.text
                    
                    for link in litag.find_all('a'):
                        y=link.get('href')
                    
                    print(y)
                    url1="https://www.drugs.com/"+y
                    r1=requests.get(url1)

                    htmlContent1=r1.content

                    soup1= BeautifulSoup(htmlContent1, 'html.parser')
                    x1=" "
                    c3=0
                    flag=0
                    for divtag in soup1.find_all('div', {'class': 'contentBox'}):
                        for div in divtag.find_all("p", {'class':'ddc-reviewed-by'}): 
                            div.extract()

                        for ptag in divtag.find_all(['p','h1','h2','h3','ul']):
                            
                            x2=ptag.get_text(strip=True)
                            x1+=str(ptag)
                            
                    invalid_tags = ['a', 'img']
                    xx2=strip_tags(x1,invalid_tags)
                    x=x.replace('/','')
                    x4="D://side_effects2//"+x+".html"
                    
                    med_names.append(str(xx2))
                    file = open(x4, 'w+',encoding="utf-8") 
                    file.writelines(med_names)
                    med_names=[]
                    x1=" "






                    