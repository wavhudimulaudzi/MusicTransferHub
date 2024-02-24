<script setup>
import {onMounted} from "vue";
import { useRouter } from 'vue-router';
import {getAccessToken} from "@/utils/spotifyUtils.js";
import { useApiDataStore } from "@/utils/globalAppStates.js"

const clientId = "a534b97e062943c5913256751ee1dc53";
const dataStore = useApiDataStore();

onMounted(async () => {
  const router = useRouter();
  var params = new URLSearchParams(window.location.search);
  var code = params.get("code");

  if (code !== undefined) {
    const accessToken = await getAccessToken(clientId, code);

    try {
      dataStore.setSpotifyAccessToken(accessToken);
    } catch (error) {
      console.error('Error setting Spotify access token:', error);
    }

    await router.push({name: 'home'})
  }
})
</script>

<template>

</template>

<style scoped>

</style>