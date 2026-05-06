import requests
import json

def emotion_detector(text_to_analyze):

    # URL
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Headers
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Input JSON
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Solicitud POST
    response = requests.post(url, json=input_json, headers=headers)

    # Resultado
    return response.json()
    