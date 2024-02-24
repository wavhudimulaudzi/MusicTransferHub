import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from "@/router/index.js";
// import dotenv from 'dotenv';

// dotenv.config();

// Initialize the Google Sign-In API
const app = createApp(App);
const pinia = createPinia();
app.use(router);
app.use(pinia);
app.mount('#app');
