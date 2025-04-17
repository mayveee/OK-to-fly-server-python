from fastapi import FastAPI
from routes import analysis

app = FastAPI()
app.include_router(analysis.router)

@app.get("/")
def root():
    return {"message": "🟢 서버가 정상적으로 작동 중입니다."}