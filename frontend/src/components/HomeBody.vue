<script setup>

</script>

<template>
<div class="landingPageBody">
  <h1>Playlist Transfer</h1>
  <h5>Transfer your playlists across your music streaming platforms </h5>
  <h3>Coming Soon</h3>
  <div class="subscribeContainer">
    <input id="email" placeholder="Enter your email" type="email"/>
    <input id="notifyMe" value="Notify Me" type="button" />
  </div>
</div>
</template>

<style scoped>
.landingPageBody {
  background-image: url('../assets/womanListeningToMusic.jpg');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  height: 850px;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #ffffff;
}

h1 {
  font-size: 64px;
  font-weight: 700;
  margin-top: 200px;
  margin-bottom: 0;
  text-align: left;
  letter-spacing: 3px;
}

h5 {
  margin-top: 0;
  font-weight: 700;
  font-size: 24px;
  width: 500px;
  text-align: left;
}

h3 {
  color: #FFF;
  font-size: 40px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  margin-top: 30px;
  margin-bottom: 100px;
}

.subscribeContainer {
  display: flex;
  align-content: space-between;
  align-items: self-start;
}

.subscribeContainer input {
  border: none;
}

#email {
  width: 305px;
  height: 53px;
  flex-shrink: 0;
  border-radius: 15px;
  background: rgba(255, 255, 255, 0.50);
  padding: 0 8px;

  color: #000000;
  font-size: 20px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}

#notifyMe {
  width: 103px;
  height: 53px;
  flex-shrink: 0;

  border-radius: 15px;
  background: #000;

  color: #FFF;
  font-size: 20px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  margin-left: 15px;
}

</style>