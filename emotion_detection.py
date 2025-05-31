from flask import Flask, request, jsonify
import requests  # <- Add this import
import json

app = Flask(__name__)

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=data)  # <- use requests here
    return response.text

@app.route('/')
def welcome():
    return "Welcome to the Emotion Detection API!"

if __name__ == '__main__':
    app.run(debug=True)
