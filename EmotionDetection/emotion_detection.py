import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=header)

    formatted_response = json.loads(response.text)['emotionPredictions'][0]['emotion']

    if response.status_code == 200:
        dominant_emotion = max(formatted_response, key=formatted_response.get)
        formatted_response['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        formatted_response = {k: None for k, _ in formatted_response.items()}
        formatted_response['dominant_emotion'] = None

    return formatted_response