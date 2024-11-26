<template>
  <div class="landing">
    <div class="hero-section">
      <div class="hero-content">
        <h1>專業的睡眠品質監測系統</h1>
        <p>24小時全天候監測，為您的健康把關</p>
        <div class="search-box">
          <input type="text" placeholder="搜尋服務項目...">
          <button><i class="fas fa-search"></i></button>
        </div>
      </div>
    </div>

    <main class="main-content container">
      <div class="quick-links">
        <div class="quick-link-item">
          <i class="fas fa-chart-line"></i>
          <h3>即時監測</h3>
          <p>24小時持續監測心率變異性</p>
        </div>
        <div class="quick-link-item">
          <i class="fas fa-chart-pie"></i>
          <h3>數據分析</h3>
          <p>專業的數據視覺化分析</p>
        </div>
        <div class="quick-link-item">
          <i class="fas fa-heartbeat"></i>
          <h3>健康建議</h3>
          <p>個人化的健康管理建議</p>
        </div>
        <div class="quick-link-item">
          <i class="fas fa-user-md"></i>
          <h3>專家諮詢</h3>
          <p>專業醫師線上諮詢服務</p>
        </div>
      </div>

      <div class="news-section">
        <h2 class="section-title">最新消息</h2>
        <div class="more-link">
          <a href="#">更多 ></a>
        </div>
        <div class="news-list">
          <div class="news-item">
            <span class="date">2024/01/25</span>
            <a href="#" class="title">新版睡眠監測系統上線公告</a>
          </div>
          <div class="news-item">
            <span class="date">2024/01/20</span>
            <a href="#" class="title">年度系統維護通知</a>
          </div>
          <div class="news-item">
            <span class="date">2024/01/15</span>
            <a href="#" class="title">睡眠品質改善研究報告發布</a>
          </div>
        </div>
      </div>
    </main>

    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-info">
            <p>聯絡地址：112303 臺北市北投區明德路365號 學思樓10樓 F1033 生醫資訊實驗室</p>
            <p>服務電話： (02)2822-7101 轉 1237</p>
            <p>本平台服務時間：週一至週五 09:00-18:00</p>
          </div>
          <div class="footer-links">
            <a href="#">隱私權策</a>
            <a href="#">資訊安全政策</a>
            <a href="#">聯絡我們</a>
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
  name: 'LandingPage'
}
</script>

<style scoped>
.landing {
  min-height: 100vh;
}

.hero-section {
  height: 100vh;
  background: linear-gradient(135deg, 
    var(--primary-dark) 0%, 
    var(--primary-light) 100%
  );
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: white;
}

.hero-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 20% 30%, rgba(44, 82, 130, 0.4) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(26, 41, 66, 0.4) 0%, transparent 50%);
  opacity: 0.8;
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 800px;
  padding: 2rem;
}

.hero-content h1 {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  background: linear-gradient(135deg, #fff 0%, #f0f0f0 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.hero-content p {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  color: rgba(255, 255, 255, 0.9);
}

.search-box {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border-radius: 50px;
  padding: 0.5rem;
  display: flex;
  gap: 0.5rem;
  max-width: 600px;
  margin: 0 auto;
}

.search-box input {
  flex: 1;
  background: transparent;
  border: none;
  color: white;
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
}

.search-box input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}

.search-box button {
  background: var(--accent-gradient);
  box-shadow: 0 4px 12px rgba(229, 62, 62, 0.3);
  border: none;
  color: white;
  padding: 0.8rem 2rem;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
}

.search-box button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
}

/* 快速連結區域 */
.quick-links {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  margin-top: -4rem;
  padding: 0 2rem;
  position: relative;
  z-index: 2;
}

.quick-link-item {
  background: rgba(255, 255, 255, 0.98);
  border: 1px solid var(--neutral-200);
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.quick-link-item:hover {
  transform: translateY(-5px);
  box-shadow: 
    0 20px 25px -5px rgba(0, 0, 0, 0.1),
    0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.quick-link-item i {
  color: var(--primary-light);
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
}

.quick-link-item:hover i {
  transform: scale(1.1);
  color: var(--accent-dark);
}

.quick-link-item h3 {
  margin: 1rem 0;
  color: #2c3e50;
}

.quick-link-item p {
  color: #666;
  font-size: 0.9rem;
}

/* 最新消息區域 */
.news-section {
  background: white;
  border-radius: 20px;
  box-shadow: 
    0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);
  padding: 2rem;
  margin: 4rem 2rem;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.news-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #eee;
  transition: all 0.3s ease;
  border-left: 3px solid transparent;
}

.news-item .date {
  color: #666;
  margin-right: 2rem;
  min-width: 100px;
}

.news-item .title {
  color: #2c3e50;
  text-decoration: none;
  flex: 1;
}

.news-item:hover {
  border-left-color: var(--accent-dark);
  background: var(--neutral-100);
  transform: translateX(10px);
}

/* 響應式設計 */
@media (max-width: 1200px) {
  .quick-links {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .hero-content h1 {
    font-size: 2rem;
  }
  
  .quick-links {
    grid-template-columns: 1fr;
    margin-top: -2rem;
  }
  
  .news-item {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .news-item .date {
    margin-bottom: 0.5rem;
  }
}

/* 容器通用樣式 */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.footer {
  background: #1a4f7b;
  color: #fff;
  padding: 2rem 0;
  margin-top: 3rem;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  margin-bottom: 2rem;
}

.footer-links a {
  color: #fff;
  text-decoration: none;
  margin-left: 1.5rem;
}

.copyright {
  text-align: center;
  padding-top: 1rem;
  border-top: 1px solid rgba(255,255,255,0.1);
}

@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
    gap: 1rem;
  }
  
  .footer-links {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .footer-links a {
    margin-left: 0;
  }
}

/* 添加標題樣式 */
.section-title {
  font-size: 1.5rem;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.more-link {
  text-align: right;
}

.more-link a {
  color: #1a4f7b;
  text-decoration: none;
  font-size: 0.9rem;
}

.more-link a:hover {
  color: #ff6b6b;
}
</style>
