# HRV Sleep Monitoring Platform

基於 Django + Vue.js 的睡眠監測平台，用於追蹤和分析心率變異性（HRV）數據。

## 專案結構

```
hrvproject/
├── backend/                 # Django 後端
│   ├── accounts/           # 用戶管理應用
│   ├── api/               # API 應用
│   ├── hrvproject/        # 主項目設定
│   └── requirements/      # 依賴需求文件
├── frontend/              # Vue.js 前端
│   ├── src/              # 源代碼
│   │   ├── components/   # Vue 組件
│   │   ├── views/        # 頁面視圖
│   │   ├── store/        # Vuex 狀態管理
│   │   └── router/       # Vue Router
├── docker/               # Docker 配置
└── docs/                 # 項目文檔
```

## 開發環境設置

### 後端設置

```bash
# 1. 創建虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. 安裝依賴
cd backend
pip install -r requirements/dev.txt

# 3. 運行遷移
python manage.py migrate

# 4. 創建超級用戶
python manage.py createsuperuser

# 5. 啟動開發服務器
python manage.py runserver
```

### 前端設置

```bash
# 1. 進入前端目錄
cd frontend

# 2. 安裝依賴
npm install

# 3. 啟動開發服務器
npm run serve
```

## API 文檔

- API 根路徑：`http://localhost:8000/api/`
- 管理界面：`http://localhost:8000/admin/`
- API 端點：
  - 用戶認證：`/api/auth/`
  - 睡眠記錄：`/api/sleep-records/`
  - HRV 數據：`/api/hrv-data/`

## 開發指南

### 後端開發
- 使用 Django REST framework 開發 API
- 遵循 PEP 8 編碼規範
- 所有新功能需要添加測試

### 前端開發
- 使用 Vue.js 3 + Vuex + Vue Router
- 遵循 Vue.js 風格指南
- 使用 ESLint 進行代碼檢查

## 部署

詳細部署說明請參考 `docs/deployment/` 目錄。

## 許可證

[MIT License](LICENSE)