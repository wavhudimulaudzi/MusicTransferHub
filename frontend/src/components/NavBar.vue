<script setup>
import {useApiDataStore} from "@/utils/globalAppStates.js";
import ProfileCard from "@/components/ProfileCard.vue";
import {onMounted} from "vue";
import {fetchProfile} from "@/utils/spotifyUtils.js";

const dataStore = useApiDataStore();
const accessToken = dataStore.getSpotifyAccessToken;
var profileData = null;

onMounted(async () => {

  if (accessToken !== null) {
    profileData = await fetchProfile(accessToken);
    console.log(profileData)
  }
})
</script>

<template>
<nav>
  <div>
    <img src="../assets/logo.svg" alt="playlistTransfer logo"/>
  </div>
  <ul v-if="accessToken === null">
    <li id="login" key="login">
      <router-link to="login">Login</router-link>
    </li>
    <li id="buyMeCoffee" key="buyMeCoffee">
      <router-link to="donate">Buy Me Coffee</router-link>
    </li>
    <li id="termsOfUse" key="termsOfUse">
      <router-link to="termsofuse">Terms of Use</router-link>
    </li>
  </ul>
  <ProfileCard
      v-if="accessToken !== null"
      :profile-image-url="profileData.images[1].url"
      :user-full-name="profileData.display_name"
      platform-name="Spotify" platform-class="spotify"
      :user-email-address="profileData.email"
  />
</nav>
</template>

<style scoped>

nav {
  padding: 15px 90px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}

li {
  margin-left: 20px;
  padding: 10px;
}

a {
  text-decoration: none;
  color: #FFFFFF;
  font-size: 22px;
  font-weight: 600;
}

#login {
  background-color: #000000;
  border-radius: 12px;

}

#login a {
  color: #ffffff;
}

</style>