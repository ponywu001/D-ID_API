from generate_talking_video import generate_talking_video
from write_in_excel import write_to_excel

audio_file_name = ['curry_15sec.mp3', 'curry_30sec.mp3', 'curry_45sec.mp3']
body_image = [
    'https://s3.ap-southeast-1.amazonaws.com/pony.test/body_15sec.png',
    'https://s3.ap-southeast-1.amazonaws.com/pony.test/body_30sec.png',
    'https://s3.ap-southeast-1.amazonaws.com/pony.test/body_45sec.png'
]
api_key = 'cHd1MTQzNzNAZ21haWwuY29t:SaNasN6yVn29ZucJdZW_J'

result = [('result_URL', 'execution_time')]

# generate talking video
for i in range(len(audio_file_name)):
    result.append(generate_talking_video(audio_file_name[i], body_image[i], api_key))   
print(result)

# write to excel    
write_to_excel(result)

