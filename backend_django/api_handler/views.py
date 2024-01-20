from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests.exceptions import RequestException
from .google_utils import *
from .services import get_user_by_email, create_user


# Create your views here.
def google_oauth_handler(request):
    try:
        # Get the code from the query
        code = request.GET.get('code')
        path_url = request.GET.get('state', '/')

        if not code:
            return HttpResponse(('Authorization code not provided!', 401))

        # Use the code to get the id and access tokens
        google_oauth_token = get_google_oauth_token(code)

        # Use the token to get the User
        google_user = get_google_user(google_oauth_token.id_token, google_oauth_token.access_token)

        print(google_user.email)
        print(google_user.verified_email)
        print(google_user.name)
        # Check if the user is verified
        if not google_user.verified_email:
            return HttpResponse(('Google account not verified', 403))

        # Update user if user already exists or create a new user
        user = get_user_by_email(google_user.email)

        if user is not None:
            user.full_name = google_user.name
            user.provider = google_user.picture
            user.provider = 'Google'
            user.verified = True
            user.role = 'Client'

            user.save()
        else:
            user = create_user(email=google_user.email, full_name=google_user.name, provider='Google', verified=True, role='Client', password=None)

        if not user:
            return redirect(f'{config.get("origin")}/oauth/error')

        # Create access and refresh token
        # access_token, refresh_token = sign_token(user)

        # Send cookies
        response = HttpResponse(redirect(f'{config("ORIGIN")}{path_url}'))
        response.set_cookie('refresh-token', google_oauth_token.refresh_token)#, **refreshTokenCookieOptions)
        response.set_cookie('access-token', google_oauth_token.access_token)#, **accessTokenCookieOptions)
        response.set_cookie('logged_in', 'true', expires=(datetime.now() + timedelta(
            hours=1)))
        return response

    except RequestException as e:
        print(f'Failed to authorize Google User: {e}')
        return redirect(f'{config.get("origin")}/oauth/error')
