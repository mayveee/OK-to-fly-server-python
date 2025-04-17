from item_list import ITEM_INFO

# GPT 설정 프롬프트
SYSTEM_PROMPT = """
이미지와 물품 목록이 주어지면 이미지에서 물품 목록 중 포함된 항목을 찾아서
물품 이름만 추출해서 아래 형식을 지켜 JSON 배열로 반환해줘.
만약 한 물체가 여러 목록에 해당되어도 가장 정확도 높은 한개로 골라줘.

형식:
["물품1", "물품2", "물품3"]

다른 설명이나 문장은 쓰지말고 JSON만 줘.
"""

# 이미지와 함께 보낼 물품 목록 프롬프트
item_names = list(ITEM_INFO.keys())
ITEM_LIST_PROMPT = "물품 목록:\n- " + "\n- ".join(item_names)