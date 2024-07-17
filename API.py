from fastapi import FastAPI, HTTPException
from process import *

app = FastAPI()

@app.get("/stock_info/{symbol}_{source}")
async def get_stock(symbol: str, source: str):
    stock = get_stock_obj(symbol=symbol, source=source)
    if stock is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {
        "symbol": symbol,
        "source": source,
        }


@app.get("/stock_info/{symbol}_{source}/symbols")
async def get_stock_all_symbols(symbol: str, source: str):
    symbols = get_all_symbols(symbol=symbol, source=source)
    return {
        "symbol": symbol,
        "source": source,
        "all_symbols": symbols,
    }


@app.get("/stock_info/{symbol}_{source}/symbols_by_exchange")
async def get_stock_symbols_by_exchange(symbol: str, source: str):
    symbols_by_exchange = get_symbols_by_exchange(symbol=symbol, source=source)

    return {
        "symbol": symbol,
        "source": source,
        "all_symbols": symbols_by_exchange,
    }
