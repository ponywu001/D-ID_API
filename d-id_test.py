import requests
import time
# API key : d3V4aWFvbWE5NDVAZ21haWwuY29t:QKdheHTnI9u7PHmy3RTIp

url = "https://api.d-id.com/talks"

payload = {
    "source_url": "https://s3.ap-southeast-1.amazonaws.com/pony.test/body.png",
    "script": {
        "type": "audio",
        "audio_url": "s3://d-id-audios-prod/auth0|6757e42626afa0f251925f61/X6pVvELXN53bRzLzwtA17/curry-15sec.wav"
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic d3V4aWFvbWE5NDVAZ21haWwuY29t:QKdheHTnI9u7PHmy3RTIp"
}

# 開始計時
start_time = time.time()

response = requests.post(url, json=payload, headers=headers)
response_json = response.json()
talk_id = response_json.get('id')  # 儲存返回的 ID

# 結束計時
end_time = time.time()
execution_time = end_time - start_time
    
print(f'response.text : {response.text}')
print()
print(f'talk_id : {talk_id}')  # 打印 ID 以驗證
print()
print(f'執行時間：{execution_time:.2f} 秒')  # 顯示執行時間



# s3://d-id-audios-prod/auth0|6757e42626afa0f251925f61/X6pVvELXN53bRzLzwtA17/curry-15sec.wav