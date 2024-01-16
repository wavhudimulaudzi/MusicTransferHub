<script setup>
import { getGoogleUrl } from '../utils/getGoogleUrl';

const from = '/';
</script>

<template>
  <div class="loginFormContainer">
    <div class="loginFormSubContainer">
      <h1>Sign in</h1>
      <div class="otherThirdPartySigningServices">
        <a :href="getGoogleUrl(from)" data-servicename="google" title="Sign in with Google" class="btn-google">
          <i class="bi bi-google"></i>
          <span class="name">Sign in with Google</span></a>
      </div>
      <div class="form-separator">
        <hr class="separator-hr">
        <span class="separator-message">OR</span>
        <hr class="separator-hr">
      </div>
      <div class="subFormContainer">
        <form action="#">
          <input type="email" id="email" placeholder="Enter your email" />
          <input type="password" id="password" placeholder="Password" />
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
}

.loginFormSubContainer {
  background-color: #121212;
  color: #FFFFFF;
  width: 550px;
  height: 750px;
  border-radius: 20px;
  display: flex;
  margin-top: 100px;
  flex-direction: column;
  //justify-content: space-between;
  align-items: center;
  padding: 10px;
}

form {
  display: flex;
  flex-direction: column;
}

form input {
  width: 430px;
  height: 52px;
  flex-shrink: 0;
  border-radius: 15px;
  background: rgba(255, 255, 255, 0.50);
  padding: 0 8px;
  border: none;

  color: #FFFFFF;
  font-size: 20px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}

#email {
  margin-bottom: 15px;
}

.forgotLink {
  font-size: 18px;
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
  margin-top: 30px;
}

.signupContainer {
  display: flex;
  letter-spacing: 1px;
}

.signupContainer p {
  margin: 0;
  margin-right: 10px;
}

.disclaimer {
  font-size: 14px;
  width: 450px;
}

.form-separator {
  display: flex;
  flex-direction: row;
  padding: 8px 0;
}

.separator-hr {
  //border: none;
  border-top: 1px solid #6b7185;
  flex-basis: auto;
  flex-grow: 1;
  flex-shrink: 1;
  height: 0;
  width: 205px;
}

.separator-message {
  margin: 0 5px;
}

.otherThirdPartySigningServices a {
  font-weight: 600;
  color: #FFFFFF;
  width: 425px;
  height: 50px;
  border: 1px solid transparent;
  border-radius: 3px;
  cursor: pointer;
  font-size: 20px;
  line-height: 15px;
  padding: 0px 10px;
}

.otherThirdPartySigningServices a:hover {
  text-decoration: none;
}

.btn-google {
  background-color: #4285f4;
  border-color: #4285f4;
  display: flex;
  flex-direction: row;
  align-items: center;
}

.name {
  margin-left: 120px;
}

</style>