<script setup>
import ComingSoonBody from "@/components/ComingSoonBody.vue";
</script>

<template>
<!--<ComingSoonBody />-->
  <div class="homeBodyContainer">
    <div class="playlistContainer">
      <div class="playlistsTransferContainer">
        <p>Your Spotify Playlists</p>
        <input type="button" value="SignIn with other music service" />
        <input type="button" value="Transfer To Apple Music" />
      </div>
      <div class="playlistInfoHeader">
        <p>Title</p>
        <p>Tracks</p>
        <p>Creator</p>
      </div>
      <div class="playlistCard">
        <input type="checkbox" />
        <img src="#" alt="Playlist Icon" />
        <p>2014 Forest Hills Drive</p>
        <p>15</p>
        <p>You</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.homeBodyContainer {
  height: 100vh;
  display: flex;
  justify-content: center;
}

.playlistContainer {
  width: 1132px;
  height: 595px;
  background: #1DB954;
  border-radius: 25px;
}

</style>