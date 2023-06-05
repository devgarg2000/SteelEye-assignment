# SteelEye Assignment

This repository contains the solution for the SteelEye assignment.

## Description

The assignment involves building an API using FastAPI to manage trades. The API provides various endpoints to fetch and filter trades based on different criteria.
## Installation

To run the API locally, follow these steps:

1. Clone the repository: `git clone https://github.com/devgarg2000/SteelEye-assignment.git`
2. Navigate to the project directory: `cd SteelEye-assignment`
3. Start the server: `uvicorn main:app --reload`


The API will be accessible at `http://localhost:8000`.

## Endpoints

### 1. Fetch a List of Trades

**Endpoint:** GET /trades

This endpoint allows you to fetch a list of trades with pagination and sorting capabilities.

**Query Parameters:**

- `page` (optional, default: 1): Page number for pagination.
- `size` (optional, default: 10): Page size for pagination.
- `sort_by` (optional): Field to sort the trades by.
- `sort_order` (optional, default: "asc"): Sort order ("asc" or "desc").

### 2. Fetch a Single Trade by Trade ID

**Endpoint:** GET /trades/{trade_id}

This endpoint allows you to fetch a single trade by its trade ID.

**Path Parameters:**

- `trade_id`: ID of the trade to fetch.

### 3. Filter Trades

**Endpoint:** GET /trades

This endpoint allows you to filter trades based on different criteria.

**Query Parameters:**

- `assetClass` (optional): Asset class of the trade.
- `end` (optional): Maximum date for the tradeDateTime field.
- `maxPrice` (optional): Maximum value for the tradeDetails.price field.
- `minPrice` (optional): Minimum value for the tradeDetails.price field.
- `start` (optional): Minimum date for the tradeDateTime field.
- `tradeType` (optional): Trade type (BUY or SELL).

### 4. Search Trades

**Endpoint:** GET /trades

This endpoint allows you to search trades based on a search query.
