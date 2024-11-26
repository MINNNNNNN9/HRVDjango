<template>
    <div class="feature-card glass-effect">
      <div class="icon-wrapper">
        <i :class="icon"></i>
      </div>
      <h3>{{ title }}</h3>
      <p>{{ description }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FeatureCard',
    props: {
      icon: String,
      title: String,
      description: String
    }
  }
  </script>
  
  <style scoped>
  .feature-card {
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
  }
  
  .feature-card:hover {
    transform: translateY(-10px);
  }
  
  .icon-wrapper {
    width: 80px;
    height: 80px;
    margin: 0 auto 1.5rem;
    background: linear-gradient(45deg, var(--primary), var(--secondary));
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .icon-wrapper i {
    font-size: 2rem;
    color: var(--light);
  }
  
  h3 {
    color: var(--primary);
    margin-bottom: 1rem;
    font-size: 1.5rem;
  }
  
  p {
    color: rgba(255, 255, 255, 0.8);
    line-height: 1.6;
  }
  </style>