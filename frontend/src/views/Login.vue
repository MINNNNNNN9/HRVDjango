<template>
  <div class="login-page">
    <div class="geometric-elements">
      <div class="geo-item square"></div>
      <div class="geo-item circle"></div>
      <div class="geo-item rectangle"></div>
      <div class="geo-item square-small"></div>
      <div class="geo-item circle-small"></div>
    </div>

    <div class="content-container">
      <div class="login-card">
        <h2 class="login-title">使用者登入</h2>
        <p class="login-subtitle">登入後進入睡眠監測系統</p>
        
        <form @submit.prevent="handleLogin" class="login-form">
          <div class="input-group">
            <input 
              type="text"
              v-model="form.username"
              placeholder="請輸入帳號"
              required
            >
          </div>

          <div class="input-group">
            <input 
              type="password"
              v-model="form.password"
              placeholder="請輸入密碼"
              required
            >
          </div>

          <button type="submit" class="login-btn">登入</button>
        </form>

        <div class="form-footer">
          <router-link to="/register" class="register-link">註冊帳號</router-link>
          <a href="#" class="help-link">登入說明</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      error: ''
    }
  },
  methods: {
    async handleLogin() {
      try {
        this.error = '';
        
        console.log('準備發送登入請求：', {
          username: this.form.username,
          password: this.form.password
        });

        const response = await this.$axios.post('/api/auth/login/', {
          username: this.form.username,
          password: this.form.password
        });

        console.log('登入響應：', response);

        if (response.data) {
          // 登入成功，儲存用戶資訊
          this.$store.commit('setUser', response.data.user);
          this.$router.push('/');
        }
      } catch (error) {
        console.error('登入錯誤：', error);
        if (error.response) {
          this.error = error.response.data.message || '登入失敗';
        } else if (error.request) {
          this.error = '無法連接到伺服器，請檢查網路連接';
        } else {
          this.error = '登入過程發生錯誤，請稍後再試';
        }
      }
    }
  }
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  background: #1E2128;
  color: white;
  display: flex;
  flex-direction: column;
}

.platform-title {
  text-align: center;
  padding: 2rem 0;
}

.platform-title h1 {
  color: #8BC34A;
  font-size: 3rem;
  margin-bottom: 0.5rem;
}

.platform-title p {
  color: #666;
  font-size: 1.2rem;
}

.content-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  position: relative;
  z-index: 1;
}

.login-card {
  background: rgba(40, 44, 52, 0.9);
  backdrop-filter: blur(10px);
  padding: 3rem;
  border-radius: 12px;
  width: 400px;
  border: 1px solid rgba(139, 195, 74, 0.2);
  position: relative;
  z-index: 2;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.2),
              0 0 10px rgba(139, 195, 74, 0.1);
}

.login-title {
  color: #8BC34A;
  font-size: 2rem;
  margin-bottom: 0.5rem;
  text-align: center;
}

.login-subtitle {
  color: #666;
  font-size: 1.1rem;
  margin-bottom: 2rem;
  text-align: center;
}

.input-group {
  margin-bottom: 1.5rem;
}

.input-group input {
  width: 100%;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(139, 195, 74, 0.5);
  border-radius: 6px;
  color: white;
  font-size: 1.1rem;
}

.input-group input:focus {
  outline: none;
  border-color: #8BC34A;
  box-shadow: 0 0 10px rgba(139, 195, 74, 0.2);
}

.login-btn {
  width: 100%;
  padding: 1rem;
  background: #8BC34A;
  border: none;
  border-radius: 6px;
  color: white;
  cursor: pointer;
  font-size: 1.2rem;
  margin-top: 1.5rem;
  transition: all 0.3s ease;
}

.login-btn:hover {
  background: #9CCC65;
  transform: translateY(-2px);
}

.form-footer {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
  font-size: 1rem;
}

.form-footer a {
  color: #8BC34A;
  text-decoration: none;
  transition: color 0.3s ease;
}

.form-footer a:hover {
  color: #9CCC65;
}

.geometric-elements {
  position: fixed;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}

.geo-item {
  position: absolute;
  border: 1px solid rgba(139, 195, 74, 0.15);
  opacity: 1.85;
}

.square {
  width: 100px;
  height: 100px;
  top: 20%;
  left: 15%;
  animation: floatAnimation 8s infinite ease-in-out;
}

.circle {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  top: 60%;
  right: 15%;
  animation: floatAnimation 10s infinite ease-in-out;
}

.rectangle {
  width: 150px;
  height: 80px;
  top: 40%;
  right: 25%;
  animation: floatAnimation 12s infinite ease-in-out;
}

.square-small {
  width: 60px;
  height: 60px;
  bottom: 20%;
  left: 25%;
  animation: floatAnimation 9s infinite ease-in-out;
}

.circle-small {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  top: 30%;
  right: 35%;
  animation: floatAnimation 11s infinite ease-in-out;
}

@keyframes floatAnimation {
  0%, 100% {
    transform: translate(0, 0) rotate(0deg);
  }
  25% {
    transform: translate(-10px, 10px) rotate(5deg);
  }
  50% {
    transform: translate(0, -15px) rotate(0deg);
  }
  75% {
    transform: translate(10px, 5px) rotate(-5deg);
  }
}

.geo-item::after {
  content: '';
  position: absolute;
  top: -2px;
  left: -2px;
  right: -2px;
  bottom: -2px;
  border-radius: inherit;
  background: rgba(139, 195, 74, 0.1);
  filter: blur(4px);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.geo-item:hover::after {
  opacity: 1;
}

@media (max-width: 768px) {
  .login-card {
    width: 90%;
    padding: 2rem;
  }
  
  .platform-title h1 {
    font-size: 2rem;
  }
  
  .platform-title p {
    font-size: 1rem;
  }

  .geometric-elements {
    display: none;
  }
}
</style>
