import axios from 'axios'

const baseURL = 'http://localhost:5000'

const axiosInstance = axios.create({
  baseURL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Request interceptor
axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/signin'
    }
    return Promise.reject(error)
  }
)

export default axiosInstance 