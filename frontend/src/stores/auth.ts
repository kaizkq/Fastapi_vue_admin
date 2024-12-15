import { defineStore } from 'pinia'
import { ref, watch } from 'vue'
import { signIn, signUp, getCurrentUser } from '@/api/auth'

interface User {
  id: number
  username: string
  nickname?: string
}

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token') || '')
  const user = ref<User | null>(JSON.parse(localStorage.getItem('user') || 'null'))
  const isAuthenticated = ref(!!token.value)
  const isInitialized = ref(false)

  // Watch for token changes to update isAuthenticated
  watch(token, (newToken) => {
    isAuthenticated.value = !!newToken
    if (!newToken) {
      user.value = null
      localStorage.removeItem('user')
    }
  })

  // Watch for user changes to update localStorage
  watch(user, (newUser) => {
    if (newUser) {
      localStorage.setItem('user', JSON.stringify(newUser))
    } else {
      localStorage.removeItem('user')
    }
  })

  async function initializeAuth() {
    if (isInitialized.value) return

    const storedToken = localStorage.getItem('token')
    const storedUser = localStorage.getItem('user')
    
    if (storedToken) {
      token.value = storedToken
      isAuthenticated.value = true
      if (storedUser) {
        const parsedUser = JSON.parse(storedUser)
        user.value = parsedUser
        try {
          // Only fetch user data if we have the user ID
          if (parsedUser?.id) {
            const userData = await getCurrentUser(parsedUser.id)
            user.value = userData
          }
        } catch (error) {
          console.error('Failed to initialize auth:', error)
          if (error.response?.status === 401) {
            logout()
          }
        }
      }
    }
    isInitialized.value = true
  }

  async function login(username: string, password: string) {
    try {
      const response = await signIn({ username, password })
      if (response.token) {
        token.value = response.token
        localStorage.setItem('token', response.token)
        isAuthenticated.value = true
        user.value = response.user
        return true
      }
      return false
    } catch (error) {
      console.error('Login failed:', error)
      return false
    }
  }

  async function register(username: string, password: string, nickname?: string) {
    try {
      await signUp({ username, password, nickname })
      return true
    } catch (error) {
      console.error('Registration failed:', error)
      return false
    }
  }

  async function fetchUser() {
    if (!token.value || !user.value?.id) return null

    try {
      const userData = await getCurrentUser(user.value.id)
      user.value = userData
      return userData
    } catch (error) {
      console.error('Failed to fetch user:', error)
      if (error.response?.status === 401) {
        logout()
      }
      throw error
    }
  }

  function logout() {
    token.value = ''
    user.value = null
    isAuthenticated.value = false
    localStorage.removeItem('token')
    localStorage.removeItem('user')
  }

  return {
    token,
    user,
    isAuthenticated,
    isInitialized,
    login,
    register,
    logout,
    fetchUser,
    initializeAuth
  }
}) 