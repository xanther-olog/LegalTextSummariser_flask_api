def getDictionary(type):

    dictionary=[]
    if type=='legal':
        file=open("legal_words.txt","r+")
        data=file.read()
        dictionary=data.split("\n")
        file.close()
    elif type=='ranked_legal':
        file=open("ranked_dict.txt","r+")
        data=file.read()
        dictionary=data.split("\n")
        file.close()
    elif type=='stopwords':
        file=open("stopwords.txt","r+")
        words=file.read()
        stopWordList=words.split("\n")
        file.close()

    return dictionary[:-1]
