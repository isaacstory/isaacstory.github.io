# Extraction Prompts for Exam Processing

## Subagent Prompt Template

Use this prompt when launching a subagent to process a single exam file. Replace `{FILENAME}` with the actual filename and `{BASE}` with `5d2a48010f15903e74c855984fc7d3640d33737b`.

---

Read the medical exam file at: {BASE}/drive/Exams/{FILENAME}

Extract TWO JSON objects from this exam. All content must be in English.

### OBJECT 1: EXAM SUMMARY

```json
{
  "file": "{FILENAME}",
  "title": "short title of the exam type",
  "material": "blood|urine|stool|DNA|saliva|hair|serum|CSF|other",
  "sample_date": "YYYY-MM-DD",
  "requested_by": "Doctor name",
  "metrics": ["what is being measured"],
  "purpose": ["what is the exam for"],
  "resultSummary": ["key findings as bullet points"],
  "abnormalValues": ["out-of-range results"],
  "normalValues": ["in-range results"],
  "assessmentSummary": ["clinical assessment summary"],
  "gptInterpretation": ["your interpretation of what this means for the patient"]
}
```

### OBJECT 2: EXAM VALUES

```json
{
  "file": "{FILENAME}",
  "title": "short title",
  "requested_by": "Doctor name",
  "sample_date": "YYYY-MM-DD",
  "results": [
    {
      "metric": "Creatinine",
      "material": "blood",
      "result": 0.37,
      "result_unit": "mg/dL",
      "reference_range_min": 0.18,
      "reference_range_max": 0.49,
      "result_status": "Normal",
      "observations": "Normal"
    }
  ]
}
```

### Rules

- sample_date format MUST be YYYY-MM-DD
- result: numeric when possible, string otherwise
- result_status: one of "Normal", "Abnormal", "High", "Low", "Indeterminate"
- material: lowercase
- reference_range_min/max: numeric or "N/A"
- For qualitative exams (imaging, EEG) with no numeric values, use string descriptions for result and "N/A" for ranges
- All fields required. Use "Unknown" or "N/A" for missing values
- If the file cannot be read or has no extractable exam data, return ONLY: `SKIP:reason`

### Expected Response Format

Return exactly two JSON code blocks labeled SUMMARY and VALUES:

````
```json SUMMARY
{...}
```

```json VALUES
{...}
```
````

No `meta` field. No arrays. Raw JSON objects only.
