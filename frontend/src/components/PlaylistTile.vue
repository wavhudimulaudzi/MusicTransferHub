<script setup>
import Checkbox from "@/components/formFields/Checkbox.vue";

const props = defineProps({
  title: String,
  tracks: Number,
  creator: String,
  type: String,
  imageSrc: String
})
</script>

<template>
  <div class="playlistTile">
    <div class="blankSpace">
      <Checkbox />
      <img :src="imageSrc" alt="Playlist Icon" class="playlistImage"/>
    </div>
    <p class="title">{{ title }}</p>
    <div class="otherHeaders">
      <p>{{ tracks }}</p>
      <p>{{ creator }}</p>
      <p>{{ type }}</p>
    </div>
    <div class="actions"></div>
  </div>
</template>

<style scoped>
.playlistTile {
  display: flex;
  align-items: center;
  height: 75px;
  border-bottom: 1px solid #117033;
  padding: 0 10px;
  color: #FFFFFF;
}

.playlistImage {
  width: 60px;
  height: 60px;
}

.blankSpace {
  width: 10vw;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

.title {
  width: 42vw;
}

.otherHeaders {
  display: flex;
  justify-content: space-between;
  width: 40vw;
}

.otherHeaders p {
  text-align: center;
}

.actions {
  width: 8vw;
}

</style>