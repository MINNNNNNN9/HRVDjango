<template>
  <div class="home">
    <nav class="navbar">
      <div class="logo">HRV 睡眠檢測平台</div>
      <div class="nav-links">
        <a href="#dashboard">儀表板</a>
        <a href="#analysis">分析報告</a>
        <a href="#settings">設置</a>
        <button @click="handleLogout" class="logout-btn">登出</button>
      </div>
    </nav>

    <main class="main-content">
      <div class="welcome-message">
        <h1>歡迎回來，{{ username }}！</h1>
        <p>讓我們一起探索您的睡眠品質</p>
      </div>

      <div class="dashboard">
        <div class="card">
          <i class="fas fa-chart-line card-icon"></i>
          <h3>睡眠趨勢</h3>
          <p>查看您的睡眠質量趨勢分析和歷史數據。</p>
        </div>

        <div class="card">
          <i class="fas fa-heartbeat card-icon"></i>
          <h3>心率變異分析</h3>
          <p>深入了解您的心率變異性指標和健康狀況。</p>
        </div>

        <div class="card">
          <i class="fas fa-moon card-icon"></i>
          <h3>睡眠階段</h3>
          <p>分析您的睡眠階段分布和睡眠效率。</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      username: ''
    }
  },
  async created() {
    try {
      const response = await axios.get('/api/user/')
      this.username = response.data.username
    } catch (error) {
      this.$router.push('/login')
    }
  },
  methods: {
    async handleLogout() {
      try {
        await axios.post('/api/logout/')
        localStorage.removeItem('token')
        this.$router.push('/login')
      } catch (error) {
        console.error('登出失敗', error)
      }
    }
  }
}
</script>

<style scoped>
.home {
  min-height: 100vh;
  background: linear-gradient(to right, #24243e, #302b63, #0f0c29);
  color: #fff;
}

.navbar {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  background: linear-gradient(45deg, #ff6b6b, #feca57);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nav-links {
  display: flex;
  gap: 2rem;
  align-items: center;
}

.nav-links a {
  color: #fff;
  text-decoration: none;
  position: relative;
  padding: 0.5rem 0;
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: #ff6b6b;
  transition: width 0.3s ease;
}

.nav-links a:hover::after {
  width: 100%;
}

.logout-btn {
  background: transparent;
  border: 2px solid #ff6b6b;
  color: #ff6b6b;
  padding: 0.5rem 1.5rem;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.logout-btn:hover {
  background: #ff6b6b;
  color: white;
}

.main-content {
  padding: 6rem 2rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.welcome-message {
  text-align: center;
  margin-bottom: 3rem;
}

.welcome-message h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 2rem;
  border-radius: 20px;
  text-align: center;
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
}

.card-icon {
  font-size: 2.5rem;
  color: #ff6b6b;
  margin-bottom: 1rem;
}

.card h3 {
  margin-bottom: 1rem;
  color: #ff6b6b;
}

.card p {
  color: rgba(255, 255, 255, 0.8);
}
</style>
