import requests

def generate_video(image_url, audio_url, api_key):
    """
    使用圖片和音檔生成影片
    """
    url_generate_video = "https://api.d-id.com/talks"
    auth = f"Basic {api_key}"
    
    payload_generate_video = {
        "source_url": image_url,
        "script": {
            "type": "audio",
            "audio_url": audio_url
        }
    }
    headers_generate_video = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": auth
    }
    
    response_generate_video = requests.post(url_generate_video, json=payload_generate_video, headers=headers_generate_video)
    response_json = response_generate_video.json()
    return response_json.get('id')