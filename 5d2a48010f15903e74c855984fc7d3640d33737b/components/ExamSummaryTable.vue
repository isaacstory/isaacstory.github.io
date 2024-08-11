<template>
    <div>
        <section class="search-section">
            <input type="text" id="searchInput" v-model="searchQuery" placeholder="Filter by anything">
        </section>

        <section class="records">
            <table id="recordsTable">
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Material</th>
                        <th>Exam</th>
                        <th>Doctor</th>
                        <th>Summary</th>
                        <th>File</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Example Record -->
                    <tr v-for="item in filteredExams" :key="item.file">
                        <td style="min-width: 62px;">{{ item.sample_date }}</td>
                        <td>{{ item.material }}</td>
                        <td>{{ item.title }}</td>
                        <td>{{ item.requested_by }}</td>
                        <td>{{ item.assessmentSummary.join(' / ') }}</td>
                        <td><a :href="'drive/Exams/' + item.file" target="_blank"><img :src="fileIcon(item)" alt="PDF"></a></td>
                    </tr>
                </tbody>
            </table>
        </section>
    </div>
  </template>
  
<script>
  module.exports = {
    props: {
      examdata: {
        type: Array,
        required: true
      }
    },
    data() {
        return {
            searchQuery: ''
        }
    },
    computed: {
        filteredExams() {
            const q = this.searchQuery.toLowerCase()
            return this.examdata.filter(item => {
                return item?.sample_date?.toLowerCase().includes(q) ||
                       item?.material?.toLowerCase().includes(q) ||
                       item?.title?.toLowerCase().includes(q) ||
                       item?.requested_by?.toLowerCase().includes(q) ||
                       item?.assessmentSummary.join(', ').toLowerCase().includes(q);
            });
        }
    },
    methods: {
        fileIcon(item) {
            const extension = item.file.split('.').pop().toLowerCase()
            return {
                pdf: 'pdf.png',
                xls: 'xls.png',
                xlsx: 'xls.png',
            }[extension] || 'xls.png'
        }
    },
    components: {
      'child-component': httpVueLoader('./ChildComponent.vue')
    },
  }
</script>
  
<style>
    input[type="text"] {
        width: 100%;
        padding: 10px;
        margin-top: 10px;
        box-sizing: border-box;
        border: 2px solid #ccc;
        border-radius: 4px;
        background-color: #fff;
        transition: border-color 0.3s;
    }

    input[type="text"]:focus {
        border-color: #4CAF50; /* Highlight color on focus */
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        font-size: 12px; /* Smaller font size for more content */
        background: #f8f8f8; /* Light background for table */
        border-radius: 8px; /* Rounded corners for table */
    }

    table, th, td {
        border: 1px solid #ddd;
    }

    th, td {
        text-align: left;
        padding: 4px; /* Reduced padding for a more compact look */
        border: 1px solid #ddd;
    }

    th {
        background-color: #f0f8ff;
    }

    tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    /* Icon styling */
    td img {
        display: block;
        width: 16px; /* Small icon size */
        height: auto;
        margin: 0 auto; /* Centering icon in the cell */
    }
</style>