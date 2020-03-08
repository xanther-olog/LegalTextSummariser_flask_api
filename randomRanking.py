from GetDictionary import *
from random import randint
dictionary=getDictionary('legal')

file=open('ranked_dict.txt','a')

for word in dictionary:
    if word !='' and word!=' ':
        file.write(word+' '+str(randint(1,15))+'\n')
file.close()
