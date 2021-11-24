from googleapiclient.http import MediaFileUpload
from lib.Google import create_service

class bot:
  CLIENT_SECRET_FILE = 'secrets/client_secrets.json'
  API_NAME = 'youtube'
  API_VERSION = 'v3'
  SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = create_service(bot.CLIENT_SECRET_FILE, bot.API_NAME, bot.API_VERSION, bot.SCOPES)

request_body = {
    'snippet': {
        'categoryI': 19,
        'title': 'Upload Testing',
        'description': 'Hello World Description',
    },
    'status': {
        'privacyStatus': 'private',
        'selfDeclaredMadeForKids': False
    },
    'notifySubscribers': False
}

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=MediaFileUpload('example.mp4')
).execute()
