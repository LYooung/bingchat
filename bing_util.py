# -*- coding: utf-8 -*-
import asyncio
import json
from fastapi import FastAPI, Request, Response, Depends, HTTPException
from pydantic import BaseModel
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
# cookies = json.loads(open("cookie.json", encoding="utf-8").read())
app = FastAPI()

# 定义一个输入模型类，用于验证和序列化输入数据
class Input(BaseModel):
    prompts: list
    sem: int
    style: str
    cookie: bool

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
            # if cookie:
            #     bot = await Chatbot.create(cookies=cookies)
            # else:
            #     bot = await Chatbot.create()
            bot = await Chatbot.create()
            text_json = await bot.ask(prompt=prompt, conversation_style=getattr(ConversationStyle, style))
            text_json = get_num(text_json["item"]["messages"])
            text = text_json['text']
            try:
                for items in text_json['sourceAttributions']:
                    source.append(f"{items['providerDisplayName']}\t{items['seeMoreUrl']}")
            except:
                pass
            source = list(set(source))
            return text, source
        except Exception as e:
            # 使用HTTPException来处理异常，并返回错误信息
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            try:
                await bot.close()
            except:
                pass
    return ''

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
# cookie = False
# 定义一个路由函数，用于处理POST请求，并返回响应数据
@app.post("/bing")
async def deduplicate_api(input: Input):
    # global cookie
    # 使用Depends参数来调用依赖函数
    # cookie = input.style
    await main_process(input.prompts, input.sem, input.style)
    return result
