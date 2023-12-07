from flask import Flask, request, redirect, make_response, render_template
import requests
import base64
import json
import os
import re
from spotify import Spotify

app = Flask(__name__)
spotify = Spotify()

redirect_uri = 'http://localhost:8888/callback'


# state_key = 'spotify_auth_state'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    resp = make_response(redirect('https://accounts.spotify.com/authorize?' +
                                  f'response_type=code&client_id={spotify.get_client_id()}&scope=user-read-private%20user-read-email&redirect_uri={redirect_uri}&state={spotify.get_state()}'))
    resp.set_cookie(spotify.get_state_key(), spotify.get_state())
    return resp


@app.route('/callback')
def callback():
    global filtered_profile_date
    code = request.args.get('code', None)
    state = request.args.get('state', None)
    stored_state = request.cookies.get(spotify.get_state_key())

    if state is None or state != stored_state:
        return redirect('/#' + json.dumps({'error': 'state_mismatch'}))
    else:
        resp = make_response(redirect('/#'))
        resp.delete_cookie(spotify.get_state_key())

        auth_options = {
            'url': 'https://accounts.spotify.com/api/token',
            'data': {
                'code': code,
                'redirect_uri': redirect_uri,
                'grant_type': 'authorization_code'
            },
            'headers': {
                'content-type': 'application/x-www-form-urlencoded',
                'Authorization': 'Basic ' + base64.b64encode(f'{spotify.get_client_id()}:{spotify.get_client_secret()}'.encode()).decode('utf-8')
            }
        }

        response = requests.post(**auth_options)
        if response.status_code == 200:
            data = response.json()
            spotify.set_access_token(data.get('access_token'))
            refresh_token = data.get('refresh_token')

            options = {
                'url': 'https://api.spotify.com/v1/me',
                'headers': {'Authorization': 'Bearer ' + spotify.get_access_token()}
            }

            profile_response = requests.get(**options)
            spotify.set_profile_data(profile_response.json())
            filtered_profile_date = {
                'display_name': spotify.get_profile_data().get('display_name'),
                'profile_image': 'https://i.scdn.co/image/ab67757000003b82aa101325470b4f2568f221d5',
                "playlist_url": "http://localhost:8888/spotify/getPlaylistsForUser",
                # Need to find a better way of handling this
            }

            resp.headers['Location'] += json.dumps({
                'access_token': spotify.get_access_token(),
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
        options = {
            'url': 'https://api.spotify.com/v1/users/' + user_id_extractor(spotify.get_profile_data().get('uri')) + '/playlists',
            'headers': {'Authorization': 'Bearer ' + spotify.get_access_token()}
        }

        playlist_response = requests.get(**options)
        playlist_list = playlist_response.json().get('items')

        playlist_data = summarise_playlist(playlist_list)

        spotify.set_playlist_data(playlist_data)

        tracks = get_playlist_tracks(spotify.get_playlist_data())

        print(tracks)

        return render_template('home.html', playlist_data=playlist_data)


# [
#   {
#       playlist_name: slow Jam,
#       tracks: [
#
#       ]
#   }
# ]

def get_playlist_tracks(playlist_data):
    playlists_tracks_details = []
    for playlist in playlist_data:
        playlist_name = playlist['name']
        href_value = playlist['tracks']['href']

        options = {
            'url': href_value,
            'headers': {'Authorization': 'Bearer ' + spotify.get_access_token()}
        }

        response = requests.get(**options)
        tracks = response.json().get('items')

        playlist_tracks = []

        for track in tracks:
            track_name = track.get("track", {}).get("name")

            if track_name:
                artists_list = []
                artists = track.get("track", {}).get("artists")
                for artist in artists:
                    artist_name = artist.get("name")
                    if artist_name:
                        artists_list.append(artist_name)

                temp = {
                    'track_name': track_name,
                    'artists': artists_list
                }
                playlist_tracks.append(temp)

        temp = {
            "playlist_name": playlist_name,
            "tracks": playlist_tracks
        }
        playlists_tracks_details.append(temp)

    return playlists_tracks_details


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
