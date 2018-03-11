from textblob import TextBlob
from flask import Flask,request,jsonify
from flask_cors import CORS
import requests
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

@app.route('/getTone',methods = ['GET','POST'])
def getTone():
    mailBody = request.json['content']
    username = 'b8a1cf9f-6ebc-424b-b283-e00e5e7b978c'
    password= 'B3APb1hIkSLz'
    baseUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-19&sentences=false'
    headers = {"content-type": "text/plain"}
    r = requests.post(baseUrl, auth=(username,password),headers = headers,data=mailBody)
    tones = json.loads(r.text)
    tones = tones['document_tone']['tone_categories']
    for tone in tones:
        if(tone['category_id']=='emotion_tone'):
            sortedList = sorted(tone['tones'],key=lambda k: k['score'],reverse=True)        
    return jsonify({"status":'success',"tone": sortedList[0]} )

if __name__ == '__main__':
    app.run(debug=False)
