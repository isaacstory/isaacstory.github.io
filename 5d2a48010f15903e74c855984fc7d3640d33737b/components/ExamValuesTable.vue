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
                        <th>Value</th>
                        <th>Ref range</th>
                        <th>File</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Example Record -->
                    <tr v-for="item in filteredExams" :key="item.key">
                        <td style="min-width: 62px;">{{ item.sample_date }}</td>
                        <td>{{ item.material }}</td>
                        <td>{{ item.metric }}</td>
                        <td :class="{ 'abnormal-value': item.result_status !== 'Normal' }">
                            {{ item.display_result }}
                        </td>
                        <td>{{ item.display_ref_range }}</td>
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
      examvalues: {
        type: Array,
        required: true
      }
    },
    created() {
        const individualValues = [];
        this.examvalues.forEach(item => {
            item.results.forEach(res => {
                individualValues.push({
                    key: `${item.file}-${res.metric}`,
                    ...res,
                    display_result: `${res.result} (${res.result_status})`,
                    display_ref_range: `${res.reference_range_min} - ${res.reference_range_max} (${res.result_unit})`,
                    file: item.file,
                    sample_date: item.sample_date,
                    title: item.title,
                    requested_by: item.requested_by,
                });
            });
        });
        this.individualValues = individualValues;
    },
    data() {
        return {
            searchQuery: '',
            individualValues: []
        }
    },
    computed: {
        filteredExams() {
            const q = this.searchQuery.toLowerCase()
            return this.individualValues.filter(item => {
                return item?.sample_date?.toLowerCase().includes(q) ||
                       item?.material?.toLowerCase().includes(q) ||
                       item?.metric?.toLowerCase().includes(q) ||
                       item?.display_result?.toLowerCase().includes(q) ||
                       item?.display_ref_range?.toLowerCase().includes(q);
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
    }
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

    .abnormal-value {
        background-color: #ffcccc; /* Light red background for abnormal values */
        font-weight: bold;
        color: #cc0000; /* Dark red text for abnormal values */
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