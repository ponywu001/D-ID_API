import requests

def upload_audio(audio_file_name, api_key):
    """
    上傳音檔到 D-ID
    """
    url_upload_audio = "https://api.d-id.com/audios"
    auth = f"Basic {api_key}"
    
    files = { "audio": (audio_file_name, open(audio_file_name, "rb"), "audio/mpeg") }
    headers_upload_audio = {
        "accept": "application/json",
        "authorization": auth
    }
    
    response_upload_audio = requests.post(url_upload_audio, files=files, headers=headers_upload_audio)
    response_json = response_upload_audio.json()
    return response_json.get('url')

# audio_file_name = 'curry_15sec.mp3'
# api_key = 'd3V4aWFvbWE5NDVAZ21haWwuY29t:QKdheHTnI9u7PHmy3RTIp'

# audio_url = upload_audio(audio_file_name, api_key)
# print(audio_url)
