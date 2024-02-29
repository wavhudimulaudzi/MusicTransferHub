<script setup>

</script>

<template>
  <div class="container">
    <input type="checkbox" id="musicCheckbox">
  </div>
</template>

<style scoped>
input[type="checkbox"] {
  width: 24px;
  height: 24px;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border: 2px solid #A1F0BD;
  border-radius: 50%;
  outline: none;
  cursor: pointer;
  position: relative;
}

input[type="checkbox"]:checked::before {
  content: "";
  width: 16px;
  height: 16px;
  background-color: #A1F0BD;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 50%;
}
</style>