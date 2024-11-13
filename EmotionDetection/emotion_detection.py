import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)['emotionPredictions'][0]['emotion']
        dominant_emotion = max(formatted_response, key=formatted_response.get)
        formatted_response['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        labels = ["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"]
        formatted_response = {k: None for k in labels}

    return formatted_response