<script setup>

</script>

<template>
  <div>
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
  </div>
</template>

<style scoped>
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
</style>