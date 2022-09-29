from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from datetime import datetime
import pytz

app = FastAPI()

class SignUpDto(BaseModel):
    name: str
    email: str
    phone: str
    receiveLetter: bool

@app.post("/sign-up")
async def signUp(dto: SignUpDto):
    mydb = mysql.connector.connect(
      host="localhost",
      port=3306,
      user="root",
      password="root",
      database="course_sign_up_db"
    )

    mycursor = mydb.cursor()

    tz_NP = pytz.timezone('Asia/Kathmandu') 
    now = datetime.now(tz_NP)

    sql = "INSERT INTO sign_up_info (name, email, phone, receive_letter, sign_up_date) VALUES (%s, %s, %s, %s, %s)"
    val = (dto.name, dto.email, dto.phone, dto.receiveLetter, now)
    mycursor.execute(sql, val)

    mydb.commit()

    return dto