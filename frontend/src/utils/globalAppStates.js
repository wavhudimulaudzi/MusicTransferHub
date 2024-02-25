import { defineStore } from 'pinia'

export const useApiDataStore = defineStore('apiData', {
    state: () => ({
        spotify: {
            accessToken: null,
            code: null,
        },
        appleMusic: {
            accessToken: null,
            code: null,
        }
    }),
    getters: {
        getSpotifyAccessToken: (state) => state.spotify.accessToken,
        getSpotifyCode: (state) => state.spotify.code,
        getAppleMusicAccessToken: (state) => state.appleMusic.accessToken,
        getAppleMusicCode: (state) => state.appleMusic.code
    },
    actions: {
        setSpotifyAccessToken(token) {
            this.spotify.accessToken = token
        },
        setSpotifyCode(code) {
            this.spotify.code = code
        }
    }
})