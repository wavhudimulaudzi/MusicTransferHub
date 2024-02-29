<script setup>
import { getGoogleUrl } from '../utils/getGoogleUrl';
import {redirectToAuthCodeFlow} from "@/utils/spotifyUtils.js";
import ServiceLoginButton from "@/components/formFields/ServiceLoginButton.vue";
import Test from "@/components/formFields/OtherServicesLoginButtons.vue";


const clientId = "a534b97e062943c5913256751ee1dc53";
const from = '/';
</script>

<template>
  <div class="loginFormContainer">
    <div class="loginFormSubContainer">
      <h1>Sign in</h1>
      <div class="otherThirdPartySigningServices">
        <ServiceLoginButton class="serviceLoginButton" title="Sign in with Spotify" service-class="btn-spotify" icon="bi-spotify" :service-url="redirectToAuthCodeFlow"/>
        <ServiceLoginButton class="serviceLoginButton" title="Sign in with Apple Music" service-class="btn-applemusic" icon="bi-music-note-beamed" :service-url="redirectToAuthCodeFlow"/>
        <ServiceLoginButton class="serviceLoginButton" title="Sign in with Tidal" service-class="btn-tidal" :is-local-image-icon="true" alt="Tidal icon" local-image-src="src/assets/icons8-tidal-50.png" :service-url="redirectToAuthCodeFlow"/>
        <ServiceLoginButton class="serviceLoginButton" title="Sign in with YouTube Music" service-class="btn-youTubeMusic" :is-local-image-icon="true" alt="YouTube Music icon" local-image-src="src/assets/youtube-music.svg" :service-url="redirectToAuthCodeFlow"/>
<!--        <Test />-->
<!--        <a :href="getGoogleUrl(from)" title="Sign in with other music services" class="btn btn-otherServices">-->
<!--          <span class="name">Sign in with Other Music Streaming Services</span>-->
<!--          <i class="bi bi-chevron-compact-down"></i>-->
<!--        </a>-->
      </div>
      <p class="disclaimer">If you are signing in with an identity provider and are not a PlaylistTranfer user, you will be registered and you will need to agree to Playlist <a href="#">Terms & Conditions Terms & Conditions</a>.<br/><br/>
        This site is protected by reCAPTCHA and the <a href="#">Google Privacy Policy</a> and <a href="#">Terms of Service</a> apply.
      </p>
    </div>
  </div>
</template>

<style scoped>
.loginFormContainer {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.loginFormSubContainer {
  background-color: #121212;
  color: #FFFFFF;
  width: 550px;
  height: 750px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
}

.loginFormSubContainer h1 {
  margin-bottom: 10px;
}

.disclaimer {
  font-size: 12px;
  width: 450px;
  margin-top: 20px;
}

.serviceLoginButton {
  margin-bottom: 6px;
}

</style>