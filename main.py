from pilot_aldss import *
from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/main/myapplication", methods=['POST'])
def legalTextSummariserMain():
    print("yes!")
    jsonResponse=request.data.decode(encoding="utf-8")
    parser=json.loads(jsonResponse)
    sourceFile=parser["sourceFile"]
    #sourceFile="data.txt"
    sortedSentenceList=func(sourceFile)
    print(sortedSentenceList)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=3000)
