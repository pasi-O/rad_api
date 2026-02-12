def procedure_to_dict(row):
    return {
        "cpt_code": row[0],
        "procedure_name": row[1],
        "modality": row[2],
        "body_part": row[3],
        "contrast": row[4],
        "avg_duration_min": row[5]
    }