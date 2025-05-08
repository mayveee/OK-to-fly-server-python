# 공항 반입 제한 물품 감지 API server in python

- AI 기반 이미지 분석을 통해 공항 보안검색 대상 물품을 자동 감지하고 기내/위탁 수하물 반입 가능 여부와 설명을 반환하는 API.  
- GPT-4.1 기반 이미지 내 물품 추출

---

## API 예시
### [POST] /analysis
+ 입력: BASE64 인코딩 이미지
```
{
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ..."  // 이미지 base64 (data URL 포함)
}
```
+ 출력:
```
{
  "detected_items": [
    {
      "name": "보조배터리",
      "description": "100Wh 초과 시 항공사 승인 필요. 위탁 금지.",
      "rule": {
        "allowed_in_cabin": true,
        "allowed_in_checked": false
      }
    },
    {
      "name": "액체류",
      "description": "설명",
      "rule": {
        "allowed_in_cabin": false,
        "allowed_in_checked": true
      }
    }
  ]
}

``` 
---

## 프로젝트 실행

### 1. 가상환경 설정
```bash
python -m venv .venv
source .venv/bin/activate  # Windows는 .venv\Scripts\activate
```
### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 환경변수 설정
.env 파일 생성 후:
```.env
OPENAI_API_KEY=sk-...
```

### 4. 서버 실행
```bash
uvicorn main:app --reload
```
