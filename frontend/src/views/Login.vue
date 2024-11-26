<template>
  <div class="login-page">
    <div class="top-spacing"></div>
    
    <div class="main-content">
      <div class="container">
        <div class="login-container">
          <div class="login-header">
            <h2>會員登入</h2>
            <p>歡迎回到 HRV 睡眠檢測平台</p>
          </div>
          
          <div class="login-box">
            <div v-if="error" class="error-message">
              <i class="fas fa-exclamation-circle"></i>
              {{ error }}
            </div>
            
            <form @submit.prevent="handleLogin">
              <div class="form-group">
                <label for="username">
                  <i class="fas fa-user"></i>
                  帳號
                </label>
                <input 
                  type="text" 
                  id="username" 
                  v-model="form.username" 
                  required
                  placeholder="請輸入帳號"
                >
              </div>
              
              <div class="form-group">
                <label for="password">
                  <i class="fas fa-lock"></i>
                  密碼
                </label>
                <input 
                  type="password" 
                  id="password" 
                  v-model="form.password" 
                  required
                  placeholder="請輸入密碼"
                >
              </div>
              
              <div class="form-actions">
                <button type="submit" class="btn btn-primary">
                  <i class="fas fa-sign-in-alt"></i>
                  登入
                </button>
                <router-link to="/register" class="btn btn-outline">
                  <i class="fas fa-user-plus"></i>
                  註冊新帳號
                </router-link>
              </div>
            </form>
            
            <div class="help-links">
              <a href="#"><i class="fas fa-question-circle"></i> 忘記密碼</a>
              <a href="#"><i class="fas fa-info-circle"></i> 使用說明</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 頁尾 -->
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-info">
            <p>聯絡地址：112303 臺北市北投區明德路365號 學思樓10樓 F1033 生醫資訊實驗室</p>
            <p>服務電話：(02)2822-7101 轉 1237</p>
            <p>本平台服務時間：週一至週五 09:00-18:00</p>
          </div>
        </div>
        <div class="copyright">
          Copyright © 2024 HRV Sleep Monitoring Platform. All rights reserved.
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginView',
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      error: null
    }
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post('/api/login/', this.form)
        if (response.data.success) {
          localStorage.setItem('token', response.data.token)
          this.$router.push('/home')
        }
      } catch (error) {
        this.error = '帳號或密碼錯誤'
      }
    }
  }
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  background: var(--neutral-100);
}

.top-spacing {
  height: 80px;
}

.main-content {
  padding: 2rem 0;
}

.login-container {
  max-width: 480px;
  margin: 0 auto;
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.login-header {
  text-align: center;
  margin-bottom: 2rem;
}

.login-header h2 {
  font-size: 1.8rem;
  color: var(--primary-dark);
  margin-bottom: 0.5rem;
}

.login-header p {
  color: var(--neutral-400);
}

.login-box {
  background: #fff;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #333;
  font-weight: 500;
}

label i {
  margin-right: 0.5rem;
  color: #1a4f7b;
}

input {
  width: 100%;
  padding: 0.8rem 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

input:focus {
  outline: none;
  border-color: #1a4f7b;
}

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.btn {
  flex: 1;
  padding: 0.8rem;
  border-radius: 4px;
  border: none;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  text-decoration: none;
}

.btn-primary {
  background: #1a4f7b;
  color: #fff;
}

.btn-outline {
  background: #fff;
  border: 1px solid #1a4f7b;
  color: #1a4f7b;
}

.help-links {
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid #eee;
  display: flex;
  justify-content: center;
  gap: 2rem;
}

.help-links a {
  color: #666;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.error-message {
  background: #fff3f3;
  color: #dc3545;
  padding: 1rem;
  border-radius: 4px;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.footer {
  background: #1a4f7b;
  color: #fff;
  padding: 2rem 0;
  margin-top: auto;
}

.footer-content {
  margin-bottom: 1rem;
}

.copyright {
  text-align: center;
  padding-top: 1rem;
  border-top: 1px solid rgba(255,255,255,0.1);
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .main-content {
    padding: 2rem 1rem;
  }
  
  .form-actions {
    flex-direction: column;
  }
  
  .help-links {
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }
}
</style>
