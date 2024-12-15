import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/signin',
      name: 'signin',
      component: () => import('@/views/SignInView.vue'),
      meta: { requiresGuest: true }
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('@/views/SignUpView.vue'),
      meta: { requiresGuest: true }
    },
    // Protected routes
    {
      path: '/home',
      name: 'home',
      component: () => import('@/views/Dashboard/HomeView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('@/views/Pages/ProfileView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/pages/settings',
      name: 'settings',
      component: () => import('@/views/Pages/SettingsView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/books',
      name: 'books',
      component: () => import('@/views/Pages/BookListView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/home'
    }
  ]
})

// Navigation guard
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  const requiresGuest = to.matched.some(record => record.meta.requiresGuest)

  // Wait for auth to be initialized
  if (!authStore.isInitialized) {
    await authStore.initializeAuth()
  }

  // If requires auth and not authenticated, redirect to signin
  if (requiresAuth && !authStore.isAuthenticated) {
    next('/signin')
    return
  }

  // If requires guest and authenticated, redirect to home
  if (requiresGuest && authStore.isAuthenticated) {
    next('/home')
    return
  }

  // If user data is needed and not loaded, try to fetch it
  if (authStore.isAuthenticated && !authStore.user) {
    try {
      await authStore.fetchUser()
    } catch (error) {
      console.error('Failed to fetch user data:', error)
      // If fetching user fails, continue anyway
    }
  }

  next()
})

export default router
