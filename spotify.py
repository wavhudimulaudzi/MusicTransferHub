from decouple import config
import random
import string


class Spotify:
    def __init__(self):
        self._client_id = config('CLIENT_ID')
        self._client_secret = config('CLIENT_SECRET')
        self._state_key = config('STATE_KEY')
        self._state = self.generate_random_string(16)
        self._access_token = None
        self._profile_data = None

    def get_client_id(self):
        return self._client_id

    def set_client_id(self, client_id):
        self._client_id = client_id

    def set_client_secret(self, client_secret):
        self._client_secret = client_secret

    def get_client_secret(self):
        return self._client_secret

    def get_state_key(self):
        return self._state_key

    def set_state_key(self, state_key):
        self._state_key = state_key

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def get_access_token(self):
        return self._access_token

    def set_access_token(self, access_token):
        self._access_token = access_token

    def get_profile_data(self):
        return self._profile_data

    def set_profile_data(self, profile_data):
        self._profile_data = profile_data

    def generate_random_string(self, length):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
