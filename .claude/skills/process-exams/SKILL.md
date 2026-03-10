---
name: process-exams
description: Sync new medical exam PDFs into the site's JSON data files. Use when the user runs /process-exams or asks to process, sync, or import new exams. Scans drive/Exams/ for unprocessed files, extracts structured data via subagents, and updates exam.json and examvalues.json.
---

# Process Exams

Detect new exam files in `drive/Exams/`, extract structured data from each, and append to the site's JSON data files.

## Key Paths

- Base: `5d2a48010f15903e74c855984fc7d3640d33737b/`
- Exam PDFs: `{base}/drive/Exams/`
- Output: `{base}/jsonout/exam.json` and `{base}/jsonout/examvalues.json`
- Sync state: `{base}/sync-state.json`

## Workflow

### 1. Load sync state

Read `sync-state.json`. Structure:
```json
{
  "processed": { "filename.pdf": { "processed_at": "ISO", "has_summary": true, "has_values": true } },
  "skipped": { "filename.pdf": { "reason": "exam request, not results" } }
}
```

### 2. Find new files

List all files in `drive/Exams/`. Compare against sync-state (use Unicode NFC normalization for filenames). Report counts and list new files.

If no new files, stop.

### 3. Triage

Auto-skip and add to `skipped`:
- `.docx` files → "unsupported format"
- Names containing "pedido", "solicitacao", "solicitação" (case-insensitive) → "exam request, not results"
- Files ending in "port.pdf" when matching "eng.pdf" exists → "portuguese duplicate"

Ask user to confirm processing vs skipping for non-PDF image files (.jpg, .jpeg, .png).

Report triage results, confirm before proceeding.

### 4. Extract data via subagents

For each file to process, launch a general-purpose subagent using the prompt template in [references/extraction-prompts.md](references/extraction-prompts.md). Launch up to 3 subagents in parallel.

### 5. Merge results

For each successful extraction:
1. Parse SUMMARY and VALUES JSON blocks from subagent response
2. Read current `exam.json` and `examvalues.json`
3. Add `meta` field to each object (copy of all fields except `file` — legacy compatibility)
4. Append new records
5. Sort both arrays by `sample_date` ascending
6. Write JSON with 2-space indent
7. Update `sync-state.json`

If subagent returns `SKIP:reason`, add to `skipped`.

### 6. Report

Summary of processed, skipped, and errored files.

## Rules

- Never remove existing records from JSON files
- Never re-process files already in sync-state
- Maintain the `meta` field for backward compatibility
- Always use Unicode NFC normalization when comparing filenames
