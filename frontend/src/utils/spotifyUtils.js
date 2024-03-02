const clientId = "a534b97e062943c5913256751ee1dc53";
const params = new URLSearchParams(window.location.search);
const code = params.get("code");

export async function redirectToAuthCodeFlow(clientId) {
    const verifier = generateCodeVerifier(128);
    const challenge = await generateCodeChallenge(verifier);

    localStorage.setItem("verifier", verifier);

    const params = new URLSearchParams();
    params.append("client_id", clientId);
    params.append("response_type", "code");
    params.append("redirect_uri", "http://localhost:5173/callback");
    params.append("scope", "user-read-private user-read-email user-read-recently-played" +
        " user-library-read user-top-read playlist-modify-public playlist-modify-private playlist-read-private" +
        " playlist-read-collaborative user-follow-modify ugc-image-upload");
    params.append("code_challenge_method", "S256");
    params.append("code_challenge", challenge);

    document.location = `https://accounts.spotify.com/authorize?${params.toString()}`;
}

function generateCodeVerifier(length) {
    let text = '';
    let possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    for (let i = 0; i < length; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    return text;
}

async function generateCodeChallenge(codeVerifier) {
    const data = new TextEncoder().encode(codeVerifier);
    const digest = await window.crypto.subtle.digest('SHA-256', data);
    return btoa(String.fromCharCode.apply(null, [...new Uint8Array(digest)]))
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=+$/, '');
}

export async function getAccessToken(clientId, code) {
    const verifier = localStorage.getItem("verifier");

    const params = new URLSearchParams();
    params.append("client_id", clientId);
    params.append("grant_type", "authorization_code");
    params.append("code", code);
    params.append("redirect_uri", "http://localhost:5173/callback");
    params.append("code_verifier", verifier);

    const result = await fetch("https://accounts.spotify.com/api/token", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: params
    });

    const { access_token } = await result.json();
    return access_token;
}

export async function fetchProfile(token) {
    const result = await fetch("https://api.spotify.com/v1/me", {
        method: "GET", headers: { Authorization: `Bearer ${token}` }
    });

    return await result.json();
}

export async function fetchUserPlaylist(token, userId) {
    const result = await fetch('https://api.spotify.com/v1/users/' + userId + '/playlists', {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${token}`
        }
    });

    let playlistData = await result.json()

    let summarisedPlaylistData = summarisePlaylistData(playlistData.items)

    return getPlaylistsAndTracks(token, summarisedPlaylistData)
}

function summarisePlaylistData(playlistData) {
    let playlists = []
    console.log('playlist data: ', playlistData)
    for (const playlist of playlistData) {
        const playlistDic = {};

        playlistDic['name'] = playlist.name;
        playlistDic['tracks'] = playlist.tracks;
        playlistDic['images'] = playlist.images;
        playlistDic['owner'] = playlist.owner.display_name;
        playlistDic['type'] = playlist.public;

        playlists.push(playlistDic);
    }

    return playlists
}

async function getPlaylistsAndTracks(token, playlistData) {
    const playlistsTracksDetails = [];

    for (const playlist of playlistData) {
        const playlistName = playlist.name;
        const hrefValue = playlist.tracks.href;
        const playlistImages = playlist.images;
        const playlist_owner = playlist.owner;
        const playlist_type = playlist.type;

        const options = {
            url: hrefValue,
            headers: { Authorization: 'Bearer ' + token }
        };

        const response = await fetch(options.url, {
            headers: options.headers
        });
        const tracks = await response.json();

        const playlistTracks = [];

        for (const track of tracks.items) {
            const trackName = track.track.name;

            if (trackName) {
                const artistsList = track.track.artists.map(artist => artist.name).filter(Boolean);
                const trackImages = track.track.album.images;

                const temp = {
                    track_name: trackName,
                    artists: artistsList,
                    images: trackImages
                };
                playlistTracks.push(temp);
            }
        }

        const temp = {
            playlist_name: playlistName,
            tracks: playlistTracks,
            images: playlistImages,
            total: playlistTracks.length,
            owner: playlist_owner,
            type: playlist_type
        };
        playlistsTracksDetails.push(temp);
    }

    return playlistsTracksDetails;
}