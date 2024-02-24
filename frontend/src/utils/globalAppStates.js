import { defineStore } from 'pinia'

export const useApiDataStore = defineStore('apiData', {
    state: () => ({
        spotifyAccessToken: null,
    }),
    getters: {
        getSpotifyAccessToken: (state) => state.spotifyAccessToken,
    },
    actions: {
        setSpotifyAccessToken(token) {
            this.$patch({ spotifyAccessToken: token });
        }
    }
})