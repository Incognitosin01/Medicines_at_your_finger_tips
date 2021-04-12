from os import listdir
from os.path import isfile, join
from side_effects.models import side_effects_data
from string import ascii_lowercase, ascii_uppercase
x=[]
for i in ascii_uppercase:
    for j in ascii_lowercase:
        k=i+j
        x=[]
        for f in listdir("E:\\Backend_work\\Medicine_AI\\Data\\side_effects2"):
            l=['+','-','.','/',' ']
            f=f.replace(".html","")
            f=f.replace(","," ")
            x1 = f[0]
            if f[1] in l:
                x2=f[2].lower()
            else:
                x2=f[1].lower()
            f2 = x1+x2
            if(f2==k):
                x.append(f)
        object=side_effects_data(alpha=k, name_list=x)
        object.save()



