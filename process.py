from vnstock3 import Vnstock

def get_stock_obj(symbol, source):
    return Vnstock().stock(symbol=symbol, source=source)


def get_all_symbols(symbol, source):
    stock =  get_stock_obj(symbol=symbol, source=source)
    return stock.listing.all_symbols().to_dict(orient="index")


def get_symbols_by_exchange(symbol, source):
    stock = get_stock_obj(symbol=symbol, source=source)
    return stock.listing.symbols_by_exchange().to_dict(orient="index")
