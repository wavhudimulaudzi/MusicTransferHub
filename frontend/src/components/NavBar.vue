<script setup>
import {useApiDataStore} from "@/utils/globalAppStates.js";

const dataStore = useApiDataStore();
</script>

<template>
<nav>
  <div>
    <img src="../assets/logo.svg" alt="playlistTransfer logo"/>
  </div>
  <ul>
    <li id="login" key="login" v-if="dataStore.getSpotifyAccessToken === null">
      <router-link to="login">Login</router-link>
    </li>
    <li id="buyMeCoffee" key="buyMeCoffee">
      <router-link to="donate">Buy Me Coffee</router-link>
    </li>
    <li id="termsOfUse" key="termsOfUse">
      <router-link to="termsofuse">Terms of Use</router-link>
    </li>
  </ul>
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