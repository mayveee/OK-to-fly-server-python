from item_list import ITEM_INFO

def map_items_to_info(detected_names: list[str]) -> list[dict]:
    """
    물품 리스트 주면 item_list에서 case와 description 가져와서 붙여서 리턴.

    Returns:
    {
        "name": "가위",
        "description": "예외: 날 길이 6cm이하의 가위는 기내 반입 가능",
        "rule": {
            "allowed_in_cabin": false,
            "allowed_in_checked": true
        }
    }
    """
    result = []

    # case 나눌 때 참조하는 맵
    RULE_CASE = {
        1: {"allowed_in_cabin": False, "allowed_in_checked": True},  # case 1
        2: {"allowed_in_cabin": True, "allowed_in_checked": False},  # case 2
        3: {"allowed_in_cabin": False, "allowed_in_checked": False}, # case 3
        4: {"allowed_in_cabin": None, "allowed_in_checked": None}    # case 4
    }

    for name in detected_names:
        info = ITEM_INFO.get(name)
        # info에 매칭되지 않는 물품이 있다면 결과 리스트에서 버림
        if not info:
            continue
        
        # case 별로 나누어서 위탁/기내 반입 여부 판단
        case = info["case"]        
        result.append({
            "name": name,
            "description": info.get("description", ""),
            "rule": RULE_CASE.get(case, {"allowed_in_cabin": None, "allowed_in_checked": None})
        })

    return result
