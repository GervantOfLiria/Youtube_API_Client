import time

import requests
import get_latests_vid_url
from youtube_upload.client import YoutubeUploader
uploader = YoutubeUploader(secrets_file_path='client_secret.json')
uploader.authenticate()


def upload_video_to_youtube(video_json):
    # Video options
    options = {
        "title" : video_json['title'], # The video title
        "description" : f"This beautiful ring can be ordered here: \n {video_json['product_url']}\n\n{video_json['description']}", # The video description
        "categoryId" : "22",
        "privacyStatus" : "public", # Video privacy. Can either be "public", "private", or "unlisted"
    }
    print('downloading video')
    r = requests.get(video_json["video_url"])
    with open('temp.mp4', 'wb') as f:
        f.write(r.content)
    # upload video
    print('uploading video')
    uploader.upload('temp.mp4', options)
    time.sleep(10)
    return get_latests_vid_url.get_newest_video()


if __name__ == '__main__':
    vid_url = upload_video_to_youtube({
        'sku': '00000',
        'video_url': 'https://images.qgold.com/0/Videos/10C1048.mp4',
        'description': 'description',
        'title': 'title',
        'product_url': 'url'
    })
    print(vid_url)