<script setup>
import {onMounted} from "vue";
import { useRouter } from 'vue-router';

onMounted(() => {
  const router = useRouter();
  var params = new URLSearchParams(window.location.search);
  var code = params.get("code");

  if (code !== undefined) {
    console.log('Before I push: ', code)
    router.push({name: 'home'})
  }
})
</script>

<template>

</template>

<style scoped>

</style>