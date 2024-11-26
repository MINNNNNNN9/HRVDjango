<template>
  <div class="register-page">
    <!-- 主要內容 -->
    <div class="main-content">
      <div class="container">
        <div class="register-container">
          <div class="register-header">
            <h2>會員註冊</h2>
            <p>歡迎加入 HRV 睡眠檢測平台</p>
          </div>
          
          <div class="register-box">
            <div v-if="error" class="error-message">
              <i class="fas fa-exclamation-circle"></i>
              {{ error }}
            </div>
            
            <form @submit.prevent="handleRegister">
              <div class="form-group">
                <label for="username">
                  <i class="fas fa-user"></i>
                  用戶名
                </label>
                <input 
                  type="text" 
                  id="username"
                  v-model="form.username"
                  required
                  placeholder="請輸入用戶名"
                >
              </div>

              <div class="form-group">
                <label for="email">
                  <i class="fas fa-envelope"></i>
                  電子郵件
                </label>
                <input 
                  type="email" 
                  id="email"
                  v-model="form.email"
                  required
                  placeholder="請輸入電子郵件"
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

              <div class="form-group">
                <label for="confirmPassword">
                  <i class="fas fa-lock"></i>
                  確認密碼
                </label>
                <input 
                  type="password" 
                  id="confirmPassword"
                  v-model="form.confirmPassword"
                  required
                  placeholder="請再次輸入密碼"
                >
              </div>
              
              <div class="form-actions">
                <button type="submit" class="btn btn-primary">
                  <i class="fas fa-user-plus"></i>
                  註冊
                </button>
                <router-link to="/login" class="btn btn-outline">
                  <i class="fas fa-sign-in-alt"></i>
                  返回登入
                </router-link>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>

    <!-- 頁尾 -->
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-info">
            <p>聯絡地址：112303 臺北市北投區明德路365號</p>
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
export default {
  name: 'RegisterAccount',
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
      },
      error: null
    }
  },
  methods: {
    async handleRegister() {
      try {
        if (this.form.password !== this.form.confirmPassword) {
          this.error = '兩次輸入的密碼不一致'
          return
        }

        const response = await this.$axios.post('/api/auth/register/', {
          username: this.form.username,
          email: this.form.email,
          password: this.form.password
        })

        if (response.data.success) {
          this.$router.push('/login')
        }
      } catch (error) {
        this.error = error.response?.data?.message || '註冊失敗，請稍後再試'
      }
    }
  }
}
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: #f5f5f5;
}

/* 使用與 Login.vue 相同的樣式 */
.main-content {
  flex: 1;
  padding: 3rem 0;
}

.register-container {
  max-width: 600px;
  margin: 0 auto;
}

.register-header {
  text-align: center;
  margin-bottom: 2rem;
}

.register-header h2 {
  color: #1a4f7b;
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.register-header p {
  color: #666;
}

.register-box {
  background: #fff;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

/* 其他樣式與 Login.vue 相同 */
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

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.btn {
  flex: 1;
  padding: 0.8rem;
  border-radius: 4px;
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
  border: none;
}

.btn-outline {
  background: #fff;
  border: 1px solid #1a4f7b;
  color: #1a4f7b;
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
}
</style>
