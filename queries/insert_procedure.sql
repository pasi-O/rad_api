INSERT INTO radiology_procedures
(cpt_code, procedure_name, modality, body_part, contrast, avg_duration_min)
VALUES(%s, %s, %s, %s, %s, %s)
RETURNING *; 