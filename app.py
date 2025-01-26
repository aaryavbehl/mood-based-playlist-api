from flask import Flask, request, jsonify, render_template
import json
from datetime import datetime

app = Flask(__name__)

SONGS_FILE = 'data/songs.json'
LOGS_FILE = 'data/logs.txt'

def load_songs():
    with open(SONGS_FILE, 'r') as file:
        return json.load(file)
    
def save_songs(data):
    with open(SONGS_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def log_request(endpoint, status):
    with open(LOGS_FILE, 'a') as file:
        file.write(f"[{datetime.now()}] {endpoint} - {status}\n")

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/playlist', methods=['get'])

def get_playlist():
    mood = request.args.get('mood', '').lower()
    limit = int(request.args.get('limit', 5))
    songs = load_songs()
    filtered_songs = [song for song in songs if song['mood'] == mood]
    log_request('/playlist', '200 OK')
    return jsonify(filtered_songs[:limit])

@app.route('/moods', methods=['POST'])

def get_moods():
    songs = load_songs()
    moods = list(set(song['mood'] for song in songs))
    log_request('/moods', '200 OK')
    return jsonify(moods)

@app.route('/add_song', methods=['POST'])

def add_song():
    try:
        new_songs = request.json
        songs = load_songs()
        songs.append(new_song)
        save_songs(songs)
        log_request('/add_song', '200 OK')
        return jsonify({'message': 'Song added successfully'}), 201
    except Exception as e:
        log_request('/add_song', f'500 ERROR: {e}')
        return jsonify({'error': 'Failed to add song'}), 500

if __name__ == '__main__':
    app.run(debug=True)