# HRV 睡眠監測平台

基於 Django + Vue.js 的睡眠監測平台，專門用於追蹤和分析心率變異性（HRV）數據，提供完整的使用者認證系統和資料視覺化功能。

## 主要功能

- 使用者認證系統 (註冊/登入/登出)
- 多語言支援 (中文/英文)
- 無障礙設計 (字體大小調整)
- 睡眠數據追蹤與分析
- HRV 數據視覺化
- 響應式設計

## 專案結構

```
hrvproject/
├── backend/ # Django 後端
│ ├── accounts/ # 使用者管理應用
│ │ ├── models.py # 使用者、睡眠記錄和HRV數據模型
│ │ ├── views.py # API視圖
│ │ └── serializers.py # 資料序列化
│ ├── api/ # API 應用
│ └── hrvproject/ # 專案設定
│ ├── settings/ # 分離的設定檔
│ │ ├── base.py # 基礎設定
│ │ └── dev.py # 開發環境設定
├── frontend/ # Vue.js 前端
│ ├── src/
│ │ ├── components/ # 可重用元件
│ │ │ ├── Navbar.vue # 導航欄
│ │ │ ├── ErrorBoundary.vue # 錯誤邊界
│ │ │ └── FeatureCard.vue # 功能卡片
│ │ └── views/ # 頁面視圖
│ │ ├── Landing.vue # 首頁
│ │ ├── Login.vue # 登入
│ │ └── Register.vue # 註冊
```


## 技術棧

### 後端
- Django 5.1
- Django REST Framework
- SQLite (開發環境)
- CORS 支援
- 自定義使用者模型
- REST API

### 前端
- Vue.js 3
- Vue Router
- 現代化UI設計
- 響應式布局
- FontAwesome 圖標
- CSS 變數與主題

## API 端點

- 認證相關:
  - 註冊: `POST /api/auth/register/`
  - 登入: `POST /api/auth/login/`
  - 登出: `POST /api/auth/logout/`
  - 使用者資訊: `GET /api/auth/user/`
  
- 數據相關:
  - 睡眠記錄: `GET/POST /api/sleep-records/`
  - HRV 數據: `GET/POST /api/hrv-data/`

## 開發環境設置

### 後端設置

bash
1. 建立虛擬環境
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
2. 安裝依賴
cd backend
pip install -r requirements.txt
3. 執行資料庫遷移
python manage.py migrate
4. 啟動開發伺服器
python manage.py runserver

### 前端設置

bash
1. 進入前端目錄
cd frontend
2. 安裝依賴
npm install
3. 啟動開發伺服器
npm run serve

## 安全性考量

- CORS 設定已正確配置
- CSRF 保護已啟用
- 密碼驗證規則已實作
- Session 安全性設定已配置

## 開發指南

### 程式碼風格
- 後端遵循 PEP 8 規範
- 前端遵循 Vue.js 官方風格指南
- 使用 ESLint 進行程式碼檢查

### 提交規範
- 使用清晰的提交訊息
- 遵循功能分支工作流程
- 提交前進行本地測試

## 待辦事項

- [ ] 實作密碼重設功能
- [ ] 添加社交媒體登入
- [ ] 優化資料視覺化
- [ ] 實作即時通知系統
- [ ] 添加更多的無障礙功能

## 授權

本專案採用 MIT 授權條款


