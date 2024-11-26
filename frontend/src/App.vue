<template>
  <div id="app">
    <ErrorBoundary>
      <NavigationBar />
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </ErrorBoundary>
  </div>
</template>

<script>
import NavigationBar from '@/components/Navbar.vue'
import ErrorBoundary from '@/components/ErrorBoundary.vue'

export default {
  name: 'App',
  components: {
    NavigationBar,
    ErrorBoundary
  }
}
</script>

<style>
:root {
  --primary-dark: #1a2942;
  --primary-light: #2c5282;
  --primary-gradient: linear-gradient(135deg, var(--primary-dark), var(--primary-light));
  
  --accent-dark: #e53e3e;
  --accent-light: #fc8181;
  --accent-gradient: linear-gradient(135deg, var(--accent-dark), var(--accent-light));
  
  --neutral-100: #f7fafc;
  --neutral-200: #edf2f7;
  --neutral-300: #e2e8f0;
  --neutral-400: #cbd5e0;
  
  --glass-bg: rgba(255, 255, 255, 0.08);
  --glass-border: rgba(255, 255, 255, 0.12);
  --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  
  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 8px 16px rgba(0, 0, 0, 0.12);
}

#app {
  min-height: 100vh;
  background: var(--neutral-100);
}

.glass-effect {
  background: var(--glass-bg);
  backdrop-filter: blur(12px);
  border: 1px solid var(--glass-border);
  box-shadow: var(--glass-shadow);
}

/* 全域動畫效果 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>

