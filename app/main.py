from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.redis_tools.tools import RedisTools
from app.services.binance import router as binance_router
from app.pages.router import router as pages_router

import aiohttp

from app.services.schemas import Symbols

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

# Глобальная переменная для aiohttp.ClientSession
aiohttp_client: aiohttp.ClientSession = None


@app.on_event("startup")
async def on_startup():
    global aiohttp_client
    aiohttp_client = aiohttp.ClientSession()


@app.on_event("shutdown")
async def on_shutdown():
    global aiohttp_client
    await aiohttp_client.close()


@app.on_event("startup")
@repeat_every(seconds=60 * 60 * 24 * 7)  # Запуск каждые 12 часов
async def refresh_pairs():
    global aiohttp_client
    async with aiohttp_client.get(f"{settings.ALL_PAIRS_KEY}") as response:
        response_json = await response.json()
        parsed_pairs = Symbols(**response_json)
        symbols = [pair.symbol for pair in parsed_pairs.symbols]
        pairs_dict = {symbol: 0 for symbol in symbols}
        await RedisTools.set_all_pairs(pairs_dict)


@app.on_event("startup")
@repeat_every(seconds=60)  # Запуск каждые 60 секунд
async def update_popular_pairs():
    global aiohttp_client
    async with aiohttp_client.get(f"{settings.BINANCE_API_URL}") as response:
        response_json = await response.json()

        popular_pairs = sorted(response_json, key=lambda x: float(x["quoteVolume"]), reverse=True)[:10]
        top_pairs = {pair["symbol"]: pair["openPrice"] for pair in popular_pairs}
        await RedisTools.set_popular_pairs(str(top_pairs))


@app.on_event("startup")
@repeat_every(seconds=5)
async def on_loop_startup():
    global aiohttp_client
    pairs = await RedisTools.get_all_pairs()  # Получаем словарь с парами и их значениями
    for symbol, value in pairs.items():
        url = f"{settings.CURRENCY_PAIR_KEY}{symbol.decode('utf-8')}"
        async with aiohttp_client.get(url) as response:
            response_json = await response.json()
            new_price = response_json["price"]

            await RedisTools.set_pair(symbol, new_price)


app.include_router(binance_router)
app.include_router(pages_router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)
