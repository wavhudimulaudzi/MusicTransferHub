from flask import Flask, request, redirect, make_response, render_template
import requests
import base64
import json
import os
import re
from spotify import Spotify
from typing import Dict
from decouple import config
from requests.exceptions import RequestException

app = Flask(__name__)
spotify = Spotify()

redirect_uri = 'http://localhost:8888/callback'


# state_key = 'spotify_auth_state'

# Define the GoogleOauthToken interface
class GoogleOauthToken:
    def __init__(self, access_token: str, id_token: str, expires_in: int,
                 refresh_token: str, token_type: str, scope: str):
        self.access_token = access_token
        self.id_token = id_token
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.token_type = token_type
        self.scope = scope


def get_google_oauth_token(code: str) -> GoogleOauthToken:
    root_url = 'https://oauth2.googleapis.com/token'

    options = {
        'code': code,
        'client_id': config('GOOGLECLIENTID'),
        'client_secret': config('GOOGLECLIENTSECRET'),
        'redirect_uri': config('GOOGLEOAUTHREDIRECT'),
        'grant_type': 'authorization_code',
    }

    try:
        response = requests.post(root_url, data=options, headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        })
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()
        return GoogleOauthToken(**data)

    except requests.exceptions.RequestException as e:
        print('Failed to fetch Google Oauth Tokens')
        raise e


# Define the GoogleUserResult interface
class GoogleUserResult:
    def __init__(self, id: str, email: str, verified_email: bool, name: str,
                 given_name: str, family_name: str, picture: str, locale: str):
        self.id = id
        self.email = email
        self.verified_email = verified_email
        self.name = name
        self.given_name = given_name
        self.family_name = family_name
        self.picture = picture
        self.locale = locale


def get_google_user(id_token: str, access_token: str) -> GoogleUserResult:
    try:
        response = requests.get(
            f'https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={access_token}',
            headers={'Authorization': f'Bearer {id_token}'}
        )
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()
        return GoogleUserResult(**data)

    except requests.exceptions.RequestException as e:
        print(e)
        raise e


@app.route('/api/sessions/oauth/google')
def google_oauth_handler():
    try:
        # Get the code from the query
        code = request.args.get('code')
        path_url = request.args.get('state', '/')

        if not code:
            return make_response(('Authorization code not provided!', 401))

        # Use the code to get the id and access tokens
        google_oauth_token = get_google_oauth_token(code)

        # Use the token to get the User
        google_user = get_google_user(google_oauth_token.id_token, google_oauth_token.access_token)

        print(google_user.email)
        print(google_user.verified_email)
        print(google_user.name)
        # Check if the user is verified
        if not google_user.verified_email:
            return make_response(('Google account not verified', 403))

        # Update user if user already exists or create a new user
        # user = find_and_update_user(
        #     {'email': google_user['email']},
        #     {
        #         'name': google_user['name'],
        #         'photo': google_user['picture'],
        #         'email': google_user['email'],
        #         'provider': 'Google',
        #         'verified': True,
        #     },
        #     {'upsert': True, 'runValidators': False, 'new': True, 'lean': True}
        # )

        # if not user:
        #     return redirect(f'{config.get("origin")}/oauth/error')

        # Create access and refresh token
        # access_token, refresh_token = sign_token(user)

        # Send cookies
        response = make_response(redirect(f'{config("ORIGIN")}{path_url}'))
        # response.set_cookie('refresh-token', refresh_token, **refreshTokenCookieOptions)
        # response.set_cookie('access-token', access_token, **accessTokenCookieOptions)
        # response.set_cookie('logged_in', 'true', expires=(datetime.now() + timedelta(
        #     minutes=config.get('accessTokenExpiresIn'))))
        return response

    except RequestException as e:
        print(f'Failed to authorize Google User: {e}')
        return redirect(f'{config.get("origin")}/oauth/error')


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
