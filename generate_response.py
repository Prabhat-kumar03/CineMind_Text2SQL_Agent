import google.generativeai as genai
import os
import dotenv
import json
from pydantic import BaseModel
from generate_sql import sql_query_generator


dotenv.load_dotenv('.env')

class Schema(BaseModel):
    answer: str


def generate_response(query):
    try:
        KEY= os.environ.get("GENAI_API_KEY")
        records = sql_query_generator(query)
        
        prompt = f"""You are an advanced AI and your name is Naruto , capable of generating response in Natural Language./
        Start and end the response with a exciting greeting and a random relevant emoji.
        You will passed a query and database record and based on that you have to generate a response in natural language. 
        Here is -
        user query - {query}
        database record - {records}./
        For queries other than movies , reply with apology.     
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
        return response["answer"]
    except Exception as e:
        print("Error as :",e)