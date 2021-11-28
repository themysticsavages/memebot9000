from flask import Flask, request, render_template, jsonify, send_file, abort
from datetime import datetime
import requests
import random
import string
import json

app = Flask('')

@app.errorhandler(404)
def fouroffour(e):
    return render_template('404.html')

@app.get('/')
def index():
    video = json.loads(requests.get(request.host_url+'/api/fetchv/').text)
    latest = video['videos'][-1]

    return render_template('index.html') \
        .replace('/latest/', str(latest[1]+' | '+datetime.fromtimestamp(latest[2]).strftime('%m/%d/%Y'))) \
        .replace('/id/', latest[0])

@app.get('/about/')
def about():
    return render_template('about.html')

@app.get('/watch/')
def watch():
    return render_template('watch.html') \
        .replace('/id/', request.args.get('id'))

@app.get('/video/')
def video():
    return send_file('templates/api/videos/{}.mp4'.format(request.args.get('id')))

@app.get('/api/')
def api():
    return jsonify({'website': request.host.replace('/api', '')})

@app.post('/api/post/')
def api_post():
    form = request.form
    if not form['title']:
        abort(400)
    elif '/' in form['title']:
        return 'malicious parameter'
    else:
        file = request.files['fstream']
        v_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=11))
        file.save('templates/api/videos/{}.mp4'.format(v_id))

        data = json.load(open('templates/api/videos.json'))
        print(data)
        data['videos'].append([v_id, form['title'], datetime.now().timestamp()])
        json.dump(data, open('templates/api/videos.json', 'w'))

        return jsonify({'status': 'complete', 'video_id': v_id})

@app.get('/api/fetchv/')
def fetchv():
    fh = json.load(open('templates/api/videos.json'))
    return jsonify({'videos': fh['videos']})
