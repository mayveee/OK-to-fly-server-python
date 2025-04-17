# test_client.py
import requests
import base64

with open("test3.jpg", "rb") as f:
    encoded = base64.b64encode(f.read()).decode("utf-8")
    data_url = f"data:image/jpeg;base64,{encoded}"

res = requests.post("http://localhost:8000/analysis", json={"image": data_url})
print(res.status_code)
print(res.json())