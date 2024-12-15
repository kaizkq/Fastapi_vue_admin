<script setup lang="ts">
import { ref, reactive, onMounted, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { updateUser } from '@/api/auth'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'

const authStore = useAuthStore()
const isLoading = ref(false)
const error = ref('')
const success = ref('')
const confirmPassword = ref('')
const pageTitle = ref('Profile')

const username = computed(() => authStore.user?.username || '')
const nickname = computed(() => authStore.user?.nickname || '')

const formData = reactive({
  username: '',
  nickname: '',
  password: ''
})

onMounted(async () => {
  if (!authStore.user) {
    await authStore.fetchUser()
  }
})

async function handleSubmit() {
  if (isLoading.value) return

  // Reset messages
  error.value = ''
  success.value = ''

  // Validate password confirmation if password is being changed
  if (formData.password && formData.password !== confirmPassword.value) {
    error.value = 'Passwords do not match'
    return
  }

  // Don't submit empty form
  if (!formData.username && !formData.nickname && !formData.password) {
    error.value = 'No changes to save'
    return
  }

  isLoading.value = true

  try {
    // Only include fields that have been changed
    const updateData = {
      ...(formData.username && { username: formData.username }),
      ...(formData.nickname && { nickname: formData.nickname }),
      ...(formData.password && { password: formData.password })
    }

    if (authStore.user?.id) {
      await updateUser(authStore.user.id, updateData)
      // Refresh user data
      await authStore.fetchUser()
      success.value = 'Profile updated successfully'
      
      // Reset form
      formData.username = ''
      formData.nickname = ''
      formData.password = ''
      confirmPassword.value = ''
    }
  } catch (e) {
    error.value = 'Failed to update profile'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <DefaultLayout>
    <BreadcrumbDefault :pageTitle="pageTitle" />

    <div class="mx-auto max-w-270">
      <div class="grid grid-cols-5 gap-8">
        <div class="col-span-5 xl:col-span-3">
          <div class="rounded-sm border border-stroke bg-white py-6 px-7.5 shadow-default dark:border-strokedark dark:bg-boxdark">
            <h2 class="text-title-md2 font-bold text-black dark:text-white">Personal Information</h2>
            <div class="mt-4">
              <form @submit.prevent="handleSubmit">
                <div class="mb-5.5">
                  <label class="mb-3 block text-sm font-medium text-black dark:text-white" for="username">
                    Username
                  </label>
                  <input
                    class="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="text"
                    name="username"
                    id="username"
                    v-model="formData.username"
                    :placeholder="username"
                  />
                </div>

                <div class="mb-5.5">
                  <label class="mb-3 block text-sm font-medium text-black dark:text-white" for="nickname">
                    Nickname
                  </label>
                  <input
                    class="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="text"
                    name="nickname"
                    id="nickname"
                    v-model="formData.nickname"
                    :placeholder="nickname || 'Enter nickname'"
                  />
                </div>

                <div class="mb-5.5">
                  <label class="mb-3 block text-sm font-medium text-black dark:text-white" for="password">
                    New Password
                  </label>
                  <input
                    class="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="password"
                    name="password"
                    id="password"
                    v-model="formData.password"
                    placeholder="Enter new password"
                  />
                </div>

                <div class="mb-5.5">
                  <label class="mb-3 block text-sm font-medium text-black dark:text-white" for="confirmPassword">
                    Confirm Password
                  </label>
                  <input
                    class="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="password"
                    name="confirmPassword"
                    id="confirmPassword"
                    v-model="confirmPassword"
                    placeholder="Confirm new password"
                  />
                </div>

                <div v-if="error" class="mb-5.5 text-sm text-danger">
                  {{ error }}
                </div>

                <div v-if="success" class="mb-5.5 text-sm text-success">
                  {{ success }}
                </div>

                <div class="flex justify-end gap-4.5">
                  <button
                    class="flex justify-center rounded bg-primary py-2 px-6 font-medium text-gray hover:bg-opacity-90"
                    type="submit"
                    :disabled="isLoading"
                  >
                    {{ isLoading ? 'Saving...' : 'Save Changes' }}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>