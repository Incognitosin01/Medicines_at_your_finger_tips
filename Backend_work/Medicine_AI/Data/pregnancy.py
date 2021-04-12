import requests,csv
from bs4 import BeautifulSoup,NavigableString
from string import ascii_lowercase
import io
med_names=[]

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
c=0
for i in ascii_lowercase:
                    if(c==1):
                        break
                    else:
                        c+=1
                    url="https://www.drugs.com/cg/hyperthyroidism-in-pregnancy.html"
                    r=requests.get(url)
                    htmlContent=r.content
                    soup= BeautifulSoup(htmlContent, 'html.parser')
                    x1=" "
                    c3=0
                    flag=0
                    for divtag in soup.find_all('div', {'class': 'contentBox'}):
                        for div in divtag.find_all("p", {'class':'ddc-reviewed-by'}): 
                            div.extract()

                        for ptag in divtag.find_all(['p','h1','h2','h3','ul']):
                            
                            x2=ptag.get_text(strip=True)
                            x1+=str(ptag)
                            
                    invalid_tags = ['a', 'img']
                    xx2=strip_tags(x1,invalid_tags)

                    x4="Hyperthyroidism_in_Pregnancy.html"
                    x4=x4.replace('/','')
                    med_names.append(str(xx2))
                    file = open(x4, 'w+',encoding="utf-8") 
                    file.writelines(med_names)
                    med_names=[]
                    x1=" "




