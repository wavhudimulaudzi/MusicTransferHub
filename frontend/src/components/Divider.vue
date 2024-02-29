<script setup>

</script>

<template>
  <div class="form-separator">
    <hr class="separator-hr">
    <span class="separator-message">OR</span>
    <hr class="separator-hr">
  </div>
</template>

<style scoped>
.form-separator {
  display: flex;
  flex-direction: row;
  padding: 0 8px 8px 8px;
}

.separator-hr {
//border: none;
  border-top: 1px solid #6b7185;
  flex-basis: auto;
  flex-grow: 1;
  flex-shrink: 1;
  height: 0;
  width: 205px;
  margin: auto 0;
}

.separator-message {
  margin: 0px 5px;
}
</style>