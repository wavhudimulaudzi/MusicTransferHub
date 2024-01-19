export const getGoogleUrl = (from) => {
    const rootUrl = `https://accounts.google.com/o/oauth2/v2/auth`;

    const options = {
        redirect_uri: 'http://localhost:8000/api/sessions/oauth/google',
        client_id: '164557792132-b6tcfqiio8dqscvg2fjnmafi07kg12m1.apps.googleusercontent.com',
        access_type: 'offline',
        response_type: 'code',
        prompt: 'consent',
        scope: [
            'https://www.googleapis.com/auth/userinfo.profile',
            'https://www.googleapis.com/auth/userinfo.email',
        ].join(' '),
        state: from,
    };

    const qs = new URLSearchParams(options);

    return `${rootUrl}?${qs.toString()}`;
};

