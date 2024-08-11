<template>
  <div class="tab-nav">
    <ul class="tab-nav-list">
      <li v-for="(tab, index) in tabNames" 
          :key="index" 
          @click="activeTab = index" 
          :class="{ active: index === activeTab }">
        {{ tab }}
      </li>
    </ul>
    <div class="tab-content">
      <slot :name="activeTab.toString()"></slot>
    </div>
  </div>
</template>
  
<script>
module.exports = {
  props: {
    tabNames: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      activeTab: 0
    }
  }
}
</script>
  
<style scoped>
.tab-nav {
  font-family: Arial, sans-serif;
}

.tab-nav-list {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
  border-bottom: 2px solid #007bff;
}

.tab-nav-list li {
  padding: 10px 20px;
  cursor: pointer;
  background-color: #f8f9fa;
  border: 1px solid #dee2e6;
  border-bottom: none;
  margin-right: 5px;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  transition: all 0.3s ease;
}

.tab-nav-list li:hover {
  background-color: #e9ecef;
}

.tab-nav-list li.active {
  background-color: #007bff;
  color: white;
  border-color: #007bff;
  font-weight: bold;
}

.tab-content {
  padding: 20px;
  border: 1px solid #dee2e6;
  border-top: none;
  background-color: white;
}
</style>