from textblob import TextBlob
from nltk.corpus import stopwords
from flask import Flask,request,jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

@app.route('/getSentiment',methods = ['GET','POST'])
def getSentiment():
    arrSubs = request.json
    arrSentiment = []
    for sub in arrSubs:
        text = TextBlob(sub)
        arrSentiment.append(round(text.sentiment[0],2))  
    return jsonify({"status":'success',"sentiment":arrSentiment})


if __name__ == '__main__':
    app.run(debug=False)
