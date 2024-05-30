<template>
    <header>
        <div class="header-content">
            <div class="text-content">
                <h1>Patient Clinical History</h1>
                <h2>Basic Information</h2>
                <p><strong>Name:</strong>Isaac França</p>
                <p><strong>Date of Birth:</strong>2018-11-06</p>
                <p><strong>Conditions:</strong> Autism Spectrum Disorder</p>
            </div>
            <img src="isaac.png" alt="Patient Photo" class="patient-photo">
        </div>
    </header>
  </template>
  
  <script>
  module.exports = {
    data() {
        return {
            who: 'world'
        }
    },
  }
  </script>
  
<style>
    header, section {
        margin-bottom: 20px;
    }

    /* Additional styles to ensure the header scales nicely */
    header {
        padding: 20px;
        background-color: #f0f8ff;
        border-bottom: 2px solid #ccc;
    }

    h1, h2 {
        margin-top: 0;
        color: #0056b3;
        /* color: #fff; */
    }

    .header-content {
        display: flex;
        align-items: center; /* Aligns items vertically in the center */
        justify-content: space-between; /* Space between text and image */
    }

    .text-content {
        flex-grow: 1; /* Allows the text content to take up remaining space */
    }

    .patient-photo {
        width: auto; /* Adjusts width automatically */
        max-height: 200px; /* Adjusts the maximum height of the image */
        border-radius: 10px; /* Rounds the corners of the image */
        margin-left: 20px; /* Adds space between the text and the image */
    }
</style>