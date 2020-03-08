from InputData import *
from CleanCorpus import *

from GetDictionary import *

from ProcessStopwords import *
from WordListGeneration import *

from RankBasedSort import *
from WordCountBasedSort import *
import sys

def func():

    #document_name=input("Select document to summarize:")
    document_name='data.txt'
    document=getData(document_name)
    paras_dt,tncs_dt,tncs_list=getSentences(document)
    for t in tncs_list:
        print(t)
    document_type=input("Select summary type\n1. legal 2.\ntechnical:")
    document_type='legal'
    legalDictionary=getDictionary(document_type)
    docWordList=processStopwords(document)
    foundWordsList,newWordsList=generateWordList(docWordList,legalDictionary)
    rankSet,rankToSentences_dict=rankBasedSort(foundWordsList,tncs_list)

    sortedSentenceList=wordCountSort(rankSet,rankToSentences_dict,foundWordsList)

    #test code
    for sentence in sortedSentenceList:
        print(sentence)

func()
