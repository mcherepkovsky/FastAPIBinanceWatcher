from fastapi import APIRouter

from app.redis_tools.tools import RedisTools
from app.exceptions import PairDoesntExists

router = APIRouter(
    prefix="/api/v1/currency",
    tags=["Валюта"]
)


@router.get("/all-pairs")
async def get_all_pairs():
    pairs = [pair.decode('utf-8') for pair in await RedisTools.get_all_pairs()]

    return pairs


@router.get("/popular-pairs")
async def get_popular_pairs():
    popular_pairs = await RedisTools.get_popular_pairs()
    popular_pairs = eval(popular_pairs) if popular_pairs else {}
    return {"popular_pairs": popular_pairs}


@router.get("/{pair}")
async def get_currency_pair(pair: str):
    if pair not in [s.decode('utf-8') for s in await RedisTools.get_all_pairs()]:
        raise PairDoesntExists

    return {
        "pair": pair,
        "price": float(await RedisTools.get_pair(pair))
    }

