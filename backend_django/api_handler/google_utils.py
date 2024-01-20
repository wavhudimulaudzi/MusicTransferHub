from decouple import config
import requests


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
