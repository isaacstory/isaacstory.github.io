<template>
    <div class="hello">Goodbye {{who}}</div>
  </template>
  
  <script>
  module.exports = {
    data() {
        return {
            who: 'world'
        }
    }
  }
  </script>
  
  <style>
  .hello {
    background-color: #bbb;
  }
  </style>