from typing import List

from pydantic import BaseModel


class Symbol(BaseModel):
    symbol: str


class Symbols(BaseModel):
    symbols: List[Symbol]
