import google.generativeai as genai
from pydantic import BaseModel
from typing import List
import os
import dotenv
import json
from database import *

dotenv.load_dotenv('.env')

class Schema(BaseModel):
    sql_query: str

def sql_query_generator(query : str) -> List:  
    try:
        KEY= os.environ.get("GENAI_API_KEY")
        sql_query1 = "SELECT * FROM moviebookings LIMIT 5"
        connection = get_or_connect_db()
        records = execute_sql_query(connection,sql_query1)
        
        column_name = execute_sql_query(connection,"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'moviebookings' AND TABLE_SCHEMA = 'movietheatre' ORDER BY ORDINAL_POSITION;")

        prompt = f""" You are an Advanced AI capable of generating SQL query for MySQL./
        You will be given a user query and 5 records of a database./
        Database stores information about movie theatre movie bookings./
        Based on the database records and user query , generate a correct SQL query ./
        Here is user query - {query} ./
        Here is table name - "moviebookings"
        Here is name of columns / Schema - {column_name}./
        Here are 5 rows of database - {records}
        """
        genai.configure(api_key=KEY)
        model = genai.GenerativeModel(
            model_name=("gemini-2.5-flash"),
            system_instruction=prompt,
            generation_config={"response_mime_type": "application/json","response_schema": Schema},
        )
        response = model.generate_content(query)
        response = json.loads(response.text)
        print(response)
        db_records = execute_sql_query(connection,response["sql_query"])
        print(db_records)
        return db_records
    except Exception as e :
        raise e