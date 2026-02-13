# Radiology Procedures API

A simple REST API for querying radiology procedure data stored in a PostgreSQL database.  
This project uses a CSV dataset of common radiology procedures (CPT codes, modality, body part, contrast usage, and average duration).

---

## Features

- Retrieve all radiology procedures
- Look up a procedure by CPT code
- Update a procedure by CPT Code
- Add a procedure by CPT code

---

## API Routes

### 1. GET / 
Returns all radiology procedures.

**Example Response:**
```json
[
  {
    "cpt_code": "71045",
    "procedure_name": "Chest X-ray 1 view",
    "modality": "XR",
    "body_part": "Chest",
    "contrast": "None",
    "avg_duration_min": 5
  }
]
```

### 2. GET /procedures/{cpt_code}
Returns a single procedures by CPT code.

**Example Response:**
```json
{
  "cpt_code": "71260",
  "procedure_name": "CT Chest w/ contrast",
  "modality": "CT",
  "body_part": "Chest",
  "contrast": "Yes",
  "avg_duration_min": 20
}
```

### 3. POST /procedures/{cpt_code}
adds a new procedure

### 4. PUT /procedures/{cpt_code}
updates an existing procedure by cpt_code




