<script setup>
import NavBar from "@/components/NavBar.vue";
import HomeBody from "@/components/HomeBody.vue";
import Footer from "@/components/Footer.vue";
import {onBeforeMount} from 'vue'
import {getAccessToken, fetchProfile} from "@/utils/spotifyUtils.js";

var code = null;
const clientId = "a534b97e062943c5913256751ee1dc53";
var accessToken = null;
var profile = null;

onBeforeMount(async () => {
  var params = new URLSearchParams(window.location.search);
  code = params.get("code");

  if (code !== null) {
    console.log('I am executed: ', code)
    accessToken = await getAccessToken(clientId, code);
    console.log('AccessToken: ', accessToken)
    // profile = await fetchProfile(accessToken);
    // console.log(profile)
  }
});
</script>

<template>
  <NavBar :code="code"/>
  <HomeBody />
  <Footer />
</template>

<style scoped>

</style>