# import datetime as dt
# from typing import List, Optional
# from fastapi import FastAPI, Response, HTTPException, Query
# from pydantic import BaseModel, Field

# class TradeDetails(BaseModel):
#     buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")
#     price: float = Field(description="The price of the Trade.")
#     quantity: int = Field(description="The amount of units traded.")

# class Trade(BaseModel):
#     assetClass: Optional[str] = Field(description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")
#     counterparty: Optional[str] = Field(description="The counterparty the trade was executed with. May not always be available")
#     instrumentId: str = Field(description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")
#     instrumentName: str = Field(description="The name of the instrument traded.")
#     tradeDateTime: dt.datetime = Field(description="The date-time the Trade was executed")
#     tradeDetails: TradeDetails = Field(description="The details of the trade, i.e. price, quantity")
#     tradeId: Optional[str] = Field(description="The unique ID of the trade")
#     trader: str = Field(description="The name of the Trader")

# # Mock database or data source
# trades_db = [
#     Trade(
#         assetClass="Equity",
#         counterparty="ABC Company",
#         instrumentId="AAPL",
#         instrumentName="Apple Inc.",
#         tradeDateTime=dt.datetime(2023, 6, 5, 12, 30, 0),
#         tradeDetails=TradeDetails(
#             buySellIndicator="BUY",
#             price=10.5,
#             quantity=100
#         ),
#         tradeId="1",
#         trader="John Doe"
#     ),
#     Trade(
#         assetClass="Equity",
#         counterparty="XYZ Corporation",
#         instrumentId="GOOGL",
#         instrumentName="Alphabet Inc.",
#         tradeDateTime=dt.datetime(2023, 6, 5, 13, 45, 0),
#         tradeDetails=TradeDetails(
#             buySellIndicator="SELL",
#             price=15.2,
#             quantity=200
#         ),
#         tradeId="2",
#         trader="Jane Smith"
#     )
# ]

# app = FastAPI()

# class TradeResponse(BaseModel):
#     trades: List[Trade]



# @app.get("/trades", response_model=TradeResponse)
# def pagination_trades(
#     page: Optional[int] = Query(1, ge=1, description="Page number"),
#     size: Optional[int] = Query(10, ge=1, le=100, description="Page size"),
#     sort_by: Optional[str] = Query(None, description="Field to sort by"),
#     sort_order: Optional[str] = Query("asc", description="Sort order (asc or desc)")
# ):
#     # Apply pagination
#     start_index = (page - 1) * size
#     end_index = start_index + size

#     # Apply sorting
#     if sort_by:
#         trades_db.sort(key=lambda t: getattr(t, sort_by), reverse=sort_order == "desc")

#     # Retrieve trades based on pagination and sorting
#     paginated_trades = trades_db[start_index:end_index]

#     return TradeResponse(trades=paginated_trades)



# @app.get("/trades", response_model=TradeResponse)
# def advance_filter_trades(
#     response: Response,
#     assetClass: Optional[str] = Query(None, description="Asset class of the trade"),
#     end: Optional[dt.datetime] = Query(None, description="The maximum date for the tradeDateTime field"),
#     maxPrice: Optional[float] = Query(None, description="The maximum value for the tradeDetails.price field"),
#     minPrice: Optional[float] = Query(None, description="The minimum value for the tradeDetails.price field"),
#     start: Optional[dt.datetime] = Query(None, description="The minimum date for the tradeDateTime field"),
#     tradeType: Optional[str] = Query(None, description="The tradeDetails.buySellIndicator is a BUY or SELL")
# ):
#     filtered_trades = trades_db

#     if assetClass:
#         filtered_trades = [trade for trade in filtered_trades if trade.assetClass == assetClass]

#     if end:
#         filtered_trades = [trade for trade in filtered_trades if trade.tradeDateTime <= end]

#     if maxPrice:
#         filtered_trades = [trade for trade in filtered_trades if trade.tradeDetails.price <= maxPrice]

#     if minPrice:
#         filtered_trades = [trade for trade in filtered_trades if trade.tradeDetails.price >= minPrice]

#     if start:
#         filtered_trades = [trade for trade in filtered_trades if trade.tradeDateTime >= start]

#     if tradeType:
#         filtered_trades = [trade for trade in filtered_trades if trade.tradeDetails.buySellIndicator == tradeType]

#     return TradeResponse(trades=filtered_trades)




# @app.get("/trades", response_model=TradeResponse)
# def search_trades(response: Response, search: Optional[str] = Query(None, description="Search text to filter trades")):
#     filtered_trades = []
#     if search:
#         for trade in trades_db:
#             if (
#                 search.lower() in trade.counterparty.lower()
#                 or search.lower() in trade.instrumentId.lower()
#                 or search.lower() in trade.instrumentName.lower()
#                 or search.lower() in trade.trader.lower()
#             ):
#                 filtered_trades.append(trade)
#     else:
#         filtered_trades = trades_db

#     return TradeResponse(trades=filtered_trades)





# @app.get("/trades/{trade_id}", response_model=Trade)
# def get_trade_by_id(trade_id: str):
#     for trade in trades_db:
#         if trade.tradeId == trade_id:
#             return trade
#     raise HTTPException(status_code=404, detail="Trade not found")

# def filter_trades(search_query: str) -> List[Trade]:
#     filtered_trades = []
#     for trade in trades_db:
#         if search_query.lower() in trade.counterparty.lower() or \
#            search_query.lower() in trade.instrumentId.lower() or \
#            search_query.lower() in trade.instrumentName.lower() or \
#            search_query.lower() in trade.trader.lower():
#             filtered_trades.append(trade)
#     return filtered_trades






import datetime as dt
from typing import List, Optional
from fastapi import FastAPI, Response, HTTPException, Query
from pydantic import BaseModel, Field

class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")
    price: float = Field(description="The price of the Trade.")
    quantity: int = Field(description="The amount of units traded.")

class Trade(BaseModel):
    assetClass: Optional[str] = Field(description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")
    counterparty: Optional[str] = Field(description="The counterparty the trade was executed with. May not always be available")
    instrumentId: str = Field(description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")
    instrumentName: str = Field(description="The name of the instrument traded.")
    tradeDateTime: dt.datetime = Field(description="The date-time the Trade was executed")
    tradeDetails: TradeDetails = Field(description="The details of the trade, i.e. price, quantity")
    tradeId: Optional[str] = Field(description="The unique ID of the trade")
    trader: str = Field(description="The name of the Trader")

# Mock database or data source
trades_db = [
    Trade(
        assetClass="Equity",
        counterparty="ABC Company",
        instrumentId="AAPL",
        instrumentName="Apple Inc.",
        tradeDateTime=dt.datetime(2023, 6, 5, 12, 30, 0),
        tradeDetails=TradeDetails(
            buySellIndicator="BUY",
            price=10.5,
            quantity=100
        ),
        tradeId="1",
        trader="John Doe"
    ),
    Trade(
        assetClass="Equity",
        counterparty="XYZ Corporation",
        instrumentId="GOOGL",
        instrumentName="Alphabet Inc.",
        tradeDateTime=dt.datetime(2023, 6, 5, 13, 45, 0),
        tradeDetails=TradeDetails(
            buySellIndicator="SELL",
            price=15.2,
            quantity=200
        ),
        tradeId="2",
        trader="Jane Smith"
    )
]

app = FastAPI()

class TradeResponse(BaseModel):
    trades: List[Trade]

@app.get("/trades", response_model=TradeResponse)
def get_trades(
    response: Response,
    page: Optional[int] = Query(1, ge=1, description="Page number"),
    size: Optional[int] = Query(10, ge=1, le=100, description="Page size"),
    sort_by: Optional[str] = Query(None, description="Field to sort by"),
    sort_order: Optional[str] = Query("asc", description="Sort order (asc or desc)"),
    assetClass: Optional[str] = Query(None, description="Asset class of the trade"),
    end: Optional[dt.datetime] = Query(None, description="The maximum date for the tradeDateTime field"),
    maxPrice: Optional[float] = Query(None, description="The maximum value for the tradeDetails.price field"),
    minPrice: Optional[float] = Query(None, description="The minimum value for the tradeDetails.price field"),
    start: Optional[dt.datetime] = Query(None, description="The minimum date for the tradeDateTime field"),
    tradeType: Optional[str] = Query(None, description="The tradeDetails.buySellIndicator is a BUY or SELL"),
    search: Optional[str] = Query(None, description="Search text to filter trades")
):
    filtered_trades = trades_db

    if assetClass:
        filtered_trades = [trade for trade in filtered_trades if trade.assetClass == assetClass]

    if end:
        filtered_trades = [trade for trade in filtered_trades if trade.tradeDateTime <= end]

    if maxPrice:
        filtered_trades = [trade for trade in filtered_trades if trade.tradeDetails.price <= maxPrice]

    if minPrice:
        filtered_trades = [trade for trade in filtered_trades if trade.tradeDetails.price >= minPrice]

    if start:
        filtered_trades = [trade for trade in filtered_trades if trade.tradeDateTime >= start]

    if tradeType:
        filtered_trades = [trade for trade in filtered_trades if trade.tradeDetails.buySellIndicator == tradeType]

    if search:
        filtered_trades = [
            trade for trade in filtered_trades
            if (
                search.lower() in trade.counterparty.lower()
                or search.lower() in trade.instrumentId.lower()
                or search.lower() in trade.instrumentName.lower()
                or search.lower() in trade.trader.lower()
            )
        ]

    # Apply sorting
    if sort_by:
        filtered_trades.sort(key=lambda t: getattr(t, sort_by), reverse=sort_order == "desc")

    # Apply pagination
    start_index = (page - 1) * size
    end_index = start_index + size
    paginated_trades = filtered_trades[start_index:end_index]

    return TradeResponse(trades=paginated_trades)


@app.get("/trades/{trade_id}", response_model=Trade)
def get_trade_by_id(trade_id: str):
    for trade in trades_db:
        if trade.tradeId == trade_id:
            return trade
    raise HTTPException(status_code=404, detail="Trade not found")
