<script setup>
import NavBar from "@/components/NavBar.vue";
import HomeBody from "@/components/HomeBody.vue";
import Footer from "@/components/Footer.vue";
import {ref, onMounted} from "vue";
import { useApiDataStore } from "@/utils/globalAppStates.js"
import {fetchProfile} from "@/utils/spotifyUtils.js";

const clientId = "a534b97e062943c5913256751ee1dc53";
const dataStore = useApiDataStore();

const accessToken = ref(null);
var profileData = ref(null);

onMounted(async () => {
  accessToken.value = dataStore.getSpotifyAccessToken;
  if (accessToken.value !== null) {
    profileData.value = await fetchProfile(accessToken.value);
    // console.log(profileData.value);
  }
});

</script>

<template>
  <NavBar :access-token="accessToken" :profile-data="profileData"/>
  <HomeBody />
  <Footer />
</template>

<style scoped>

</style>