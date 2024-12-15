<script setup lang="ts">
import DefaultLayout from '@/layouts/DefaultLayout.vue'
</script>

<template>
  <DefaultLayout>
    <div class="grid grid-cols-1 gap-4 md:grid-cols-2 md:gap-6 xl:grid-cols-4 2xl:gap-7.5">
      <div class="rounded-sm border border-stroke bg-white py-6 px-7.5 shadow-default dark:border-strokedark dark:bg-boxdark">
        <h2 class="text-title-md2 font-bold text-black dark:text-white">Welcome to Admin Dashboard</h2>
        <p class="mt-4 text-sm font-medium">This is your simplified admin dashboard template. You can start adding your own components here.</p>
      </div>
    </div>

    <div class="mt-4 grid grid-cols-12 gap-4 md:mt-6 md:gap-6 2xl:mt-7.5 2xl:gap-7.5">
      <!-- Add your custom components here -->
      <div class="col-span-12">
        <div class="rounded-sm border border-stroke bg-white p-7.5 shadow-default dark:border-strokedark dark:bg-boxdark">
          <h4 class="mb-6 text-xl font-semibold text-black dark:text-white">
            Getting Started
          </h4>
          <p class="text-base text-body-color dark:text-body-color-dark">
            This is a simplified admin dashboard template. You can:
          </p>
          <ul class="mt-4 list-inside list-disc text-base text-body-color dark:text-body-color-dark">
            <li>Add your own components</li>
            <li>Customize the layout</li>
            <li>Implement your business logic</li>
            <li>Connect to your backend services</li>
          </ul>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template> 