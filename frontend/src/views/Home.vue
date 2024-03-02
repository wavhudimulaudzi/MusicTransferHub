<script setup>
import NavBar from "@/components/NavBar.vue";
import HomeBody from "@/components/HomeBody.vue";
import Footer from "@/components/Footer.vue";
import {ref, onMounted, onUpdated} from "vue";
import { useApiDataStore } from "@/utils/globalAppStates.js"
import {fetchProfile, fetchUserPlaylist} from "@/utils/spotifyUtils.js";

const clientId = "a534b97e062943c5913256751ee1dc53";
const dataStore = useApiDataStore();

const accessToken = ref(null);
var profileData = ref(null);
var playlistData = ref(null);

onMounted(async () => {
  accessToken.value = dataStore.getSpotifyAccessToken;
  if (accessToken.value !== null) {
    profileData.value = await fetchProfile(accessToken.value);
    dataStore.setSpotifyUserId(profileData.id);
    // console.log('accessToken: ', accessToken.value, ' userId: ', profileData.value.id)
    playlistData.value = await fetchUserPlaylist(accessToken.value, profileData.value.id)
    console.log(playlistData.value)
  }
});

// onUpdated(async () => {
//   playlistData.value = await fetchUserPlaylist(accessToken, dataStore.getSpotifyUserId)
//   console.log(playlistData)
// });

</script>

<template>
  <NavBar class="navBar" :access-token="accessToken" :profile-data="profileData"/>
  <HomeBody class="body" :playlists="playlistData"/>
  <Footer class="footer"/>
</template>

<style scoped>
.navBar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
}

.body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #333;
  color: #fff;
  padding: 10px 20px;
}
</style>