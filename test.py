import requests
# 定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
# 定义请求参数
params = {
    "prompts": ["你好", "你叫什么名字"],
    "sem": 1,
    "style": "creative",
    "cookie": False
}
# 发送请求
# response = requests.post("https://chattest-1umk.onrender.com/bing", headers=headers, json=params)
response = requests.post("http://127.0.0.1:8000/bing", headers=headers, json=params)
# 打印返回结果
print(response.text)
