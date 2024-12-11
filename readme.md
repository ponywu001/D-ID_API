# D-ID API
This is a python script to generate talking video using D-ID API.

## INPUT
+ image url
+ mp3檔
+ api key

## Execution
    python main.py
+ 參數 : 
    + audio_file_name (type : string)
    + body_image (type : URL)
    + api_key (type : string)



## OUTPUT
+ video url
+ execution time


## FLOWCHART
### 1. upload_audio.py
+ url : https://api.d-id.com/audios

+ **input** : <font color="red">mp3檔</font>
+ **output** : <font color="red">audio_id</font>

### 2. generate_talking_video.py
+ url: https://api.d-id.com/talks

+ **input** : <font color="red">audio_id</font>
+ **output** : <font color="red">talk_id</font>

### 3. get_url.py
+ url: https://api.d-id.com/talks/{talk_id}

+ **input** : <font color="red">talk_id</font>
+ **output** : <font color="red">video_url</font>

### generate_talking_video.py
+ **Integrate all steps** (upload_audio, generate_talking_video, get_url)

### 4. write_in_excel.py
+ get video_url

+ write in excel