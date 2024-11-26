<template>
    <slot></slot>
  </template>
  
  <script>
  export default {
    name: 'ErrorBoundaryComponent',
    errorCaptured(err, vm, info) {
      console.error('Error captured:', err, vm, info)
      return false
    }
  }
  </script>