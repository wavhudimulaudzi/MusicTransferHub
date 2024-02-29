<script setup>
import ComingSoonBody from "@/components/ComingSoonBody.vue";
import PlaylistTile from "@/components/PlaylistTile.vue";
import OtherServicesLoginButtons from "@/components/formFields/OtherServicesLoginButtons.vue";

</script>

<template>
<!--<ComingSoonBody />-->
  <div class="homeBodyContainer">
    <div class="playlistContainer">
      <div class="playlistsTransferContainer">
        <p>Your Spotify Playlists</p>
        <OtherServicesLoginButtons />
        <input type="button" value="Transfer To Apple Music" />
      </div>
      <div class="playlistInfoHeader">
        <div class="blankSpace"></div>
        <p class="title">Title</p>
        <div class="otherHeaders">
          <p>Tracks</p>
          <p>Creator</p>
          <p>Types</p>
        </div>
        <div class="actions"></div>
      </div>
      <PlaylistTile title="Amukelani" tracks="20" creator="You" type="Private"/>
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

.playlistsTransferContainer {
  background: #FFFFFF;
  display: flex;
  justify-content: space-between;
  padding: 10px;
  border-radius: 25px 25px 0 0;
}

.playlistsTransferContainer p {
  color: #000000;
  font-weight: bold;
}

.playlistInfoHeader {
  color: #FFFFFF;
  font-size: 20px;
  display: flex;
  border-bottom: 1px solid #49E27F;
  border-top: 1px solid #49E27F;
  padding: 3px 10px;
}

.blankSpace {
  width: 10vw;
}

.title {
  width: 42vw;
}

.otherHeaders {
  display: flex;
  justify-content: space-between;
  width: 40vw;
}

.actions {
  width: 8vw;
}

</style>