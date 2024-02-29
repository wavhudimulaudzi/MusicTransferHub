<script setup>

import {redirectToAuthCodeFlow} from "@/utils/spotifyUtils.js";

const clientId = "a534b97e062943c5913256751ee1dc53";

const props = defineProps({
  title: String,
  serviceClass: String,
  serviceUrl: Function,
  icon: String,
  isLocalImageIcon: Boolean,
  localImageSrc: String,
  alt: String
})
</script>

<template>
  <a @click="serviceUrl(clientId)" :title="title" class="btn" :class="serviceClass">
    <img v-if="isLocalImageIcon" :src="localImageSrc" :alt="alt" width="25px" height="25px">
    <i v-else class="bi" :class="icon"></i>
    <span class="name">{{ title }}</span>
  </a>
</template>

<style scoped>
.btn {
  font-weight: 600;
  color: #FFFFFF;
  width: 450px;
  height: 50px;
//border: 1px solid transparent;
  border-radius: 3px;
  cursor: pointer;
  font-size: 20px;
  line-height: 15px;
  padding: 0px 25px;

  display: flex;
  flex-direction: row;
  align-items: center;
  //margin-bottom: 10px;
}

.btn:hover {
  text-decoration: none;
}

.btn-spotify {
  background-color: #1DB954;
  border-color: #1DB954;
}

.btn-applemusic {
  background-color: #ff2d55;
  border-color: #ff2d55;
}

.btn-tidal {
  background-color: #000000;
  border-color: #000000;
}

.btn-otherServices {
  font-size: 16px;
  line-height: 20px;
  background-color: #383838;
  border-color: #383838;
}

.btn-youTubeMusic {
  background-color: #FF0000;
  border-color: #FF0000;
}

.bi {
  font-size: 25px;
}

.name {
  margin: 0 auto;
}
</style>