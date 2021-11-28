from video_service.app import app
import json

if __name__ == '__main__':
  port = json.load(open('bot.config.json'))['web_port']
  app.run(threaded=True, port=port, host='0.0.0.0')
