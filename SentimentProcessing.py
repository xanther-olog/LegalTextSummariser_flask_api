from textblob import TextBlob

def generateSentiments(corpus):

    sentiments={}

    for sentence in corpus:
    	if sentence[1]==0:
    		break
    	testimonial = TextBlob(sentence[0])
        sentiments{sentence[0]}=testimonial.sentiment

    return sentiments
