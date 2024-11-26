<template>
  <div class="font-size-adjuster">
    <div class="dropdown">
      <button class="dropdown-toggle">
        <i class="fas fa-font"></i> 字型大小
      </button>
      <div class="dropdown-menu">
        <a 
          href="#" 
          @click.prevent="changeFontSize('small')"
          :class="{ active: currentFontSize === 'small' }"
        >小</a>
        <a 
          href="#" 
          @click.prevent="changeFontSize('medium')"
          :class="{ active: currentFontSize === 'medium' }"
        >中</a>
        <a 
          href="#" 
          @click.prevent="changeFontSize('large')"
          :class="{ active: currentFontSize === 'large' }"
        >大</a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'FontSizeAdjuster',
  computed: {
    ...mapGetters('settings', ['currentFontSize'])
  },
  methods: {
    ...mapActions('settings', ['changeFontSize'])
  }
}
</script>

<style scoped>
.font-size-adjuster {
  position: relative;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-toggle {
  background: none;
  border: none;
  color: inherit;
  cursor: pointer;
  padding: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background: white;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  display: none;
  z-index: 1000;
}

.dropdown:hover .dropdown-menu {
  display: block;
}

.dropdown-menu a {
  display: block;
  padding: 0.5rem 1rem;
  color: #333;
  text-decoration: none;
}

.dropdown-menu a:hover,
.dropdown-menu a.active {
  background: #f5f5f5;
}
</style>
