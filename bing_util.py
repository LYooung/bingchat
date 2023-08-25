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

# 定义一个响应模型类，用于验证和序列化输出数据
class Output(BaseModel):
    text: str
    source: list

# 定义一个辅助函数，用于从参数中提取有用的信息
def get_num(param):
    for _ in param:
        if 'sourceAttributions' in _:
            return _
    return None

# 定义一个异步函数，用于调用Chatbot对象的ask方法，并返回文本和来源
async def get_ask(prompt, style, bot: Chatbot):
    source = []
    for n in range(10):
        try:
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
    return ''

# 定义一个异步函数，用于并发地调用get_ask函数，并将结果存储在result列表中
async def bing(quest, semaphore, n, style, bot: Chatbot):
    async with semaphore:
        result.append([])
        text, source = await get_ask(quest, style, bot)
        result[n] = [text, source]

# 定义一个异步函数，用于创建一个信号量，并创建多个协程任务来执行bing函数
async def main_process(result, sem, style: str, bot: Chatbot):
    async with sem:
        semaphore = asyncio.Semaphore(20)  # 进程中协程数控制
        tasks = [asyncio.create_task(bing(line, semaphore, n, style, bot)) for n, line in enumerate(result)]
        await asyncio.wait(tasks)

result = []

# 定义一个依赖函数，用于返回一个Chatbot对象，并在使用完后关闭它
def get_bot():
    bot = Chatbot.create()
    yield bot
    bot.close()

# 定义一个路由函数，用于处理POST请求，并返回响应数据
@app.post("/bing", response_model=Output)
async def deduplicate_api(input: Input, bot: Chatbot = Depends(get_bot)):
    # 使用Depends参数来调用依赖函数
    await main_process(input.prompts, input.sem, input.style, bot)
    return result
