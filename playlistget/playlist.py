#!/usr/bin/env python3
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import youtube_dl
import sys

app = Flask(__name__)
CORS(app)
TOKEN = "DEFAULT_TOKEN"

def to_output(entry):
    return {
        'url': entry['url'],
        'title': entry['title'],
    }

def get_playlist(url):
    dl_opts = { "--flat-playlist": True, }
    with youtube_dl.YoutubeDL(dl_opts) as ydl:
        result = ydl.extract_info(url, download=False, process=False)
        return list(map(to_output, result['entries']))

def invalid_token():
    print(request.args)
    return 'token' not in request.args or request.args['token'] != TOKEN

@app.route('/<yt_id>/', methods=['GET'])
def get(yt_id):
    # flask is whild in that that we dont get request args via the callback here
    if invalid_token(): 
        print("invalid token")
        abort(401) # raises 401

    yt_id = yt_id.strip()
    if yt_id == "":
        print("no playlist id")
        abort(400) # raises 401

    url = f"https://www.youtube.com/playlist?list={yt_id}"

    print("Getting playlist for ", repr(url))
    pl = get_playlist(url)
    return jsonify(pl)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: ./playlist.py <TOKEN> <PORT>")
        sys.exit(1)
    TOKEN = sys.argv[1]
    port = int(sys.argv[2])
    app.run(port=port) # could switch to something more robust
