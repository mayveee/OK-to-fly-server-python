import json
from fastapi import APIRouter, HTTPException
import os
import openai
from dotenv import load_dotenv
from pydantic import BaseModel
from prompts import ITEM_LIST_PROMPT, SYSTEM_PROMPT
from utils.item_mapper import map_items_to_info

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # 키가 .env에 포함되어있어야함.
router = APIRouter()

class ImageInput(BaseModel):
    image: str  # Base64

@router.post("/analysis")
async def analyze_image(data: ImageInput):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                # 프롬프트들은 prompts.py에서 한번에 관리
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user", 
                    "content": [
                        {"type": "text", "text": ITEM_LIST_PROMPT},
                        {"type": "image_url", "image_url": {"url": data.image}}
                    ]}
            ],
            max_tokens=1000
        )

        # GPT 결과 파싱
        raw_output = response.choices[0].message.content
        detected_names = json.loads(raw_output)

        result = map_items_to_info(detected_names)

        return {"detected_items": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
