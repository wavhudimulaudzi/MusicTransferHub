<script setup>
import { getGoogleUrl } from '../utils/getGoogleUrl';
import {redirectToAuthCodeFlow} from "@/utils/spotifyUtils.js";


const clientId = "a534b97e062943c5913256751ee1dc53";
const from = '/';
</script>

<template>
  <div class="loginFormContainer">
    <div class="loginFormSubContainer">
      <h1>Sign in</h1>
      <div class="otherThirdPartySigningServices">
        <a @click="redirectToAuthCodeFlow(clientId)" data-servicename="spotify" title="Sign in with spotify" class="btn btn-spotify">
          <i class="bi bi-spotify"></i>
          <span class="name">Sign in with Spotify</span>
        </a>
        <a :href="getGoogleUrl(from)" data-servicename="applemusic" title="Sign in with Apple Music" class="btn btn-applemusic">
          <i class="bi bi-music-note-beamed"></i>
          <span class="name">Sign in with Apple Music</span>
        </a>
        <a :href="getGoogleUrl(from)" data-servicename="tidal" title="Sign in with Tidal" class="btn btn-tidal">
          <img src="../assets/icons8-tidal-50.png" alt="Tidal icon" width="25px" height="25px"/>
          <span class="name">Sign in with Tidal</span>
        </a>
        <a :href="getGoogleUrl(from)" data-servicename="otherServices" title="Sign in with other music services" class="btn btn-otherServices">
          <span class="name">Sign in with Other Music Streaming Services</span>
          <i class="bi bi-chevron-compact-down"></i>
        </a>
      </div>
      <div class="form-separator">
        <hr class="separator-hr">
        <span class="separator-message">OR</span>
        <hr class="separator-hr">
      </div>
      <div class="subFormContainer">
        <form action="#">
          <div class="input-box">
            <i class="bi bi-person"></i>
            <input type="email" id="email" placeholder=" " class="input"/>
            <div class="cut"></div>
            <label for="email" class="placeholder">Email</label>
          </div>
          <div class="input-box">
            <i class="bi bi-key"></i>
            <input type="password" id="password" placeholder=" " class="input"/>
            <div class="cut"></div>
            <label for="password" class="placeholder">Password</label>
          </div>
        </form>
        <a href="#" class="forgotLink">Forgot password?</a>
      </div>
      <div class="loginBtnContainer">
        <input type="button" value="Log in" id="loginBtn">
        <div class="signupContainer">
          <p>Don't have an account?</p>
          <a href="#">Sign up</a>
        </div>
      </div>
      <p class="disclaimer">If you are signing in with an identity provider and are not a PlaylistTranfer user, you will be registered and you will need to agree to Playlist <a href="#">Terms & Conditions Terms & Conditions</a>.<br/><br/>
        This site is protected by reCAPTCHA and the <a href="#">Google Privacy Policy</a> and <a href="#">Terms of Service</a> apply.
      </p>
    </div>
  </div>
</template>

<style scoped>
.loginFormContainer {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.loginFormSubContainer {
  background-color: #121212;
  color: #FFFFFF;
  width: 550px;
  height: 750px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  //justify-content: space-between;
  align-items: center;
  padding: 10px;
}

.loginFormSubContainer h1 {
  margin-bottom: 10px;
}

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

.btn {
  font-weight: 600;
  color: #FFFFFF;
  width: 450px;
  height: 50px;
  //border: 1px solid transparent;
  border-radius: 3px;
  cursor: pointer;
  font-size: 20px;
  line-height: 15px;
  padding: 0px 25px;

  background-color: #4285f4;
  border-color: #4285f4;
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 10px;
}

.btn:hover {
  text-decoration: none;
}

.btn-spotify {
  background-color: #1DB954;
  border-color: #1DB954;
}

.btn-applemusic {
  background-color: #ff2d55;
  border-color: #ff2d55;
}

.btn-tidal {
  background-color: #000000;
  border-color: #000000;
}

.btn-otherServices {
  font-size: 16px;
  line-height: 20px;
  background-color: #383838;
  border-color: #383838;
}

.bi {
  font-size: 25px;
}

.name {
  margin: 0 auto;
}

form {
  display: flex;
  flex-direction: column;
}

form input {
  background: none;
  border: none;
  width: 100%;
  outline: 0;

  color: #FFFFFF;
  font-size: 20px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}

.input-box {
  border: 1px solid rgba(255, 255, 255, 0.50);
  border-radius: 15px;
  width: 450px;
  height: 52px;
  padding: 0 10px;
  display: flex;
  align-items: center;
  margin: 15px 0;
  position: relative;
}

.cut {
  background-color: #121212;
  border-radius: 10px;
  height: 20px;
  left: 55px;
  position: absolute;
  top: -25px;
  transform: translateY(0);
  transition: transform 200ms;
  width: 76px;
  outline: none;
}

.input:focus ~ .cut,
.input:not(:placeholder-shown) ~ .cut {
  transform: translateY(12px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.50);
}

.placeholder {
  color: #65657b;
  font-family: sans-serif;
  left: 55px;
  line-height: 14px;
  pointer-events: none;
  position: absolute;
  transform-origin: 0 50%;
  transition: transform 200ms, color 200ms;
  top: 20px;
}

.input:focus ~ .placeholder,
.input:not(:placeholder-shown) ~ .placeholder {
  transform: translateY(-30px) translateX(10px) scale(0.75);
}

.input:not(:placeholder-shown) ~ .placeholder {
  color: #808097;
}

.input:focus ~ .placeholder {
  color: #054bee;
}

.input-box .bi {
  width: 45px;
  height: 100%;
  padding: 10px;
}

.input-box:nth-of-type(2) {
  margin-bottom: 0;
}

.forgotLink {
  font-size: 14px;
  letter-spacing: 1px;
}

#loginBtn {
  width: 450px;
  height: 52px;
  border-radius: 15px;
  border: none;
  font-size: 22px;
  font-weight: 500;
}

.loginBtnContainer {
  margin-top: 25px;
}

.signupContainer {
  display: flex;
  letter-spacing: 1px;
  font-size: 14px;
}

.signupContainer p {
  margin: 0;
  margin-right: 10px;
}

.disclaimer {
  font-size: 12px;
  width: 450px;
  margin-top: 20px;
}

</style>