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
    if(v1<16):
        v1+=1
        continue
    else:
        for j in ascii_lowercase:
            k=i+j

            url="https://drugs.com//alpha//"+k+".html"
            r=requests.get(url)
            htmlContent=r.content
            soup= BeautifulSoup(htmlContent, 'html.parser')

            c1=0
            for divtag in soup.find_all('div', {'class': 'content'}):
                print(k)
                for ultag in divtag.find_all('ul', {'class': 'ddc-list-unstyled'}):
                    print(2)

                    for litag in ultag.find_all('li'):
                        print(3)
                        x=litag.text
                        
                        for link in litag.find_all('a'):
                            y=link.get('href')
                        
                        print(y)
                        url1="https://www.drugs.com/"+y
                        r1=requests.get(url1)

                        htmlContent1=r1.content

                        soup1= BeautifulSoup(htmlContent1, 'html.parser')
                        x1=""" """
                        c3=0
                        flag=0
                        for divtag in soup1.find_all('div', {'class': 'contentBox'}):
                            for div in divtag.find_all("p", {'class':'ddc-reviewed-by'}): 
                                div.extract()

                            for ptag in divtag.find_all(['p','h2','h1','h3','ul']):

                                x2=ptag.get_text(strip=True)
                        
                                x1+=str(ptag)
                        invalid_tags = ['a', 'img']
                        xx2=strip_tags(x1,invalid_tags)

                        x4=x+".html"
                        x4=x4.replace('/','')
                        x5="".join(x4.split())
                        med_names.append(str(xx2))
                        file = open(x5, 'w+',encoding="utf-8") 
                        file.writelines(med_names)
                        med_names=[]
                        x1=" "

