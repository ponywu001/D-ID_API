import time

from upload_audio import upload_audio
from generate_video import generate_video
from get_url import get_video_url

def generate_talking_video(audio_file_name, image_url, api_key):
    """
    主函數：整合所有步驟並返回URL跟execution time
    """
    # start time
    start_time = time.time()
    
    # upload audio
    audio_url = upload_audio(audio_file_name, api_key)
    if audio_url is None:   
        print("upload audio failed...")
        return None, None
    else:
        print("upload audio successfully...")
        print(f'audio_url: {audio_url}')
        # generate video if success
        talk_id = generate_video(image_url, audio_url, api_key)
        if talk_id is None:
            print("generate video failed...")
            return None, None
        else:
            print("generate video successfully...")
            # get video url if success
            video_url = get_video_url(talk_id, api_key)
            if video_url is None:   
                print("get video url failed...")
                return None, None
            else:
                print("get video url successfully...")
                print(f'video_url: {video_url}')
    
    # end time
    execution_time = time.time() - start_time
    
    return video_url, execution_time