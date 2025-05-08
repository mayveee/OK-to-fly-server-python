from fastapi import FastAPI
from routes import analysis
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(analysis.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "🟢 서버가 정상적으로 작동 중입니다."}