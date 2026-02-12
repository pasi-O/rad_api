from fastapi import FastAPI
from db import get_connection
from models import procedure_to_dict
from pathlib import Path
from models import ProcedureCreate

app = FastAPI()

def load_query(name):
    return Path(f"queries/{name}.sql").read_text()

# Get all procedures
@app.get('/')
def get_all_procedures():
    conn = get_connection()
    cur = conn.cursor()

    query = load_query("get_all_procedures")
    cur.execute(query)
    all_procedures = cur.fetchall()
      
    cur.close()
    conn.close()

    return all_procedures

#Get procedure by cpt_code
@app.get('/procedures/{cpt_code}')
def get_procedure_cpt_code(cpt_code: str):
    conn = get_connection()
    cur = conn.cursor()

    query = load_query("get_procedures_by_cpt_code")
    cur.execute(query, (cpt_code,))
    procedure_by_cpt = cur.fetchone()
    return procedure_by_cpt

# add a procedure
@app.post('/procedures')
def create_procedure(procedure: ProcedureCreate):
      conn = get_connection()
      cur = conn.cursor()

      query = load_query("insert_procedure")
      cur.execute(query, (
          procedure.cpt_code,
          procedure.procedure_name,
          procedure.modality,
          procedure.body_part,
          procedure.contrast,
          procedure.avg_duration_min
      ))

      new_row = cur.fetchone()
      conn.commit()

   
      cur.close()
      conn.close()
      return {  "Message": "Procedure created successfully",
                 "procedure": procedure_to_dict(new_row)}
      
           

# update a procedure
@app.put("/procedures/:{cpt_code}")
def update_procedure(cpt_code: str):
    return None

