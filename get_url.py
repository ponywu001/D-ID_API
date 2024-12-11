import requests
import time

talk_id = ['tlk_t_s0YW9ZMweuQBVYeAuPc', 'tlk_o8jYpOSLMmFobo8nxylF2']
api_key = 'd3V4aWFvbWE5NDVAZ21haWwuY29t:QKdheHTnI9u7PHmy3RTIp'

def get_video_url(talk_id, api_key, max_retries=10, delay=3):
    """
    獲取生成的URL，包含重試機制
    """
    url_get_video_url = f"https://api.d-id.com/talks/{talk_id}"
    auth = f"Basic {api_key}"
    
    headers_get_video_url = {
        "accept": "application/json",
        "authorization": auth
    }
    
    for _ in range(max_retries):
        response_get_video_url = requests.get(url_get_video_url, headers=headers_get_video_url)
        response_json = response_get_video_url.json()
        video_url = response_json.get('result_url')
        
        if video_url:
            return video_url
            
        time.sleep(delay)  # wait for a few seconds before retrying
        
    return None

# for i in range(len(talk_id)):
#     video_url = get_video_url(talk_id[i], api_key)
#     print(video_url)