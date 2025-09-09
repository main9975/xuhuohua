import json

def parse_to_playwright_cookies(cookies):
    # 处理 Cookies 代码来自 ChatGPT
    same_site_map = {
        "no_restriction": "None",
        "lax": "Lax",
        "strict": "Strict",
        "unspecified": "Lax"
    }

    # 用列表推导式转换格式
    converted = [
        {
            "name": c["name"],
            "value": c["value"],
            "domain": c["domain"],
            "path": c.get("path", "/"),
            "secure": c.get("secure", False),
            "httpOnly": c.get("httpOnly", False),
            "expires": int(c["expirationDate"]) if "expirationDate" in c else -1,
            "sameSite": same_site_map.get(
                c.get("sameSite", "").lower() if isinstance(c.get("sameSite"), str) else "unspecified",
                "Lax"
            )
        }
        for c in json.loads(cookies)
    ]

    return converted