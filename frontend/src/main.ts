import './assets/css/satoshi.css'
import './assets/css/style.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)

// Initialize auth state before mounting
import { useAuthStore } from '@/stores/auth'
const init = async () => {
  const authStore = useAuthStore()
  await authStore.initializeAuth()
  app.mount('#app')
}

init()
