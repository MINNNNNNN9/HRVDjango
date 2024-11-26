<template>
  <nav class="navbar" :class="{ 'navbar-scrolled': isScrolled }">
    <div class="container navbar-container">
      <div class="nav-left">
        <router-link to="/" class="logo">
          <span class="gradient-text">HRV</span>
          <span>睡眠檢測平台</span>
        </router-link>
      </div>

      <div class="nav-center">
        <div class="language-switch">
          <a href="#" 
            :class="{ active: currentLanguage === 'zh' }"
            @click.prevent="changeLanguage('zh')"
          >中文</a>
          <span class="divider">|</span>
          <a href="#" 
            :class="{ active: currentLanguage === 'en' }"
            @click.prevent="changeLanguage('en')"
          >English</a>
        </div>
        <FontSizeAdjuster />
        <a href="#" class="accessibility-link">
          <i class="fas fa-universal-access"></i> 
          <span>無障礙設定</span>
        </a>
      </div>
      
      <div class="nav-right" :class="{ 'active': isMenuOpen }">
        <template v-if="isAuthenticated">
          <router-link to="/dashboard">儀表板</router-link>
          <router-link to="/analysis">分析報告</router-link>
          <router-link to="/profile">個人檔案</router-link>
          <button @click="handleLogout" class="btn btn-outline">
            <i class="fas fa-sign-out-alt"></i> 登出
          </button>
        </template>
        <template v-else>
          <router-link to="/login" class="login-link">
            <i class="fas fa-sign-in-alt"></i> 會員登入
          </router-link>
          <router-link to="/register" class="register-link">
            <i class="fas fa-user-plus"></i> 註冊帳號
          </router-link>
        </template>
      </div>
      
      <button class="menu-toggle" @click="toggleMenu">
        <i class="fas fa-bars"></i>
      </button>
    </div>
  </nav>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import FontSizeAdjuster from './FontSizeAdjuster.vue'

export default {
  name: 'NavigationBar',
  components: {
    FontSizeAdjuster
  },
  data() {
    return {
      isScrolled: false,
      isMenuOpen: false
    }
  },
  computed: {
    ...mapGetters('auth', ['isAuthenticated', 'username']),
    ...mapGetters('settings', ['currentLanguage'])
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
  },
  unmounted() {
    window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    ...mapActions('auth', ['logout']),
    ...mapActions('settings', ['changeLanguage']),
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen
    },
    async handleLogout() {
      try {
        await this.logout()
        this.$router.push('/login')
      } catch (error) {
        console.error('登出失敗', error)
      }
    },
    handleScroll() {
      this.isScrolled = window.scrollY > 50
    }
  }
}
</script>

<style scoped>
/* 導航欄初始狀態 */
.navbar {
  background: transparent; /* 初始透明背景 */
  backdrop-filter: blur(12px);
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
  padding: 1rem 0;
  transition: all 0.4s ease;
}

/* Logo 區域樣式 */
.nav-left .logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  font-size: 1.5rem;
  font-weight: 600;
}

/* HRV 文字漸層效果 */
.gradient-text {
  background: linear-gradient(135deg, #FF6B6B, #FF8787);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
  font-size: 1.8rem;
}

/* "睡眠檢測平台" 文字樣式 */
.logo span:not(.gradient-text) {
  color: #fff;  /* 設定為白色，與其他文字顏色一致 */
}

/* 滾動後的導航欄樣式 */
.navbar-scrolled {
  background: rgba(26, 41, 66, 0.98); /* 滾動後的深色背景 */
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

/* 導航欄容器 */
.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* 登入註冊按鈕樣式 */
.login-link,
.register-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.6rem;
  border-radius: 50px;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.3s ease;
}

.login-link {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.register-link {
  background: linear-gradient(135deg, #FF6B6B, #FF8787);
  color: white;
  margin-left: 0.8rem;
  box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
}

/* 按鈕懸停效果 */
.login-link:hover,
.register-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
}

.nav-center {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

/* 語言切換樣式 */
.language-switch {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.language-switch a {
  color: #fff;
  text-decoration: none;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  transition: all 0.3s ease;
  font-size: 0.95rem;
}

.language-switch a.active {
  background: rgba(255, 255, 255, 0.15);
}

.language-switch .divider {
  color: rgba(255, 255, 255, 0.5);
}

.accessibility-link {
  color: #fff;
  text-decoration: none;
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.1);
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.accessibility-link:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateY(-1px);
}

.menu-toggle {
  display: none;
  background: none;
  border: none;
  color: var(--light);
  font-size: 1.5rem;
  cursor: pointer;
}

@media (max-width: 768px) {
  .menu-toggle {
    display: block;
  }

  .nav-center,
  .nav-right {
    display: none;
  }

  .nav-right.active {
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: var(--dark);
    padding: 1rem;
    gap: 1rem;
  }

  .language-switch {
    flex-direction: column;
    align-items: flex-start;
  }

  .accessibility-link span {
    display: none;
  }
}

/* 字體大小調整器樣式 */
:deep(.font-size-adjuster) {
  position: relative;
  display: inline-block;
}

:deep(.font-size-adjuster .dropdown-toggle) {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
}

:deep(.font-size-adjuster .dropdown-toggle:hover) {
  background: rgba(255, 255, 255, 0.15);
}

:deep(.font-size-adjuster .dropdown-menu) {
  position: absolute;
  top: 100%;
  right: 0;
  background: white;
  border-radius: 4px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  padding: 0.5rem 0;
  min-width: 150px;
  z-index: 1000;
}

:deep(.font-size-adjuster .dropdown-menu a) {
  display: block;
  padding: 0.5rem 1rem;
  color: var(--dark);
  text-decoration: none;
}

:deep(.font-size-adjuster .dropdown-menu a:hover) {
  background: rgba(0,0,0,0.05);
}
</style>
