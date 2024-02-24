<script setup>
import NavBar from "@/components/NavBar.vue";
import HomeBody from "@/components/HomeBody.vue";
import Footer from "@/components/Footer.vue";
import {onMounted} from "vue";
import { useApiDataStore } from "@/utils/globalAppStates.js"

const clientId = "a534b97e062943c5913256751ee1dc53";
const dataStore = useApiDataStore();

</script>

<template>
  <NavBar />
  <HomeBody />
  <Footer />
</template>

<style scoped>

</style>