<template>
  <div class="register-page">
    <div class="geometric-elements">
      <div class="geo-item square"></div>
      <div class="geo-item circle"></div>
      <div class="geo-item rectangle"></div>
      <div class="geo-item square-small"></div>
      <div class="geo-item circle-small"></div>
    </div>

    <div class="content-container">
      <div class="register-card">
        <h2 class="register-title">會員註冊</h2>
        <p class="register-subtitle">歡迎加入 HRV 睡眠監測平台</p>
        
        <form @submit.prevent="handleRegister" class="register-form">
          <div class="input-group">
            <input 
              type="text"
              v-model="form.username"
              placeholder="請輸入用戶名"
              required
            >
          </div>

          <div class="input-group">
            <input 
              type="email"
              v-model="form.email"
              placeholder="請輸入電子郵件"
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

          <div class="input-group">
            <input 
              type="password"
              v-model="form.confirmPassword"
              placeholder="請再次輸入密碼"
              required
            >
          </div>

          <button type="submit" class="register-btn">註冊</button>
        </form>

        <div class="form-footer">
          <div class="footer-buttons">
            <router-link to="/login" class="footer-btn back-btn">
              <i class="fas fa-arrow-left"></i>
              返回登入
            </router-link>
            <button class="footer-btn help-btn">
              <i class="fas fa-question-circle"></i>
              註冊說明
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegisterForm',
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
      },
      error: ''
    }
  },
  methods: {
    async handleRegister() {
      try {
        // 先清除之前的錯誤訊息
        this.error = '';
        
        // 基本驗證
        if (!this.form.username || !this.form.email || !this.form.password || !this.form.confirmPassword) {
          this.error = '請填寫所有必填欄位';
          return;
        }

        // 密碼驗證
        if (this.form.password !== this.form.confirmPassword) {
          this.error = '兩次輸入的密碼不相符';
          return;
        }

        // 添加請求前的日誌
        console.log('準備發送註冊請求，數據：', {
          username: this.form.username,
          email: this.form.email,
          password: this.form.password,
          confirm_password: this.form.confirmPassword
        });

        const response = await fetch('http://localhost:8000/api/auth/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.form.username,
            email: this.form.email,
            password: this.form.password,
            confirm_password: this.form.confirmPassword
          })
        });

        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.message || '註冊失敗');
        }

        // 註冊成功
        console.log('註冊成功：', data);
        alert('註冊成功！請登入');
        this.$router.push('/login');

      } catch (error) {
        console.error('註冊錯誤：', error);
        this.error = error.message || '註冊過程發生錯誤，請稍後再試';
      }
    }
  }
}
</script>

<style scoped>
/* 複製 Login.vue 的基本樣式，並修改相關類名 */
.register-page {
  min-height: 100vh;
  background: #1E2128;
  color: white;
  display: flex;
  flex-direction: column;
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

.register-card {
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

.register-title {
  color: #8BC34A;
  font-size: 2rem;
  margin-bottom: 0.5rem;
  text-align: center;
}

.register-subtitle {
  color: #666;
  font-size: 1.1rem;
  margin-bottom: 2rem;
  text-align: center;
}

/* 其他樣式與 Login.vue 相同，只需更改類名 */
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

.register-btn {
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

.register-btn:hover {
  background: #9CCC65;
  transform: translateY(-2px);
}

/* 幾何圖形動畫樣式，與 Login.vue 完全相同 */
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
  opacity: 0.85;
}

/* 複製 Login.vue 中的所有動畫相關樣式 */
.square, .circle, .rectangle, .square-small, .circle-small {
  /* 保持與 Login.vue 相同的動畫設置 */
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

/* 響應式設計 */
@media (max-width: 768px) {
  .register-card {
    width: 90%;
    padding: 2rem;
  }
  
  .geometric-elements {
    display: none;
  }
}

/* 保留原有樣式，添加新的按鈕樣式 */

.form-footer {
  margin-top: 2rem;
}

.footer-buttons {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
}

.footer-btn {
  flex: 1;
  padding: 0.8rem 1.2rem;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.back-btn {
  background: rgba(139, 195, 74, 0.1);
  border: 1px solid rgba(139, 195, 74, 0.3);
  color: #8BC34A;
}

.back-btn:hover {
  background: rgba(139, 195, 74, 0.2);
  transform: translateY(-2px);
}

.help-btn {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #666;
}

.help-btn:hover {
  background: rgba(255, 255, 255, 0.05);
  color: #8BC34A;
  transform: translateY(-2px);
}

/* 圖示樣式 */
.footer-btn i {
  font-size: 1rem;
}

/* 響應式調整 */
@media (max-width: 768px) {
  .footer-buttons {
    flex-direction: column;
  }
  
  .footer-btn {
    width: 100%;
  }
}
</style>

