from flask import Flask, request, redirect, make_response, render_template
import requests
import base64
import json
import os
import re
import random
import string
from decouple import config

app = Flask(__name__)

redirect_uri = 'http://localhost:8888/callback'
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
STATE_KEY = config('STATE_KEY')

# state_key = 'spotify_auth_state'

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    state = generate_random_string(16)
    resp = make_response(redirect('https://accounts.spotify.com/authorize?' +
                                  f'response_type=code&client_id={CLIENT_ID}&scope=user-read-private%20user-read-email&redirect_uri={redirect_uri}&state={state}'))
    resp.set_cookie(STATE_KEY, state)
    return resp


@app.route('/callback')
def callback():
    global filtered_profile_date
    code = request.args.get('code', None)
    state = request.args.get('state', None)
    stored_state = request.cookies.get(STATE_KEY)

    if state is None or state != stored_state:
        return redirect('/#' + json.dumps({'error': 'state_mismatch'}))
    else:
        resp = make_response(redirect('/#'))
        resp.delete_cookie(STATE_KEY)

        auth_options = {
            'url': 'https://accounts.spotify.com/api/token',
            'data': {
                'code': code,
                'redirect_uri': redirect_uri,
                'grant_type': 'authorization_code'
            },
            'headers': {
                'content-type': 'application/x-www-form-urlencoded',
                'Authorization': 'Basic ' + base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode('utf-8')
            }
        }

        response = requests.post(**auth_options)
        if response.status_code == 200:
            data = response.json()
            access_token = data.get('access_token')
            refresh_token = data.get('refresh_token')

            options = {
                'url': 'https://api.spotify.com/v1/me',
                'headers': {'Authorization': 'Bearer ' + access_token}
            }

            profile_response = requests.get(**options)
            profile_data = profile_response.json()
            print(profile_data)  # Do something with the profile data
            filtered_profile_date = {
                'display_name': profile_data.get('display_name'),
                'profile_image': 'https://i.scdn.co/image/ab67757000003b82aa101325470b4f2568f221d5',  # profile_data.get('images')[0].get('url'),
                "playlist_url": "http://localhost:8888/spotify/getPlaylistsForUser?access_token=" + access_token + "&user_id=" + user_id_extractor(profile_data.get('uri')),
                # Need to find a better way of handling this
            }

            resp.headers['Location'] += json.dumps({
                'access_token': access_token,
                'refresh_token': refresh_token
            })

        return render_template('home.html', data=filtered_profile_date)


def user_id_extractor(spotify_uri: str):
    pattern = r"spotify:user:(\w+)"  # Spotify user pattern
    match = re.search(pattern, spotify_uri)

    if match:
        return match.group(1)
    else:
        return "No match found."


@app.route('/spotify/getPlaylistsForUser', methods=['GET', 'POST'])
def getPlaylistsUser():
    if request.method == 'GET':
        access_token = request.args.get('access_token')
        user_id = request.args.get('user_id')

        options = {
            'url': 'https://api.spotify.com/v1/users/' + user_id + '/playlists',
            'headers': {'Authorization': 'Bearer ' + access_token}
        }

        playlist_response = requests.get(**options)
        playlist_list = playlist_response.json().get('items')

        playlist_data = summarise_playlist(playlist_list)

        return render_template('home.html', playlist_data=playlist_data)

# [
# {
#   name: slow Jam,
#   tracks: {'href': 'https://api.spotify.com/v1/playlists/0hMbFKJ5oCamJ4EKr6usGY/tracks', 'total': 3}
# },
# {
#   name: One of Those days,
#   tracks: {'href': 'https://api.spotify.com/v1/playlists/5HAZhbBDRqjgC2KLEAGVFK/tracks', 'total': 11}
# },
# {
#   name: gospel,
#   tracks: {'href': 'https://api.spotify.com/v1/playlists/0OMFEc34XGQ2l63bSlaR7i/tracks', 'total': 3}
# }
# ]

def summarise_playlist(playlist_list):
    summarised = []
    for playlist in playlist_list:
        playlist_dic = {}
        for key, value in playlist.items():
            if key == 'name' or key == 'tracks':
                playlist_dic[key] = value

        summarised.append(playlist_dic)

    return summarised



if __name__ == '__main__':
    app.run(port=8888)

# my_user_id = i36lrmsgfre56jp0q2lmanat1
