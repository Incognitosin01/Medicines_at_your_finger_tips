import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Medicine_AI.settings')
django.setup()
from difflib import SequenceMatcher,get_close_matches
import re
from Home.models import medicine

l = list((medicine.objects.values_list('name',flat=True)))
# x = 'Paracetamol'
# l = ' '.join(l)
# k = re.search('',l)
# print(k.string)

# y='Paracetamol'
# for i in l:
#     print(i)
#     k = re.search(y,i)
#     if k!=None:
#         break
# print(k.string)
x = get_close_matches('paracetamol', l)
print(x)