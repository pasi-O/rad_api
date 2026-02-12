from fastapi import FastAPI
from db import get_connection
from models import procedure_to_dict

app = FastAPI()


@app.get("/procedures")
def get_procedures():
    return {"this": "not done"}

@app.get("/procedures/{cpt_code}")
def get_procedure(cpt_code: str):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM radiology_procedures where cpt_code = %s", (cpt_code,))
        row = cur.fetchone()

        cur.close()
        conn.close()

        if not row:
              return {"error" : "procedure not found"}
        
        return procedure_to_dict(row)