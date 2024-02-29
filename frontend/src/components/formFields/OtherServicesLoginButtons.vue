<script setup>
import { ref } from 'vue';
import {redirectToAuthCodeFlow} from "@/utils/spotifyUtils.js";
import ServiceLoginButton from "@/components/formFields/ServiceLoginButton.vue";

const show = ref("");
const modalStyles = ref(null);

function showModal() {
  modalStyles.value = "display: block";
  setTimeout(() => show.value = "show", 0)
}

function hideModal() {
  show.value = "";
}
</script>

<template>
  <div>
    <button class="btn" @click="showModal">
      Sign in with Other Music Streaming Services
      <i class="bi bi-chevron-compact-down"></i>
    </button>
    <div class="modal" :class="show" v-bind:style="modalStyles">
      <button class="close" @click="hideModal">
        <svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g clip-path="url(#clip0_7_7)">
            <path d="M25.5 8.5L8.5 25.5" stroke="#DADADA" stroke-width="2.125" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M9 9L26 26" stroke="#DADADA" stroke-width="2.125" stroke-linecap="round" stroke-linejoin="round"/>
          </g>
          <defs>
            <clipPath id="clip0_7_7">
              <rect width="34" height="34" fill="white"/>
            </clipPath>
          </defs>
        </svg>
      </button>

      <ServiceLoginButton class="serviceLoginButton" title="Sign in with Apple Music" service-class="btn-applemusic" icon="bi-music-note-beamed" :service-url="redirectToAuthCodeFlow"/>
      <ServiceLoginButton class="serviceLoginButton" title="Sign in with Tidal" service-class="btn-tidal" :is-local-image-icon="true" alt="Tidal icon" local-image-src="src/assets/icons8-tidal-50.png" :service-url="redirectToAuthCodeFlow"/>
      <ServiceLoginButton class="serviceLoginButton" title="Sign in with YouTube Music" service-class="btn-youTubeMusic" :is-local-image-icon="true" alt="YouTube Music icon" local-image-src="src/assets/youtube-music.svg" :service-url="redirectToAuthCodeFlow"/>
    </div>
  </div>
</template>

<style scoped>
.btn {
  font-weight: 600;
  color: #FFFFFF;
  width: 450px;
  height: 50px;
  border-radius: 3px;
  cursor: pointer;
  font-size: 16px;
  line-height: 15px;
  padding: 0px 25px;

  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  background-color: #383838;
}

.bi {
  font-size: 25px;
}

button {
  background: transparent;
  border: none;
  font-family: inherit;
  color: inherit;
  cursor: pointer;
}

.modal {
  display: none;
  position: fixed;
  top: 28%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0.5);
  background-color: yellow;
  color: #fff;
  padding: 5px;
  width: 450px;
  max-width: 600px;
  border-radius: 3px;
  opacity: 0;
  transition: 0.2s;
}
.modal.show {
  opacity: 1;
  transform: translate(-50%, -50%) scale(1);
}
.modal .close {
  margin-inline-start: auto;
  width: 20px;
  height: 20px;
  display: block;
  cursor: pointer;
}

.serviceLoginButton {
  width: 100%;
  margin-top: 6px;
}

</style>