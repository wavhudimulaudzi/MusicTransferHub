import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router/index.js";
// import dotenv from 'dotenv';

// dotenv.config();

// Initialize the Google Sign-In API
const app = createApp(App);
app.use(router).mount('#app')
