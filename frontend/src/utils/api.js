import axios from 'axios'

// 創建 axios 實例
const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json'
  },
  withCredentials: true
})

// 請求攔截器
api.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// API 方法
export const auth = {
  login: (credentials) => api.post('/login/', credentials),
  register: (userData) => api.post('/register/', userData),
  logout: () => api.post('/logout/'),
  getUser: () => api.get('/user/')
}

export default api
