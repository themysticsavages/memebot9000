from googleapiclient.http import MediaFileUpload
from lib.Google import Create_Service

class bot:
  CLIENT_SECRET_FILE = 'client_secrets.json'
  API_NAME = 'youtube'
  API_VERSION = 'v3'
  SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(bot.CLIENT_SECRET_FILE, bot.API_NAME, bot.API_VERSION, bot.SCOPES)

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
