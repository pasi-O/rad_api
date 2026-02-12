# Radiology Procedures API

A simple REST API for querying radiology procedure data stored in a PostgreSQL database.  
This project uses a CSV dataset of common radiology procedures (CPT codes, modality, body part, contrast usage, and average duration).

---

## Features

- Retrieve all radiology procedures
- Look up a procedure by CPT code
- Filter by modality, body part, contrast, or duration
- Combine multiple filters
- Optional CRUD routes for adding, updating, or deleting procedures
- Optional analytics routes (e.g., modality counts)

---

## API Routes

### 1. GET /procedures  
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

### 2. GET/ procedures/:cpt_code
return a single procedure by CPT code

Example:
GET /procedures/71260

sample response:
# Radiology Procedures API

A simple REST API for querying radiology procedure data stored in a PostgreSQL database.  
This project uses a CSV dataset of common radiology procedures (CPT codes, modality, body part, contrast usage, and average duration).

---

## Features

- Retrieve all radiology procedures
- Look up a procedure by CPT code
- Filter by modality, body part, contrast, or duration
- Combine multiple filters
- Optional CRUD routes for adding, updating, or deleting procedures
- Optional analytics routes (e.g., modality counts)

---

## API Routes

### 1. GET /procedures  
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

### 2. GET/procedures/:cpt_code
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

### 3. GET /procedures?modality=CT
Filters procedures by modality
```json
[
  {
    "cpt_code": "71260",
    "procedure_name": "CT Chest w/ contrast",
    "modality": "CT",
    "body_part": "Chest",
    "contrast": "Yes",
    "avg_duration_min": 20
  }
]

### 4. GET /procedures?body_part=Chest
filters by body part

### 5. GET /procedures?contrast=Yes
filters by contrast usage

### 6. GET /procedures?max_duration=20
filters by maximum exam duration

### 7. GET /procedures with multiple filters
supports combining filters

example: GET /procedures?modality=CT&contrast=Yes&max_duration=25

### 8. POST /procedures
adds a new procedure

PUT /Procedures/:cpt_code
updates an existing procedure




