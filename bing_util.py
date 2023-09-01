# -*- coding: utf-8 -*-
import asyncio
import json
from fastapi import FastAPI, Request, Response, Depends, HTTPException
from pydantic import BaseModel
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
cookies = json.loads(open("cookie.json", encoding="utf-8").read())
app = FastAPI()

# 定义一个输入模型类，用于验证和序列化输入数据
class Input(BaseModel):
    prompts: list
    sem: int
    style: str
    cookie_U: str

class InputUpdate(BaseModel):
    text: str


# 定义一个辅助函数，用于从参数中提取有用的信息
def get_num(param):
    for _ in param:
        if 'sourceAttributions' in _:
            return _
    return None

# 定义一个异步函数，用于调用Chatbot对象的ask方法，并返回文本和来源
async def get_ask(prompt, style):
    source = []
    for n in range(5):
        try:
            bot = await Chatbot.create(cookies=cookies)
            text_json = await bot.ask(prompt=prompt, conversation_style=getattr(ConversationStyle, style))
            text_json = get_num(text_json["item"]["messages"])
            text = text_json['text']
            try:
                for items in text_json['sourceAttributions']:
                    source.append(f"{items['providerDisplayName']}\t{items['seeMoreUrl']}")
            except Exception as e:
                print(e)
            source = list(set(source))
            return text, source
        except Exception as e:
            print(e)
        finally:
            try:
                await bot.close()
            except Exception as e:
                print(e)
    return '返回错误', []

# 定义一个异步函数，用于并发地调用get_ask函数，并将结果存储在result列表中
async def bing(quest, semaphore, n, style):
    async with semaphore:
        result.append([])
        text, source = await get_ask(quest, style)
        result[n] = [text, source]

# 定义一个异步函数，用于创建一个信号量，并创建多个协程任务来执行bing函数
async def main_process(result, sem, style):
    semaphore = asyncio.Semaphore(sem)  # 进程中协程数控制
    tasks = [asyncio.create_task(bing(line, semaphore, n, style)) for n, line in enumerate(result)]
    await asyncio.wait(tasks)

result = []
# 定义一个路由函数，用于处理POST请求，并返回响应数据
# uvicorn bing_util:app --reload
@app.post("/bing")
async def deduplicate_api(input: Input):
    global result
    print('调用接口')
    result = []
    cookies[10]['value'] = input.cookie_U
    await main_process(input.prompts, input.sem, input.style)
    print('调用结束')
    return result

# 定义一个PUT请求的路由函数，用于更新cookie.json文件
@app.put("/update-cookie")
async def update_cookie(new_cookie: InputUpdate):
    # 打开cookie.json文件，并读取其中的内容
    with open("cookie.json", "w", encoding="utf-8") as f:
        f.write(new_cookie.text)