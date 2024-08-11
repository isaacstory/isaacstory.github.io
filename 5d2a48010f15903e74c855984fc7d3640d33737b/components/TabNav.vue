<template>
  <div class="tab-nav">
    <ul class="tab-nav-list">
      <li v-for="(tab, index) in tabNames" :key="index" @click="activeTab = index" :class="{ active: index === activeTab }">
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
.tab-nav-list {
  display: flex;
  list-style: none;
  padding: 0;
}
.tab-nav-list li {
  padding: 10px;
  cursor: pointer;
}
.tab-nav-list li.active {
  font-weight: bold;
}
</style>