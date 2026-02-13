from pydantic import BaseModel

class ProcedureCreate(BaseModel):
    cpt_code: str
    procedure_name:str
    modality: str
    body_part: str
    contrast: str | None = None
    avg_duration_min: int
class ProcedureUpdate(BaseModel):
    cpt_code: str | None = None
    modality:str | None = None
    body_part:str | None = None
    contrast: str | None = None
    avg_duration_min: int | None = None

def procedure_to_dict(row):
    return {
        "cpt_code": row[0],
        "procedure_name": row[1],
        "modality": row[2],
        "body_part": row[3],
        "contrast": row[4],
        "avg_duration_min": row[5]
    }
