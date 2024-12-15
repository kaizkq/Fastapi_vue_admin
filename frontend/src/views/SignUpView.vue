<template>
  <div class="flex min-h-screen items-center justify-center bg-gray-100">
    <div class="w-full max-w-md rounded-lg bg-white p-8 shadow-md">
      <h2 class="mb-6 text-center text-2xl font-bold text-gray-900">Sign Up</h2>
      <form @submit.prevent="handleSubmit" class="space-y-4">
        <div>
          <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
          <input
            id="username"
            v-model="username"
            type="text"
            required
            class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
          />
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
          <input
            id="password"
            v-model="password"
            type="password"
            required
            class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
          />
        </div>

        <div>
          <label for="nickname" class="block text-sm font-medium text-gray-700">Nickname (Optional)</label>
          <input
            id="nickname"
            v-model="nickname"
            type="text"
            class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
          />
        </div>

        <div v-if="error" class="text-sm text-red-600">{{ error }}</div>

        <button
          type="submit"
          class="w-full rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          :disabled="isLoading"
        >
          {{ isLoading ? 'Signing up...' : 'Sign Up' }}
        </button>

        <div class="text-center text-sm">
          <router-link to="/signin" class="text-blue-600 hover:text-blue-800">
            Already have an account? Sign in
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const username = ref('')
const password = ref('')
const nickname = ref('')
const error = ref('')
const isLoading = ref(false)

async function handleSubmit() {
  if (isLoading.value) return

  error.value = ''
  isLoading.value = true

  try {
    const success = await authStore.register(username.value, password.value, nickname.value || undefined)
    if (success) {
      router.push('/signin')
    } else {
      error.value = 'Registration failed'
    }
  } catch (e) {
    error.value = 'An error occurred during registration'
  } finally {
    isLoading.value = false
  }
}
</script> 