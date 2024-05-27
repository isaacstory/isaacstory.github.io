<template>
  <div>
    <div class="goodbye">Hello {{who}}</div>
    <child-component></child-component>
  </div>
</template>

<script>
module.exports = {
  data() {
      return {
          who: 'world'
      }
  },
  components: {
    'child-component': httpVueLoader('./ChildComponent.vue')
  },
}
</script>

<style>
.goodbye {
  background-color: #ffe;
}
</style>