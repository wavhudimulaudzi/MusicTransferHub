<script setup>
const props = defineProps({
  profileImageUrl: {
    type: String,
    default: "/src/assets/Luffy🔥.jpeg"
  },
  userFullName: String,
  platformName: String,
  platformClass: String,
  userEmailAddress: String
})
</script>

<template>
  <div class="profileCardMainContainer" :class="platformClass">
    <img :src="profileImageUrl" alt="profile image" class="profileImage">
    <div class="profileInfo">
      <p class="name">{{ userFullName }}</p>
      <p class="platformLoggedWith">{{ platformName }}</p>
      <p class="email">{{ userEmailAddress }}</p>
    </div>
  </div>
</template>

<style scoped>

.profileCardMainContainer {
  width: 282px;
  height: 80px;
  display: flex;
  border-radius: 50px;
}

.spotify {
  background: #1DB954;
}

.appleMusic {
  background: #ff2d55;
}

.tidal {
  background: #000000;
}

.profileImage {
  height: inherit;
  width: 80px;
  border-radius: inherit;
}

.profileInfo {
  padding: 10px;
  overflow: hidden;
  white-space: nowrap;
  width: 180px;
}

.name {
  color: #FFFFFF;
  font-weight: bold;
  font-size: 18px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 180px;
}

.platformLoggedWith {
  color: #DDDDDD;
  font-size: 16px;
  font-weight: 500;
}

.email {
  font-size: 14px;
  color: #CCCCCC;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 180px;
}

</style>