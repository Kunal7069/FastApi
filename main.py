from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

class Item(BaseModel):
    api_name: str
    api_url: str

@app.post("/items/")
async def create_item(item: Item):
    response = supabase.table("API").insert({"api_name": item.api_name, "api_url": item.api_url}).execute()
    return response.data

@app.get("/items/")
async def read_items():
    response = supabase.table("API").select("*").execute()
    print(response)
    return response.data



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
